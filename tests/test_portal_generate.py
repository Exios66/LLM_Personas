"""Tests for portal generate.py output path safety."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GENERATE = REPO_ROOT / "courtroom" / "portal" / "generate.py"


def test_validate_output_path_refuses_transcript_directory(tmp_path: Path) -> None:
    transcripts = tmp_path / "transcripts"
    transcripts.mkdir()
    (transcripts / "2026-05-30-example.md").write_text("# test\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(GENERATE),
            "--output",
            str(transcripts),
            "--force",
            "--skip-gitmal",
        ],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "Refusing to delete" in result.stderr
