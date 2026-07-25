#!/usr/bin/env python3
"""Sync repo markdown into Quarto-ready pages under site/ for Posit Connect Cloud."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSIT = ROOT / "posit"
SITE = POSIT / "site"
APPS = SITE / "apps"

# (source relative to ROOT, dest under site/, title)
PAGES: list[tuple[str, str, str]] = [
    # Wiki
    ("wiki/Home.md", "guide/home.md", "Court System Guide"),
    ("wiki/Quick-Start.md", "guide/quick-start.md", "Quick Start"),
    ("wiki/Onboarding.md", "guide/onboarding.md", "Onboarding"),
    ("wiki/The-Court.md", "guide/the-court.md", "The Court"),
    ("wiki/Command-Reference.md", "guide/command-reference.md", "Command Reference"),
    ("wiki/When-to-Convene.md", "guide/when-to-convene.md", "When to Convene"),
    ("wiki/Procedures.md", "guide/procedures.md", "Procedures"),
    ("wiki/Domains-and-Experts.md", "guide/domains-and-experts.md", "Domains & Experts"),
    ("wiki/SME-Framework.md", "guide/sme-framework.md", "SME Framework"),
    ("wiki/Precedents.md", "guide/precedents.md", "Precedents (Wiki)"),
    ("wiki/State-and-Metrics.md", "guide/state-and-metrics.md", "State & Metrics"),
    ("wiki/Error-Recovery.md", "guide/error-recovery.md", "Error Recovery"),
    ("wiki/Inter-Agent-Protocol.md", "guide/inter-agent-protocol.md", "Inter-Agent Protocol"),
    ("wiki/Companion-Personas.md", "guide/companion-personas.md", "Companion Personas"),
    ("wiki/Portal.md", "guide/portal.md", "Transcript Portal"),
    ("wiki/Glossary.md", "guide/glossary.md", "Glossary"),
    ("wiki/Runbook.md", "guide/runbook.md", "Runbook"),
    ("wiki/Edge-Cases.md", "guide/edge-cases.md", "Edge Cases"),
    ("wiki/Aegis-Protocol.md", "guide/aegis-protocol.md", "Aegis Protocol"),
    ("wiki/Repository-Map.md", "guide/repository-map.md", "Repository Map"),
    ("wiki/Changelog.md", "guide/changelog.md", "Changelog (Wiki)"),
    # Core law
    ("core/personalities.md", "core/personalities.md", "Court Personalities"),
    ("core/procedures.md", "core/procedures.md", "Core Procedures"),
    ("core/MFAF.md", "core/mfaf.md", "Multi-Factor Assessment Framework"),
    ("core/sme-framework.md", "core/sme-framework.md", "SME Framework (Core)"),
    ("core/case-format.md", "core/case-format.md", "Case Naming Format"),
    ("core/error-recovery.md", "core/error-recovery.md", "Error Recovery (Core)"),
    ("core/inter-agent-protocol.md", "core/inter-agent-protocol.md", "Inter-Agent Protocol (Core)"),
    ("core/state-schema.md", "core/state-schema.md", "State Schema"),
    # Courtroom
    ("courtroom/RULES.md", "courtroom/rules.md", "Court Rules"),
    ("courtroom/BEST_PRACTICES.md", "courtroom/best-practices.md", "Best Practices"),
    ("courtroom/COURT_PROTOCOL.md", "courtroom/court-protocol.md", "Court Protocol"),
    ("courtroom/precedents.md", "courtroom/precedents.md", "Precedent Database"),
    ("courtroom/spectators.md", "courtroom/spectators.md", "Spectators"),
    ("courtroom/portal/README.md", "courtroom/portal.md", "Portal Technical Reference"),
    ("courtroom/reporter/README.md", "courtroom/reporter.md", "Court Reporter"),
    # Litigation & executive
    ("litigation/README.md", "litigation/runner.md", "Litigation Runner"),
    ("litigation/OPENROUTER_BEST_PRACTICES.md", "litigation/openrouter.md", "OpenRouter Best Practices"),
    ("executive/protocol.md", "executive/protocol.md", "Executive Protocol"),
    # Project docs
    ("MODELCARD.md", "project/modelcard.md", "Repository Card"),
    ("CHANGELOG.md", "project/changelog.md", "Project Changelog"),
    ("SECURITY.md", "project/security.md", "Security"),
    ("architecture-overview.md", "project/architecture.md", "Architecture Overview"),
    ("docs/ONBOARDING.md", "project/docs-onboarding.md", "Docs Onboarding"),
    ("docs/RUNBOOK.md", "project/docs-runbook.md", "Docs Runbook"),
    ("docs/glossary.md", "project/docs-glossary.md", "Docs Glossary"),
    ("docs/agent-schema.md", "project/agent-schema.md", "Agent Schema"),
    ("docs/agent-skills.md", "project/agent-skills.md", "Agent Skills"),
    ("docs/court-reporter.md", "project/court-reporter-docs.md", "Court Reporter Docs"),
    ("state/metrics.md", "project/metrics.md", "Metrics Dashboard"),
    ("state/current.md", "project/current-state.md", "Current Session State"),
]

# Wiki-style link targets → site paths (without .html)
WIKI_LINK_MAP = {
    "Home": "guide/home",
    "Quick-Start": "guide/quick-start",
    "Onboarding": "guide/onboarding",
    "The-Court": "guide/the-court",
    "Command-Reference": "guide/command-reference",
    "When-to-Convene": "guide/when-to-convene",
    "Procedures": "guide/procedures",
    "Domains-and-Experts": "guide/domains-and-experts",
    "SME-Framework": "guide/sme-framework",
    "Precedents": "guide/precedents",
    "State-and-Metrics": "guide/state-and-metrics",
    "Error-Recovery": "guide/error-recovery",
    "Inter-Agent-Protocol": "guide/inter-agent-protocol",
    "Companion-Personas": "guide/companion-personas",
    "Portal": "guide/portal",
    "Glossary": "guide/glossary",
    "Runbook": "guide/runbook",
    "Edge-Cases": "guide/edge-cases",
    "Aegis-Protocol": "guide/aegis-protocol",
    "Repository-Map": "guide/repository-map",
    "Changelog": "guide/changelog",
}


def front_matter(title: str) -> str:
    safe = title.replace('"', '\\"')
    return f'---\ntitle: "{safe}"\n---\n\n'


def neutralize_yaml_breaks(text: str) -> str:
    """Prevent Pandoc from treating body `---` rules as YAML front matter."""
    # Horizontal rules / transcript separators commonly use ---
    return re.sub(r"(?m)^---\s*$", "***", text)


def rewrite_wiki_links(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2)
        # Skip absolute / anchored / already-pathed links
        if target.startswith(("http://", "https://", "#", "/", "mailto:")):
            return match.group(0)
        if "/" in target or target.endswith((".md", ".qmd", ".html")):
            return match.group(0)
        mapped = WIKI_LINK_MAP.get(target)
        if mapped:
            return f"[{label}](/{mapped}.html)"
        return match.group(0)

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, text)


def strip_emoji_heading_noise(text: str) -> str:
    # Keep content; MODELCARD uses emoji in H1 — fine for Quarto.
    return text


def write_page(src: Path, dest: Path, title: str) -> None:
    raw = src.read_text(encoding="utf-8")
    # Drop leading H1 if it duplicates the Quarto title
    body = re.sub(r"^#\s+.+\n+", "", raw, count=1)
    body = rewrite_wiki_links(body)
    body = neutralize_yaml_breaks(body)
    body = strip_emoji_heading_noise(body)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(front_matter(title) + body, encoding="utf-8")


def build_transcript_index() -> None:
    transcripts = sorted((ROOT / "courtroom" / "transcripts").glob("*.md"))
    dest = SITE / "courtroom" / "transcripts.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        front_matter("Certified Transcripts"),
        "Certified deliberation transcripts from the MORNINGSTAR court.",
        "",
        "| Transcript | File |",
        "|---|---|",
    ]
    out_dir = SITE / "courtroom" / "transcripts"
    out_dir.mkdir(parents=True, exist_ok=True)
    for path in transcripts:
        title = path.stem.replace("-", " ").replace("_", " ")
        page = out_dir / f"{path.stem}.md"
        body = neutralize_yaml_breaks(path.read_text(encoding="utf-8"))
        page.write_text(front_matter(title) + body, encoding="utf-8")
        rel = f"transcripts/{path.stem}.html"
        lines.append(f"| [{title}]({rel}) | `{path.name}` |")
    lines.append("")
    dest.write_text("\n".join(lines), encoding="utf-8")


def stage_apps() -> None:
    """Copy interactive HTML apps into site/apps for Quarto resources."""
    if APPS.exists():
        shutil.rmtree(APPS)
    APPS.mkdir(parents=True)

    # Live courtroom UI (stable path; Quarto index.qmd must not own root index.html)
    live_src = ROOT / "courtroom" / "live"
    apps_court = APPS / "live-courtroom"
    if apps_court.exists():
        shutil.rmtree(apps_court)
    shutil.copytree(live_src, apps_court)

    # Portal viewer
    portal_src = ROOT / "courtroom" / "portal"
    portal_dst = APPS / "portal"
    portal_dst.mkdir(parents=True)
    for name in ("viewer.html", "dracula.css", "transcripts_manifest.json"):
        src = portal_src / name
        if src.exists():
            shutil.copy2(src, portal_dst / name)
    # Copy transcripts for portal fetch (markdown)
    t_dst = portal_dst / "transcripts"
    t_dst.mkdir(exist_ok=True)
    for md in (ROOT / "courtroom" / "transcripts").glob("*.md"):
        shutil.copy2(md, t_dst / md.name)
    # Fix viewer paths if needed — viewer typically fetches relative to repo root;
    # rewrite common prefixes to local copies.
    viewer = portal_dst / "viewer.html"
    if viewer.exists():
        v = viewer.read_text(encoding="utf-8")
        v = v.replace("../transcripts/", "transcripts/")
        v = v.replace("../../courtroom/transcripts/", "transcripts/")
        v = v.replace("transcripts_manifest.json", "transcripts_manifest.json")
        viewer.write_text(v, encoding="utf-8")

    # Landing page for apps
    (SITE / "apps" / "index.md").write_text(
        front_matter("Interactive Applications")
        + """
The MORNINGSTAR repository includes browser applications. On this Posit Connect Cloud site they are published as static resources.

## Live Courtroom Session

Open the full deliberation UI (OpenRouter / proxy-capable courtroom workflow):

**[Launch Live Courtroom](live-courtroom/index.html){.btn .btn-primary}**

## Transcript Portal Viewer

Browse certified transcripts in the Dracula-themed portal:

**[Open Transcript Portal](portal/viewer.html){.btn .btn-secondary}**

> Note: Live LLM calls require an OpenRouter API key (or the optional Node proxy). Portal browsing works fully offline from the staged transcript corpus.
""",
        encoding="utf-8",
    )


def experts_page() -> None:
    src = ROOT / "courtroom" / "domains" / "experts.yaml"
    dest = SITE / "courtroom" / "experts.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    yaml_text = src.read_text(encoding="utf-8") if src.exists() else "_experts.yaml missing_"
    dest.write_text(
        front_matter("SME Expert Registry")
        + "Canonical expert roster from `courtroom/domains/experts.yaml`.\n\n"
        + "```yaml\n"
        + yaml_text
        + "\n```\n",
        encoding="utf-8",
    )


def main() -> None:
    if SITE.exists():
        # Preserve hand-authored files if any; rebuild generated tree cleanly
        for child in SITE.iterdir():
            if child.name in {"apps", "guide", "core", "courtroom", "litigation", "executive", "project"}:
                shutil.rmtree(child)
    SITE.mkdir(exist_ok=True)

    for src_rel, dest_rel, title in PAGES:
        src = ROOT / src_rel
        if not src.is_file():
            print(f"SKIP missing {src_rel}")
            continue
        write_page(src, SITE / dest_rel, title)
        print(f"OK {dest_rel}")

    build_transcript_index()
    experts_page()
    stage_apps()
    print(f"Site pages ready under {SITE}")


if __name__ == "__main__":
    main()
