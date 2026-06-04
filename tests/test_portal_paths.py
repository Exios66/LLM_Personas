"""Regression tests for courtroom portal path resolution."""

import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LAUNCH_SH = REPO_ROOT / "courtroom" / "portal" / "launch.sh"
VIEWER_HTML = REPO_ROOT / "courtroom" / "portal" / "viewer.html"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"


def test_launch_sh_resolves_transcripts_dir():
    """launch.sh must find courtroom/transcripts, not courtroom/courtroom/transcripts."""
    script = LAUNCH_SH.read_text(encoding="utf-8")
    assert 'TRANSCRIPTS_DIR="$COURTROOM_DIR/transcripts"' in script
    assert 'courtroom/transcripts"' not in script or "COURTROOM_DIR/transcripts" in script

    # Simulate launch.sh path resolution (bash)
    result = subprocess.run(
        [
            "bash",
            "-c",
            f'SCRIPT_DIR="$(cd "$(dirname "{LAUNCH_SH}")" && pwd)"; '
            'COURTROOM_DIR="$(dirname "$SCRIPT_DIR")"; '
            'TRANSCRIPTS_DIR="$COURTROOM_DIR/transcripts"; '
            'echo "$TRANSCRIPTS_DIR"',
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    resolved = Path(result.stdout.strip())
    assert resolved == TRANSCRIPTS_DIR.resolve()
    assert resolved.is_dir()


def test_viewer_html_transcripts_dir_relative_path():
    """viewer.html fetch path must resolve to courtroom/transcripts from portal/."""
    html = VIEWER_HTML.read_text(encoding="utf-8")
    match = re.search(r"const TRANSCRIPTS_DIR = '([^']+)';", html)
    assert match is not None
    rel = match.group(1)
    assert rel == "../transcripts/"
    assert "courtroom/transcripts" not in rel

    portal_dir = VIEWER_HTML.parent
    resolved = (portal_dir / rel).resolve()
    assert resolved == TRANSCRIPTS_DIR.resolve()
