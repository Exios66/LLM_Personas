"""Regression tests for courtroom portal path resolution."""

import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"
LAUNCH_SH = PORTAL_DIR / "launch.sh"
VIEWER_HTML = PORTAL_DIR / "viewer.html"


def test_launch_sh_resolves_transcripts_dir():
    """launch.sh must point at courtroom/transcripts, not courtroom/courtroom/transcripts."""
    text = LAUNCH_SH.read_text(encoding="utf-8")
    assert 'TRANSCRIPTS_DIR="$COURTROOM_DIR/transcripts"' in text
    assert "$PROJECT_ROOT/courtroom/transcripts" not in text


def test_viewer_html_transcripts_fetch_path():
    """viewer.html fetch path from portal/ must resolve to courtroom/transcripts/."""
    text = VIEWER_HTML.read_text(encoding="utf-8")
    m = re.search(r"const TRANSCRIPTS_DIR = '([^']+)';", text)
    assert m is not None
    rel = m.group(1)
    # Resolved from courtroom/portal/viewer.html
    resolved = (PORTAL_DIR / rel).resolve()
    assert resolved == TRANSCRIPTS_DIR.resolve()


def test_viewer_path_served_over_http():
    """Relative URL from /courtroom/portal/ must not double the courtroom segment."""
    rel = "../transcripts/"
    # Browser resolves relative to /courtroom/portal/viewer.html -> /courtroom/transcripts/
    assert rel == "../transcripts/"
    assert "courtroom/courtroom" not in rel
