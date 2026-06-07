"""Regression tests for courtroom portal path resolution."""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PORTAL_DIR = REPO_ROOT / "courtroom" / "portal"
TRANSCRIPTS_DIR = REPO_ROOT / "courtroom" / "transcripts"
SAMPLE_TRANSCRIPT = TRANSCRIPTS_DIR / "2026-02-15-framework-enhancement-analysis.md"
EXPORT_SCRIPT = PORTAL_DIR / "export_transcript.py"
LAUNCH_SCRIPT = PORTAL_DIR / "launch.sh"


def test_launch_script_resolves_transcripts_dir():
    """launch.sh must point at courtroom/transcripts, not courtroom/courtroom/transcripts."""
    script_dir = PORTAL_DIR
    courtroom_dir = script_dir.parent
    transcripts_dir = courtroom_dir / "transcripts"
    assert transcripts_dir == TRANSCRIPTS_DIR
    assert transcripts_dir.exists()


def test_launch_script_starts_without_path_error():
    result = subprocess.run(
        ["bash", str(LAUNCH_SCRIPT)],
        input="q\n",
        capture_output=True,
        text=True,
        cwd=str(PORTAL_DIR),
    )
    assert "courtroom/courtroom/transcripts" not in result.stdout + result.stderr
    assert "Transcripts directory not found" not in result.stdout + result.stderr


def test_export_transcript_accepts_repo_relative_path():
    assert SAMPLE_TRANSCRIPT.exists()
    out_path = PORTAL_DIR / "exports" / "_test_export_paths.html"
    try:
        result = subprocess.run(
            [
                sys.executable,
                str(EXPORT_SCRIPT),
                f"courtroom/transcripts/{SAMPLE_TRANSCRIPT.name}",
                "-o",
                str(out_path),
            ],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        )
        assert result.returncode == 0
        assert out_path.exists()
        assert out_path.stat().st_size > 0
    finally:
        out_path.unlink(missing_ok=True)


def test_export_transcript_accepts_courtroom_relative_path():
    assert SAMPLE_TRANSCRIPT.exists()
    out_path = PORTAL_DIR / "exports" / "_test_export_paths2.html"
    try:
        result = subprocess.run(
            [
                sys.executable,
                str(EXPORT_SCRIPT),
                f"transcripts/{SAMPLE_TRANSCRIPT.name}",
                "-o",
                str(out_path),
            ],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=True,
        )
        assert result.returncode == 0
        assert out_path.exists()
    finally:
        out_path.unlink(missing_ok=True)


def test_viewer_transcript_dir_is_sibling_of_portal():
    viewer = (PORTAL_DIR / "viewer.html").read_text(encoding="utf-8")
    assert "../courtroom/transcripts/" not in viewer
    assert "../transcripts/" in viewer
