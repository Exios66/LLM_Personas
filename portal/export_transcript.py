#!/usr/bin/env python3
"""
Export a single MORNINGSTAR transcript .md file to styled HTML.

Used by portal/launch.sh when no pre-built .html exists.
No external dependencies; uses only the standard library.

Usage:
    python portal/export_transcript.py <path-to-transcript.md> [-o output.html]

Output defaults to portal/exports/<basename>.html
"""

import argparse
import re
import sys
from pathlib import Path

# Project paths
SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
TRANSCRIPTS_DIR = BASE_DIR / "courtroom" / "transcripts"
EXPORTS_DIR = SCRIPT_DIR / "exports"

# Dracula theme + courtroom personality styling (matches portal)
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | MORNINGSTAR</title>
    <style>
        :root {{
            --bg: #282a36;
            --bg-light: #44475a;
            --bg-lighter: #343746;
            --fg: #f8f8f2;
            --comment: #6272a4;
            --cyan: #8be9fd;
            --green: #50fa7b;
            --orange: #ffb86c;
            --pink: #ff79c6;
            --purple: #bd93f9;
            --red: #ff5555;
            --yellow: #f1fa8c;
            --border: #44475a;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Georgia', 'Times New Roman', serif;
            background: var(--bg);
            color: var(--fg);
            line-height: 1.7;
            max-width: 1000px;
            margin: 0 auto;
            padding: 2rem;
        }}
        header {{ text-align: center; border-bottom: 2px solid var(--purple); padding-bottom: 2rem; margin-bottom: 2rem; }}
        header h1 {{ color: var(--purple); font-size: 2rem; letter-spacing: 0.1em; }}
        header p {{ color: var(--comment); font-style: italic; margin-top: 0.5rem; }}
        h1, h2, h3, h4 {{ color: var(--purple); margin: 1.5rem 0 0.75rem 0; }}
        h2 {{ color: var(--cyan); font-size: 1.3rem; }}
        h3 {{ color: var(--cyan); font-size: 1.1rem; }}
        p {{ margin: 0.75rem 0; }}
        pre {{ background: var(--bg-light); border: 1px solid var(--border); border-left: 3px solid var(--purple); padding: 1rem; border-radius: 6px; overflow-x: auto; margin: 1rem 0; }}
        code {{ background: var(--bg-light); color: var(--pink); padding: 0.2em 0.4em; border-radius: 4px; font-family: 'Fira Code', monospace; }}
        pre code {{ background: none; color: var(--fg); padding: 0; }}
        table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
        th, td {{ border: 1px solid var(--border); padding: 0.75rem; text-align: left; }}
        th {{ background: var(--bg-light); color: var(--purple); font-weight: 600; }}
        hr {{ border: none; border-top: 1px solid var(--border); margin: 2rem 0; }}
        blockquote {{ border-left: 4px solid var(--purple); padding-left: 1rem; margin: 1rem 0; color: var(--comment); }}
        ul, ol {{ margin: 0.75rem 0; padding-left: 1.5rem; }}
        li {{ margin: 0.25rem 0; }}
        strong {{ color: var(--yellow); }}
        .p-morningstar {{ color: var(--purple); font-weight: bold; }}
        .p-architect {{ color: var(--cyan); font-weight: bold; }}
        .p-engineer {{ color: var(--green); font-weight: bold; }}
        .p-debugger {{ color: var(--orange); font-weight: bold; }}
        .p-prophet {{ color: var(--pink); font-weight: bold; }}
        .p-scribe {{ color: var(--comment); font-weight: bold; }}
        .vote-yes {{ color: var(--green); font-weight: bold; }}
        .vote-no {{ color: var(--red); font-weight: bold; }}
        .vote-abstain {{ color: var(--yellow); font-weight: bold; }}
        .footer-meta {{ color: var(--comment); font-size: 0.85em; border-top: 1px solid var(--border); padding-top: 1rem; margin-top: 3rem; text-align: center; }}
    </style>
</head>
<body>
    <header>
        <h1>MORNINGSTAR</h1>
        <p>"The court has ruled. Regrettably sensible."</p>
    </header>
    <main class="content">
{body}
    </main>
    <footer class="footer-meta">
        <p>Exported from MORNINGSTAR Courtroom Portal</p>
        <p><em>The court's rulings are its legacy.</em></p>
    </footer>
</body>
</html>
"""


def md_to_html(md: str) -> str:
    """Convert markdown to HTML. Minimal implementation, no external deps."""
    html = md

    # Escape HTML first (so we don't double-escape in code blocks)
    def escape_inline(s: str) -> str:
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # Code blocks (fenced) - protect before other transforms
    def code_block(m: re.Match) -> str:
        lang, code = m.group(1) or "", m.group(2)
        return f'<pre><code>{escape_inline(code.strip())}</code></pre>'

    html = re.sub(r"```(\w*)\n([\s\S]*?)```", code_block, html)

    # Headers (at line start)
    html = re.sub(r"^#### (.+)$", r"<h4>\1</h4>", html, flags=re.MULTILINE)
    html = re.sub(r"^### (.+)$", r"<h3>\1</h3>", html, flags=re.MULTILINE)
    html = re.sub(r"^## (.+)$", r"<h2>\1</h2>", html, flags=re.MULTILINE)
    html = re.sub(r"^# (.+)$", r"<h1>\1</h1>", html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", html)
    html = re.sub(r"_(.+?)_", r"<em>\1</em>", html)

    # Inline code (single backticks)
    html = re.sub(r"`([^`]+)`", r"<code>\1</code>", html)

    # Links
    html = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', html)

    # Horizontal rules
    html = re.sub(r"^---\s*$", "<hr>", html, flags=re.MULTILINE)

    # Blockquotes
    html = re.sub(r"^>\s*(.+)$", r"<blockquote>\1</blockquote>", html, flags=re.MULTILINE)

    # Tables: | a | b | -> <tr><td>a</td><td>b</td></tr>; separator row skipped
    lines = html.split("\n")
    in_table = False
    out = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^\|.+\|$", stripped):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if not cells:
                continue
            if all(re.match(r"^[-:\s]+$", c) for c in cells):
                continue  # separator row
            if not in_table:
                out.append("<table>")
                in_table = True
            out.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
        else:
            if in_table:
                out.append("</table>")
                in_table = False
            out.append(line)
    if in_table:
        out.append("</table>")
    html = "\n".join(out)

    # Unordered list items
    html = re.sub(r"^[-*]\s+(.+)$", r"<li>\1</li>", html, flags=re.MULTILINE)
    # Wrap consecutive <li> in <ul>
    html = re.sub(r"(<li>[\s\S]*?</li>\n?)+", lambda m: "<ul>" + m.group(0) + "</ul>", html)

    # Paragraphs: lines that are not already block elements
    lines = html.split("\n")
    result = []
    for line in lines:
        trimmed = line.strip()
        if not trimmed:
            result.append("")
            continue
        if trimmed.startswith("<") and (trimmed.startswith("<h") or trimmed.startswith("<p") or trimmed.startswith("<ul") or trimmed.startswith("<li") or trimmed.startswith("<table") or trimmed.startswith("<tr") or trimmed.startswith("<td") or trimmed.startswith("<th") or trimmed.startswith("<pre") or trimmed.startswith("<blockquote") or trimmed.startswith("<hr")):
            result.append(line)
            continue
        result.append(f"<p>{trimmed}</p>")
    html = "\n".join(result)

    return html


def apply_personality_styling(html: str) -> str:
    """Wrap personality names and votes in span classes."""
    # Use capturing group so \1 is valid in replacement
    patterns = [
        (r"\b(MORNINGSTAR|Morningstar)\b", "p-morningstar"),
        (r"\b(ARCHITECT|Architect)\b", "p-architect"),
        (r"\b(ENGINEER|Engineer)\b", "p-engineer"),
        (r"\b(DEBUGGER|Debugger)\b", "p-debugger"),
        (r"\b(PROPHET|Prophet)\b", "p-prophet"),
        (r"\b(SCRIBE|Scribe)\b", "p-scribe"),
        (r"\b(YES)\b", "vote-yes"),
        (r"\b(NO)\b", "vote-no"),
        (r"\b(ABSTAIN|RECUSED)\b", "vote-abstain"),
    ]
    for pattern, cls in patterns:
        html = re.sub(pattern, rf'<span class="{cls}">\1</span>', html)
    return html


def extract_title(md_path: Path, content: str) -> str:
    """Derive a human-readable title from path or first H1."""
    m = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    stem = md_path.stem
    # 2026-02-15-framework-enhancement-analysis -> Framework Enhancement Analysis
    if re.match(r"\d{4}-\d{2}-\d{2}-", stem):
        topic = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", stem)
        return topic.replace("-", " ").title()
    if re.match(r"\d{8}_\d{6}_", stem):
        parts = stem.split("_", 2)
        if len(parts) >= 3:
            return parts[2].replace("_", " ").title()
    return stem.replace("_", " ").replace("-", " ").title()


def main() -> int:
    parser = argparse.ArgumentParser(description="Export MORNINGSTAR transcript .md to HTML")
    parser.add_argument("transcript", help="Path to transcript .md file")
    parser.add_argument("-o", "--output", help="Output HTML path (default: portal/exports/<basename>.html)")
    args = parser.parse_args()

    src = Path(args.transcript)
    if not src.is_absolute():
        src = BASE_DIR / args.transcript.lstrip("/")
    if not src.exists():
        print(f"Error: File not found: {src}", file=sys.stderr)
        return 1
    if src.suffix.lower() != ".md":
        print("Error: Input must be a .md file.", file=sys.stderr)
        return 1

    content = src.read_text(encoding="utf-8")
    title = extract_title(src, content)
    body_html = md_to_html(content)
    body_html = apply_personality_styling(body_html)

    if args.output:
        out_path = Path(args.output)
        if not out_path.is_absolute():
            out_path = BASE_DIR / args.output
    else:
        EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
        out_path = EXPORTS_DIR / f"{src.stem}.html"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    html = HTML_TEMPLATE.format(title=title, body=body_html)
    out_path.write_text(html, encoding="utf-8")
    print(str(out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
