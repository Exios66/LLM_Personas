"""Regression tests for portal transcript path resolution."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"


def test_viewer_transcripts_dir_resolves_to_courtroom_transcripts():
    """viewer.html must fetch ../transcripts/, not ../courtroom/transcripts/."""
    viewer = (PORTAL_DIR / "viewer.html").read_text(encoding="utf-8")
    assert "const TRANSCRIPTS_DIR = '../transcripts/';" in viewer
    assert "../courtroom/transcripts/" not in viewer

    resolved = (PORTAL_DIR / "../transcripts").resolve()
    assert resolved == TRANSCRIPTS_DIR
    assert resolved.exists()


def test_launch_sh_transcripts_dir_resolves_to_courtroom_transcripts():
    """launch.sh must list courtroom/transcripts, not courtroom/courtroom/transcripts."""
    launch = (PORTAL_DIR / "launch.sh").read_text(encoding="utf-8")
    assert 'TRANSCRIPTS_DIR="$SCRIPT_DIR/../transcripts"' in launch
    assert 'TRANSCRIPTS_DIR="$PROJECT_ROOT/courtroom/transcripts"' not in launch

    resolved = (PORTAL_DIR / "../transcripts").resolve()
    assert resolved == TRANSCRIPTS_DIR
    assert resolved.exists()
