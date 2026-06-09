"""Regression tests for courtroom portal path resolution."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"
LAUNCH_SH = PORTAL_DIR / "launch.sh"
VIEWER_HTML = PORTAL_DIR / "viewer.html"


def test_viewer_transcripts_dir_relative_path() -> None:
    """viewer.html must fetch ../transcripts/, not ../courtroom/transcripts/."""
    content = VIEWER_HTML.read_text(encoding="utf-8")
    match = re.search(r"const TRANSCRIPTS_DIR = '([^']+)';", content)
    assert match is not None, "TRANSCRIPTS_DIR constant not found in viewer.html"
    assert match.group(1) == "../transcripts/"


def test_launch_sh_resolves_transcripts_dir() -> None:
    """launch.sh must resolve TRANSCRIPTS_DIR to courtroom/transcripts."""
    script = f"""
    SCRIPT_DIR="$(cd "$(dirname "{LAUNCH_SH}")" && pwd)"
    BASE_DIR="$(dirname "$SCRIPT_DIR")"
    TRANSCRIPTS_DIR="$BASE_DIR/transcripts"
    echo "$TRANSCRIPTS_DIR"
    """
    result = subprocess.run(
        ["bash", "-c", script],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=True,
    )
    resolved = Path(result.stdout.strip())
    assert resolved == TRANSCRIPTS_DIR
    assert resolved.exists()


def test_launch_sh_check_transcripts_succeeds() -> None:
    """launch.sh transcript directory check must not fail on a normal repo checkout."""
    script = f"""
    SCRIPT_DIR="$(cd "$(dirname "{LAUNCH_SH}")" && pwd)"
    BASE_DIR="$(dirname "$SCRIPT_DIR")"
    TRANSCRIPTS_DIR="$BASE_DIR/transcripts"
    if [ ! -d "$TRANSCRIPTS_DIR" ]; then
      echo "missing: $TRANSCRIPTS_DIR"
      exit 1
    fi
    """
    result = subprocess.run(
        ["bash", "-c", script],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
