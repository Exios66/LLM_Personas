#!/usr/bin/env python3
"""
Litigation Transcript Viewer

List, show, and serve litigation/transcripts from the terminal.
Akin to courtroom/portal but localized to litigation and terminal-first.

Usage:
  python viewer.py list              # List transcripts
  python viewer.py show [name]       # Print transcript (optional pager)
  python viewer.py serve [port]      # Local HTTP index + rendered transcripts
"""

import argparse
import html
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple

LITIGATION_ROOT = Path(__file__).resolve().parent
TRANSCRIPTS_DIR = LITIGATION_ROOT / "transcripts"

# Personality / vote CSS (matches courtroom portal style)
PORTAL_CSS = """
<style>
:root { --bg: #282a36; --bg-light: #44475a; --fg: #f8f8f2; --comment: #6272a4; --purple: #bd93f9; --cyan: #8be9fd; --green: #50fa7b; --pink: #ff79c6; }
* { box-sizing: border-box; }
body { font-family: 'Fira Code', 'JetBrains Mono', monospace; background: var(--bg); color: var(--fg); margin: 0; padding: 2rem; min-height: 100vh; line-height: 1.6; }
.container { max-width: 900px; margin: 0 auto; }
.header { text-align: center; padding: 2rem 0; border-bottom: 2px solid var(--purple); margin-bottom: 2rem; }
.header h1 { color: var(--purple); font-size: 2rem; margin: 0; }
.header p { color: var(--comment); font-style: italic; margin: 0.5rem 0 0 0; }
.nav { margin-bottom: 2rem; }
.nav a { color: var(--cyan); text-decoration: none; }
.nav a:hover { color: var(--pink); }
h2 { color: var(--purple); }
.transcript-list { list-style: none; padding: 0; }
.transcript-list li { background: var(--bg-light); border-radius: 8px; margin: 1rem 0; border-left: 3px solid transparent; transition: all 0.2s; }
.transcript-list li:hover { border-left-color: var(--purple); transform: translateX(5px); }
.transcript-list a { display: block; padding: 1rem 1.5rem; color: var(--fg); text-decoration: none; }
.transcript-list strong { display: block; color: var(--cyan); margin-bottom: 0.25rem; }
.transcript-date { color: var(--comment); font-size: 0.85em; }
.footer { text-align: center; color: var(--comment); font-size: 0.85em; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--bg-light); }
.content h1, .content h2, .content h3 { color: var(--purple); }
.content strong { color: var(--cyan); }
.content pre, .content code { background: var(--bg-light); padding: 0.2em 0.4em; border-radius: 4px; }
.content pre { padding: 1rem; overflow-x: auto; }
.vote-yes { color: #50fa7b !important; font-weight: bold; }
.vote-no { color: #ff5555 !important; font-weight: bold; }
.vote-abstain { color: #f1fa8c !important; font-weight: bold; }
.p-morningstar { color: #bd93f9 !important; font-weight: bold; }
.p-architect { color: #8be9fd !important; font-weight: bold; }
.p-engineer { color: #50fa7b !important; font-weight: bold; }
.p-debugger { color: #ffb86c !important; font-weight: bold; }
.p-prophet { color: #ff79c6 !important; font-weight: bold; }
.p-counsel { color: #6272a4 !important; font-weight: bold; }
</style>
"""


def _transcript_meta(path: Path) -> tuple[str, str]:
    """Return (date_str, topic) from transcript filename."""
    name = path.stem
    # YYYY-MM-DD-slug
    if len(name) >= 10 and name[4] == "-" and name[7] == "-":
        date_str = name[:10]
        topic = name[11:].replace("-", " ").title() if len(name) > 11 else name
        return date_str, topic
    return "—", name.replace("_", " ").replace("-", " ").title()


def _collect_transcripts() -> List[Tuple[Path, str, str]]:
    """Return list of (path, date_str, topic) for transcripts."""
    if not TRANSCRIPTS_DIR.exists():
        return []
    out = []
    for p in sorted(TRANSCRIPTS_DIR.glob("*.md"), key=lambda x: x.name, reverse=True):
        if p.name.startswith(".") or p.name == "README.md":
            continue
        date_str, topic = _transcript_meta(p)
        out.append((p, date_str, topic))
    return out


def cmd_list(plain: bool) -> None:
    """List transcripts in a table or plain lines."""
    rows = _collect_transcripts()
    if not rows:
        print("No transcripts in litigation/transcripts/", file=sys.stderr)
        sys.exit(0)
    if plain:
        for path, _, _ in rows:
            print(path.name)
        return
    # Table: date, topic, filename
    max_date = max(len(r[1]) for r in rows)
    max_topic = min(50, max(len(r[2]) for r in rows))
    print(f"{'Date':<{max_date}}  {'Topic':<{max_topic}}  File")
    print("-" * (max_date + max_topic + 8))
    for path, date_str, topic in rows:
        topic_short = (topic[:47] + "...") if len(topic) > 50 else topic
        print(f"{date_str:<{max_date}}  {topic_short:<{max_topic}}  {path.name}")


def cmd_show(name: Optional[str], pager: bool) -> None:
    """Print one transcript by name (exact or prefix match)."""
    rows = _collect_transcripts()
    if not rows:
        print("No transcripts in litigation/transcripts/", file=sys.stderr)
        sys.exit(1)
    if not name or name.strip() == "":
        # Show latest
        path = rows[0][0]
    else:
        name = name.strip()
        matches = [r for r in rows if r[0].stem == name or r[0].name == name or r[0].stem.startswith(name) or name in r[0].stem]
        if not matches:
            print(f"No transcript matching '{name}'", file=sys.stderr)
            print("Use 'viewer.py list' to see available transcripts.", file=sys.stderr)
            sys.exit(1)
        if len(matches) > 1:
            # Prefer exact stem match
            exact = [m for m in matches if m[0].stem == name]
            path = exact[0][0] if exact else matches[0][0]
        else:
            path = matches[0][0]
    text = path.read_text(encoding="utf-8")
    if pager:
        import subprocess
        pager_cmd = os.environ.get("PAGER", "less")
        proc = subprocess.run([pager_cmd], input=text, text=True, shell=(pager_cmd == "less"))
        sys.exit(proc.returncode)
    print(text)


def _markdown_to_html(md: str) -> str:
    """Render markdown to HTML with personality/vote styling."""
    try:
        import markdown  # type: ignore[import-untyped]
        html_body = markdown.markdown(md, extensions=["fenced_code", "tables"])
    except ImportError:
        html_body = "<pre>" + html.escape(md) + "</pre>"
    # Personality and vote spans (same patterns as courtroom portal)
    patterns = [
        (r"\b(MORNINGSTAR|Morningstar)\b", "p-morningstar"),
        (r"\b(ARCHITECT|Architect)\b", "p-architect"),
        (r"\b(ENGINEER|Engineer)\b", "p-engineer"),
        (r"\b(DEBUGGER|Debugger)\b", "p-debugger"),
        (r"\b(PROPHET|Prophet)\b", "p-prophet"),
        (r"\b(COUNSEL|Counsel)\b", "p-counsel"),
        (r"\bYES\b", "vote-yes"),
        (r"\bNO\b", "vote-no"),
        (r"\bABSTAIN\b", "vote-abstain"),
    ]
    for pattern, cls in patterns:
        html_body = re.sub(pattern, f'<span class="{cls}">\\1</span>', html_body)
    return html_body


def _index_html(rows: List[Tuple[Path, str, str]]) -> str:
    """Generate index page HTML."""
    items = "\n".join(
        f'<li><a href="/transcript/{p.stem}"><strong>{html.escape(topic)}</strong> <span class="transcript-date">{html.escape(date_str)}</span></a></li>'
        for p, date_str, topic in rows
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Litigation Transcripts</title>{PORTAL_CSS}</head>
<body>
<div class="container">
<header class="header"><h1>Litigation Transcripts</h1><p>Local viewer — litigation/transcripts</p></header>
<nav class="nav"><a href="/">&larr; Index</a></nav>
<h2>Transcripts</h2>
<ul class="transcript-list">{items}</ul>
<footer class="footer"><p>Generated {datetime.now().strftime("%Y-%m-%d %H:%M")}</p></footer>
</div>
</body>
</html>"""


def _transcript_html(path: Path, body_html: str, title: str) -> str:
    """Single transcript page HTML."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{html.escape(title)}</title>{PORTAL_CSS}</head>
<body>
<div class="container">
<header class="header"><h1>{html.escape(title)}</h1><p>{path.name}</p></header>
<nav class="nav"><a href="/">Index</a></nav>
<div class="content">{body_html}</div>
<footer class="footer"><p><a href="/">Back to index</a></p></footer>
</div>
</body>
</html>"""


def cmd_serve(port: int) -> None:
    """Run local HTTP server for index + rendered transcripts."""
    try:
        from http.server import HTTPServer, BaseHTTPRequestHandler
    except ImportError:
        print("http.server not available", file=sys.stderr)
        sys.exit(1)

    rows = _collect_transcripts()

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            path = self.path.split("?")[0].rstrip("/") or "/"
            if path == "/" or path == "/index.html":
                body = _index_html(rows).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            if path.startswith("/transcript/"):
                name = path.replace("/transcript/", "").strip("/")
                if not name:
                    self.send_error(404)
                    return
                found = None
                for p, date_str, topic in rows:
                    if p.stem == name or name in p.stem:
                        found = (p, topic)
                        break
                if not found:
                    self.send_error(404)
                    return
                p, topic = found
                md = p.read_text(encoding="utf-8")
                body_html = _markdown_to_html(md)
                title = f"In Re: {topic}"
                page = _transcript_html(p, body_html, title).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(page)))
                self.end_headers()
                self.wfile.write(page)
                return
            self.send_error(404)

        def log_message(self, format: str, *args: object) -> None:
            print(f"[{self.log_date_time_string()}] {format % args}")

    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"Litigation transcript viewer: http://127.0.0.1:{port}/")
    print("Ctrl+C to stop.")
    server.serve_forever()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Litigation transcript viewer — list, show, or serve transcripts.",
        prog="viewer.py",
    )
    sub = parser.add_subparsers(dest="command", required=True)
    list_p = sub.add_parser("list", help="List transcripts in litigation/transcripts/")
    list_p.add_argument("--plain", "-p", action="store_true", help="One filename per line (for scripts)")
    show_p = sub.add_parser("show", help="Print a transcript (by name or latest)")
    show_p.add_argument("name", nargs="?", default=None, help="Filename stem or partial match")
    show_p.add_argument("--pager", action="store_true", help="Pipe output through PAGER (e.g. less)")
    serve_p = sub.add_parser("serve", help="Run local HTTP server for browser viewing")
    serve_p.add_argument("port", nargs="?", type=int, default=8765, help="Port (default 8765)")

    args = parser.parse_args()
    if args.command == "list":
        cmd_list(plain=getattr(args, "plain", False))
    elif args.command == "show":
        cmd_show(getattr(args, "name", None), getattr(args, "pager", False))
    elif args.command == "serve":
        cmd_serve(getattr(args, "port", 8765))


if __name__ == "__main__":
    main()
