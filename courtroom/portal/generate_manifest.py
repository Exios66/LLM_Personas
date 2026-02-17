#!/usr/bin/env python3
"""
Generate a manifest of transcript .md files for the portal viewer.

Writes portal/transcripts_manifest.json so the viewer can discover
transcripts without hardcoding KNOWN_TRANSCRIPTS. Run from project root
or before serving the portal.

Usage:
    python3 portal/generate_manifest.py
    # or from project root:
    python3 portal/generate_manifest.py

Output: portal/transcripts_manifest.json
"""

import json
import re
from pathlib import Path
from typing import Optional

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
TRANSCRIPTS_DIR = BASE_DIR / "courtroom" / "transcripts"
OUTPUT_FILE = SCRIPT_DIR / "transcripts_manifest.json"


def parse_basename(basename: str):
    """Return (date_display, title) for a transcript basename."""
    # YYYY-MM-DD-topic
    if re.match(r"^\d{4}-\d{2}-\d{2}-", basename):
        date_part = basename[:10]
        title = basename[11:].replace("-", " ").title() if len(basename) > 11 else basename
        return date_part, title
    # YYYYMMDD_HHMMSS_topic
    m = re.match(r"^(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})\d{2}_(.+)$", basename)
    if m:
        date_display = f"{m.group(1)}-{m.group(2)}-{m.group(3)} {m.group(4)}:{m.group(5)}"
        title = m.group(6).replace("_", " ").title()
        return date_display, title
    return "Unknown", basename.replace("_", " ").replace("-", " ").title()


def extract_case_number(content: str) -> Optional[str]:
    """Extract case number from transcript content (Case No. or Matter ID)."""
    m = re.search(r"\*\*Case No\.\*\*:\s*(\d{4}-[A-Z]+-\d{3}(?:-\d+)?)", content, re.I)
    if m:
        return m.group(1)
    m = re.search(r"\*\*Matter ID\*\*:\s*(\d{4}-[A-Z]+-\d{3}(?:-\d+)?)", content, re.I)
    return m.group(1) if m else None


def main() -> None:
    if not TRANSCRIPTS_DIR.exists():
        manifest = {"transcripts": [], "generated": ""}
        OUTPUT_FILE.write_text(json.dumps(manifest, indent=2))
        return

    transcripts = []
    for path in sorted(TRANSCRIPTS_DIR.glob("*.md")):
        if path.name.startswith(".") or path.name == "README.md" or path.name.startswith("HANDOFF"):
            continue
        basename = path.stem
        date_display, title = parse_basename(basename)
        content = path.read_text(encoding="utf-8")
        case_number = extract_case_number(content)
        entry = {
            "filename": path.name,
            "basename": basename,
            "date": date_display,
            "title": title,
        }
        if case_number:
            entry["case_number"] = case_number
        transcripts.append(entry)

    from datetime import datetime
    manifest = {
        "transcripts": transcripts,
        "generated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    OUTPUT_FILE.write_text(json.dumps(manifest, indent=2))
    print(f"Wrote {len(transcripts)} transcript(s) to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
