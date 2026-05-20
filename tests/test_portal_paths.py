"""Portal path regression: viewer and launch script must not double-prefix courtroom/."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
VIEWER_HTML = PORTAL_DIR / "viewer.html"
LAUNCH_SH = PORTAL_DIR / "launch.sh"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"


def test_viewer_transcripts_dir_relative_path():
    """viewer.html lives in courtroom/portal/; transcripts are ../transcripts/."""
    content = VIEWER_HTML.read_text(encoding="utf-8")
    assert "const TRANSCRIPTS_DIR = '../transcripts/';" in content
    assert "../courtroom/transcripts/" not in content


def test_launch_sh_resolves_transcripts_dir():
    """launch.sh PROJECT_ROOT is courtroom/; transcripts are courtroom/transcripts/."""
    text = LAUNCH_SH.read_text(encoding="utf-8")
    assert 'TRANSCRIPTS_DIR="$PROJECT_ROOT/transcripts"' in text
    assert 'TRANSCRIPTS_DIR="$PROJECT_ROOT/courtroom/transcripts"' not in text

    # Mirror launch.sh path logic
    script_dir = PORTAL_DIR.resolve()
    project_root = script_dir.parent
    transcripts_dir = project_root / "transcripts"
    assert transcripts_dir == TRANSCRIPTS_DIR
    assert transcripts_dir.is_dir()
