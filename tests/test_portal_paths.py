"""Regression tests for courtroom portal transcript path resolution."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"


def test_launch_sh_transcripts_dir_points_at_courtroom_transcripts() -> None:
    """launch.sh must not resolve to courtroom/courtroom/transcripts."""
    launch_sh = (PORTAL_DIR / "launch.sh").read_text(encoding="utf-8")
    assert 'TRANSCRIPTS_DIR="$COURTROOM_DIR/transcripts"' in launch_sh
    assert "courtroom/transcripts" not in launch_sh.split("TRANSCRIPTS_DIR=")[1].split("\n")[0]

    script_dir = PORTAL_DIR
    courtroom_dir = script_dir.parent
    resolved = courtroom_dir / "transcripts"
    assert resolved == TRANSCRIPTS_DIR
    assert resolved.exists()


def test_viewer_html_transcripts_dir_is_sibling_not_nested() -> None:
    """viewer.html is served from courtroom/portal/; transcripts live at ../transcripts/."""
    viewer = (PORTAL_DIR / "viewer.html").read_text(encoding="utf-8")
    assert "const TRANSCRIPTS_DIR = '../transcripts/';" in viewer
    assert "../courtroom/transcripts/" not in viewer

    resolved = (PORTAL_DIR / "../transcripts").resolve()
    assert resolved == TRANSCRIPTS_DIR
    assert resolved.exists()
