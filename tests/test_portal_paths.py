"""Regression tests for consistent courtroom portal transcript paths."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"


def test_launch_sh_resolves_transcripts_to_courtroom_transcripts() -> None:
    launch = (PORTAL_DIR / "launch.sh").read_text(encoding="utf-8")
    assert 'TRANSCRIPTS_DIR="$COURTROOM_DIR/transcripts"' in launch
    assert "courtroom/courtroom/transcripts" not in launch


def test_viewer_html_fetches_from_sibling_transcripts_dir() -> None:
    viewer = (PORTAL_DIR / "viewer.html").read_text(encoding="utf-8")
    assert "const TRANSCRIPTS_DIR = '../transcripts/';" in viewer
    assert "../courtroom/transcripts/" not in viewer


def test_transcripts_dir_exists() -> None:
    assert TRANSCRIPTS_DIR.exists()
