"""Tests for courtroom portal manifest generation."""

from pathlib import Path

import json
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_SCRIPT = REPO_ROOT / "courtroom" / "portal" / "generate_manifest.py"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"
MANIFEST_PATH = REPO_ROOT / "courtroom" / "portal" / "transcripts_manifest.json"


def test_transcripts_dir_resolves_to_courtroom_transcripts():
    """Manifest generator must read courtroom/transcripts, not courtroom/courtroom/transcripts."""
    # Mirror path logic in generate_manifest.py
    script_dir = MANIFEST_SCRIPT.parent
    base_dir = script_dir.parent
    transcripts_dir = base_dir / "transcripts"
    assert transcripts_dir == TRANSCRIPTS_DIR
    assert transcripts_dir.exists()


def test_generate_manifest_includes_transcripts():
    result = subprocess.run(
        [sys.executable, str(MANIFEST_SCRIPT)],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    md_count = len(
        [
            p
            for p in TRANSCRIPTS_DIR.glob("*.md")
            if not p.name.startswith(".")
            and p.name != "README.md"
            and not p.name.upper().startswith("HANDOFF")
        ]
    )
    assert len(manifest["transcripts"]) == md_count
    assert manifest["transcripts"], "expected at least one transcript in manifest"


def test_launch_sh_transcripts_dir():
    """launch.sh PROJECT_ROOT is courtroom/; transcripts must be courtroom/transcripts."""
    launch_sh = REPO_ROOT / "courtroom" / "portal" / "launch.sh"
    content = launch_sh.read_text(encoding="utf-8")
    assert 'TRANSCRIPTS_DIR="$PROJECT_ROOT/transcripts"' in content
    assert 'TRANSCRIPTS_DIR="$PROJECT_ROOT/courtroom/transcripts"' not in content


def test_viewer_html_transcripts_dir():
    """viewer.html is under courtroom/portal/; fetch path must be ../transcripts/."""
    viewer = REPO_ROOT / "courtroom" / "portal" / "viewer.html"
    content = viewer.read_text(encoding="utf-8")
    assert "const TRANSCRIPTS_DIR = '../transcripts/';" in content
    assert "../courtroom/transcripts/" not in content
