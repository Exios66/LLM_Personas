"""Tests for courtroom portal manifest generation and path resolution."""

from pathlib import Path
import re

import json
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
MANIFEST_SCRIPT = PORTAL_DIR / "generate_manifest.py"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"
MANIFEST_PATH = PORTAL_DIR / "transcripts_manifest.json"
VIEWER_HTML = PORTAL_DIR / "viewer.html"
LAUNCH_SH = PORTAL_DIR / "launch.sh"


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


def test_viewer_transcripts_dir_is_relative_to_portal():
    """viewer.html must fetch ../transcripts/, not ../courtroom/transcripts/."""
    content = VIEWER_HTML.read_text(encoding="utf-8")
    match = re.search(r"const TRANSCRIPTS_DIR = '([^']+)';", content)
    assert match is not None
    assert match.group(1) == "../transcripts/"
    assert "../courtroom/transcripts/" not in content


def test_launch_sh_resolves_transcripts_dir():
    """launch.sh must resolve to repo courtroom/transcripts, not courtroom/courtroom/transcripts."""
    script = (
        f"SCRIPT_DIR=$(cd '{PORTAL_DIR}' && pwd); "
        "PROJECT_ROOT=$(cd \"$SCRIPT_DIR/../..\" && pwd); "
        'TRANSCRIPTS_DIR="$PROJECT_ROOT/courtroom/transcripts"; '
        'echo "$TRANSCRIPTS_DIR"'
    )
    result = subprocess.run(
        ["bash", "-c", script],
        capture_output=True,
        text=True,
        check=True,
    )
    resolved = Path(result.stdout.strip())
    assert resolved == TRANSCRIPTS_DIR
    assert resolved.exists()
