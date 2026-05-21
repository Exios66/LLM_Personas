"""Regression tests for courtroom portal transcript path resolution."""

from pathlib import Path

import subprocess


REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
VIEWER_HTML = PORTAL_DIR / "viewer.html"
LAUNCH_SH = PORTAL_DIR / "launch.sh"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"


def test_viewer_transcripts_dir_relative_path():
    """viewer.html is under courtroom/portal/; transcripts are ../transcripts/."""
    content = VIEWER_HTML.read_text(encoding="utf-8")
    assert "../courtroom/transcripts/" not in content
    assert "const TRANSCRIPTS_DIR = '../transcripts/';" in content


def test_launch_sh_resolves_transcripts_dir():
    """launch.sh must point at courtroom/transcripts, not courtroom/courtroom/transcripts."""
    script = LAUNCH_SH.read_text(encoding="utf-8")
    assert 'TRANSCRIPTS_DIR="$COURTROOM_DIR/transcripts"' in script
    assert "$PROJECT_ROOT/courtroom/transcripts" not in script

    result = subprocess.run(
        [
            "bash",
            "-c",
            'SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"; '
            'COURTROOM_DIR="$(dirname "$SCRIPT_DIR")"; '
            'echo "$COURTROOM_DIR/transcripts"',
        ],
        capture_output=True,
        text=True,
        cwd=str(PORTAL_DIR),
        check=True,
    )
    resolved = Path(result.stdout.strip())
    assert resolved == TRANSCRIPTS_DIR
    assert resolved.exists()


def test_launch_sh_check_transcripts_succeeds():
    """Simulate check_transcripts guard used by launch.sh."""
    result = subprocess.run(
        [
            "bash",
            "-c",
            'SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"; '
            'COURTROOM_DIR="$(dirname "$SCRIPT_DIR")"; '
            'TRANSCRIPTS_DIR="$COURTROOM_DIR/transcripts"; '
            'test -d "$TRANSCRIPTS_DIR"',
        ],
        cwd=str(PORTAL_DIR),
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr.decode()
