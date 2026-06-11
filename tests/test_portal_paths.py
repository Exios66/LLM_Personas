"""Regression tests for courtroom portal transcript path resolution."""

from pathlib import Path

import re

REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"
LAUNCH_SH = PORTAL_DIR / "launch.sh"
VIEWER_HTML = PORTAL_DIR / "viewer.html"


def test_launch_sh_transcripts_dir_resolves_to_courtroom_transcripts():
    """launch.sh must point at courtroom/transcripts, not courtroom/courtroom/transcripts."""
    content = LAUNCH_SH.read_text(encoding="utf-8")
    match = re.search(r'TRANSCRIPTS_DIR="\$PROJECT_ROOT/([^"]+)"', content)
    assert match is not None, "TRANSCRIPTS_DIR assignment not found in launch.sh"
    assert match.group(1) == "transcripts"
    assert TRANSCRIPTS_DIR.exists()


def test_viewer_html_transcripts_dir_resolves_to_courtroom_transcripts():
    """viewer.html fetch path must resolve to courtroom/transcripts from portal/."""
    content = VIEWER_HTML.read_text(encoding="utf-8")
    match = re.search(r"const TRANSCRIPTS_DIR = '([^']+)';", content)
    assert match is not None, "TRANSCRIPTS_DIR constant not found in viewer.html"
    assert match.group(1) == "../transcripts/"
    resolved = (PORTAL_DIR / match.group(1)).resolve()
    assert resolved == TRANSCRIPTS_DIR.resolve()
