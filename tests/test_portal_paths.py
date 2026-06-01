"""Regression tests for courtroom portal path resolution (viewer + launch.sh)."""

from pathlib import Path
import re

REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"


def test_launch_sh_transcripts_dir_resolves_to_courtroom_transcripts():
    """launch.sh must not resolve to courtroom/courtroom/transcripts."""
    script_dir = PORTAL_DIR
    project_root = script_dir.parent
    transcripts_dir = project_root / "transcripts"
    assert transcripts_dir == TRANSCRIPTS_DIR
    assert transcripts_dir.exists()


def test_viewer_html_transcripts_dir_relative_to_portal():
    """viewer.html fetch path must be ../transcripts/, not ../courtroom/transcripts/."""
    content = (PORTAL_DIR / "viewer.html").read_text(encoding="utf-8")
    match = re.search(
        r"const\s+TRANSCRIPTS_DIR\s*=\s*['\"]([^'\"]+)['\"]",
        content,
    )
    assert match is not None, "TRANSCRIPTS_DIR constant not found in viewer.html"
    assert match.group(1) == "../transcripts/"
    assert "courtroom/courtroom" not in match.group(1)
