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


@pytest.mark.parametrize(
    ("basename", "expected_date", "expected_title"),
    [
        ("2026-06-09-deliberation-session", "2026-06-09", "Deliberation Session"),
        ("20260609_143022_legacy_topic", "2026-06-09 14:30", "Legacy Topic"),
    ],
)
def test_parse_basename_formats(basename, expected_date, expected_title) -> None:
    date_display, title = parse_basename(basename)
    assert date_display == expected_date
    assert title == expected_title


@pytest.mark.parametrize(
    ("content", "expected"),
    [
        ("**Case No.**: 2026-CATC-001-001\n", "2026-CATC-001-001"),
        ("**Matter ID**: 2026-DEL-042\n", "2026-DEL-042"),
        ("No case header here\n", None),
    ],
)
def test_extract_case_number(content, expected) -> None:
    assert extract_case_number(content) == expected
