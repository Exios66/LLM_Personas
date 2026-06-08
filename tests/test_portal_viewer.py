"""Regression tests for portal viewer static assets."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VIEWER_HTML = REPO_ROOT / "courtroom" / "portal" / "viewer.html"
LAUNCH_SH = REPO_ROOT / "courtroom" / "portal" / "launch.sh"


def test_viewer_transcripts_dir_resolves_from_portal() -> None:
    """viewer.html is under courtroom/portal/; transcripts are courtroom/transcripts/."""
    content = VIEWER_HTML.read_text(encoding="utf-8")
    assert "const TRANSCRIPTS_DIR = '../transcripts/';" in content
    assert "../courtroom/transcripts" not in content


def test_launch_sh_transcripts_dir_resolves_from_portal() -> None:
    """launch.sh PROJECT_ROOT is courtroom/; transcripts are courtroom/transcripts/."""
    content = LAUNCH_SH.read_text(encoding="utf-8")
    assert 'TRANSCRIPTS_DIR="$PROJECT_ROOT/transcripts"' in content
    assert 'TRANSCRIPTS_DIR="$PROJECT_ROOT/courtroom/transcripts"' not in content
