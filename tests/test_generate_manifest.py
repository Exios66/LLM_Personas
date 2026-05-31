"""Tests for courtroom portal manifest generation."""

from pathlib import Path

import json
import subprocess
import sys

import pytest

from courtroom.portal.generate_manifest import extract_case_number, parse_basename

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_SCRIPT = REPO_ROOT / "courtroom" / "portal" / "generate_manifest.py"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"
MANIFEST_PATH = REPO_ROOT / "courtroom" / "portal" / "transcripts_manifest.json"


@pytest.mark.parametrize(
    ("basename", "expected_date", "expected_title_fragment"),
    [
        ("2026-05-31-deliberation", "2026-05-31", "Deliberation"),
        ("20260531_143022_session_notes", "2026-05-31 14:30", "Session Notes"),
        ("legacy_special_interest", "Unknown", "Legacy Special Interest"),
    ],
)
def test_parse_basename_formats(
    basename: str, expected_date: str, expected_title_fragment: str
) -> None:
    date_display, title = parse_basename(basename)
    assert date_display == expected_date
    assert expected_title_fragment in title


def test_extract_case_number_prefers_case_no_over_matter_id() -> None:
    content = (
        "**Matter ID**: 2026-LEG-001\n"
        "**Case No.**: 2026-DEL-042-1\n"
    )
    assert extract_case_number(content) == "2026-DEL-042-1"


def test_extract_case_number_legacy_matter_id() -> None:
    content = "**Matter ID**: 2026-SPEC-003\n"
    assert extract_case_number(content) == "2026-SPEC-003"


def test_extract_case_number_missing_returns_none() -> None:
    assert extract_case_number("No case header here.") is None


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
