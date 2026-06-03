"""Regression tests for courtroom portal transcript path resolution."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"
VIEWER_HTML = PORTAL_DIR / "viewer.html"
LAUNCH_SH = PORTAL_DIR / "launch.sh"


def test_viewer_transcripts_dir_points_at_courtroom_transcripts():
    """viewer.html is served from courtroom/portal/; fetches must use ../transcripts/."""
    content = VIEWER_HTML.read_text(encoding="utf-8")
    assert "../courtroom/transcripts/" not in content
    assert "../transcripts/" in content


def test_launch_sh_transcripts_dir_resolves_to_courtroom_transcripts():
    """launch.sh must list courtroom/transcripts, not courtroom/courtroom/transcripts."""
    content = LAUNCH_SH.read_text(encoding="utf-8")
    assert 'courtroom/transcripts"' not in content or "COURTROOM_DIR/transcripts" in content
    assert "$COURTROOM_DIR/transcripts" in content
    assert (PORTAL_DIR.parent / "transcripts") == TRANSCRIPTS_DIR
    assert TRANSCRIPTS_DIR.exists()
