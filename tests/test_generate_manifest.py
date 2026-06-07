"""Tests for courtroom portal manifest generation."""

from pathlib import Path

import json
import subprocess
import sys

from courtroom.portal.generate_manifest import extract_case_number, parse_basename


REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_SCRIPT = REPO_ROOT / "courtroom" / "portal" / "generate_manifest.py"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"
MANIFEST_PATH = REPO_ROOT / "courtroom" / "portal" / "transcripts_manifest.json"


def test_transcripts_dir_resolves_to_courtroom_transcripts():
    """Manifest generator must read courtroom/transcripts, not courtroom/courtroom/transcripts."""
    # Mirror path logic in generate_manifest.py
    script_dir = MANIFEST_SCRIPT.parent
    base_dir = script_dir.parent
    transcripts_dir = base_dir / "transcripts"
    assert transcripts_dir == TRANSCRIPTS_DIR
    assert transcripts_dir.exists()


def test_generate_manifest_includes_transcripts():
    result = subprocess.run(
        [sys.executable, str(MANIFEST_SCRIPT)],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    md_count = len(
        [
            p
            for p in TRANSCRIPTS_DIR.glob("*.md")
            if not p.name.startswith(".")
            and p.name != "README.md"
            and not p.name.upper().startswith("HANDOFF")
        ]
    )
    assert len(manifest["transcripts"]) == md_count
    assert manifest["transcripts"], "expected at least one transcript in manifest"


def test_parse_basename_iso_date_format():
    date, title = parse_basename("2026-02-17-bench-trial-topic")
    assert date == "2026-02-17"
    assert title == "Bench Trial Topic"


def test_parse_basename_legacy_timestamp_format():
    date, title = parse_basename("20260216_133000_special_interest_security")
    assert date == "2026-02-16 13:30"
    assert title == "Special Interest Security"


def test_parse_basename_unknown_falls_back_to_titleized_stem():
    date, title = parse_basename("misc_legacy_name")
    assert date == "Unknown"
    assert title == "Misc Legacy Name"


def test_extract_case_number_prefers_case_no_over_matter_id():
    content = (
        "**Case No.**: 2026-SECU-042-001\n"
        "**Matter ID**: 2026-LEGAL-001\n"
    )
    assert extract_case_number(content) == "2026-SECU-042-001"


def test_extract_case_number_reads_legacy_matter_id():
    content = "**Matter ID**: 2026-LEGAL-001\n"
    assert extract_case_number(content) == "2026-LEGAL-001"


def test_extract_case_number_returns_none_when_missing():
    assert extract_case_number("No case header in this draft.\n") is None
