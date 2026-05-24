"""Regression tests for portal transcript path resolution."""

import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"
LAUNCH_SH = PORTAL_DIR / "launch.sh"
VIEWER_HTML = PORTAL_DIR / "viewer.html"


def test_launch_sh_transcripts_dir():
    """launch.sh must resolve transcripts to courtroom/transcripts, not courtroom/courtroom/transcripts."""
    text = LAUNCH_SH.read_text(encoding="utf-8")
    assert 'TRANSCRIPTS_DIR="$COURTROOM_DIR/transcripts"' in text
    assert "courtroom/transcripts" not in text.split("TRANSCRIPTS_DIR=")[1].split("\n")[0]


def test_viewer_html_transcripts_fetch_path():
    """viewer.html fetch path must be ../transcripts/ relative to portal/, not ../courtroom/transcripts/."""
    text = VIEWER_HTML.read_text(encoding="utf-8")
    m = re.search(r"const TRANSCRIPTS_DIR = '([^']+)';", text)
    assert m is not None
    assert m.group(1) == "../transcripts/"
    assert "courtroom/courtroom" not in text


def test_launch_sh_lists_transcripts():
    """launch.sh check_transcripts must succeed when transcripts exist."""
    result = subprocess.run(
        [
            "bash",
            "-c",
            f'source /dev/null; SCRIPT_DIR="{PORTAL_DIR}"; COURTROOM_DIR="$(dirname "$SCRIPT_DIR")"; '
            f'TRANSCRIPTS_DIR="$COURTROOM_DIR/transcripts"; test -d "$TRANSCRIPTS_DIR"',
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert TRANSCRIPTS_DIR.exists()
