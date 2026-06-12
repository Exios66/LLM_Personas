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

# Import after path constants so module resolution matches repo layout
import importlib.util

_spec = importlib.util.spec_from_file_location("generate_manifest", MANIFEST_SCRIPT)
assert _spec and _spec.loader
_gm = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_gm)
parse_basename = _gm.parse_basename
extract_case_number = _gm.extract_case_number


def test_parse_basename_standard_and_legacy() -> None:
    date, title = parse_basename("2026-02-17-bench-trial-topic")
    assert date == "2026-02-17"
    assert title == "Bench Trial Topic"

    date2, title2 = parse_basename("20260216_133000_special_interest_security")
    assert date2 == "2026-02-16 13:30"
    assert "Special Interest" in title2 or "Security" in title2


def test_extract_case_number_prefers_case_no_over_matter_id() -> None:
    case_only = "**Case No.**: 2026-SECU-042-001\n"
    assert extract_case_number(case_only) == "2026-SECU-042-001"

    matter_only = "**Matter ID**: 2026-LEGAL-001\n"
    assert extract_case_number(matter_only) == "2026-LEGAL-001"

    both = "**Case No.**: 2026-A-001\n**Matter ID**: 2026-B-002\n"
    assert extract_case_number(both) == "2026-A-001"


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


def test_parse_basename_standard_date_topic():
    date_display, title = parse_basename("2026-02-15-aegis-protocol")
    assert date_display == "2026-02-15"
    assert title == "Aegis Protocol"


def test_parse_basename_legacy_timestamp_topic():
    date_display, title = parse_basename("20260216_133000_special_interest_security")
    assert date_display == "2026-02-16 13:30"
    assert "Security" in title


def test_extract_case_number_prefers_case_no_over_matter_id():
    content = (
        "**Matter ID**: 2026-OLD-001\n"
        "**Case No.**: 2026-SECU-042-001\n"
    )
    assert extract_case_number(content) == "2026-SECU-042-001"


def test_extract_case_number_matter_id_fallback():
    content = "**Matter ID**: 2026-LEGAL-001\n"
    assert extract_case_number(content) == "2026-LEGAL-001"
