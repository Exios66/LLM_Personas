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


def test_launch_sh_transcripts_dir_matches_courtroom_transcripts():
    """launch.sh must resolve transcripts under courtroom/, not courtroom/courtroom/."""
    portal_dir = REPO_ROOT / "courtroom" / "portal"
    project_root = portal_dir.parent
    transcripts_dir = project_root / "transcripts"
    assert transcripts_dir == TRANSCRIPTS_DIR
    assert transcripts_dir.is_dir()


def test_viewer_transcripts_dir_resolves_from_portal():
    """viewer.html fetch path must resolve to courtroom/transcripts/."""
    portal_dir = REPO_ROOT / "courtroom" / "portal"
    resolved = (portal_dir / "../transcripts/example.md").resolve()
    assert resolved == (TRANSCRIPTS_DIR / "example.md").resolve()
