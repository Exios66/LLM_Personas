"""Regression tests for courtroom portal generate.py path resolution."""

from __future__ import annotations

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GENERATE_SCRIPT = REPO_ROOT / "courtroom" / "portal" / "generate.py"


def _load_generate_module():
    spec = importlib.util.spec_from_file_location("portal_generate", GENERATE_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_generate_base_dir_is_courtroom():
    mod = _load_generate_module()
    expected = REPO_ROOT / "courtroom"
    assert mod.BASE_DIR == expected


def test_generate_transcript_index_uses_courtroom_transcripts():
    """generate.py must read courtroom/transcripts, not courtroom/courtroom/transcripts."""
    mod = _load_generate_module()
    transcripts_dir = mod.BASE_DIR / "transcripts"
    expected = REPO_ROOT / "courtroom" / "transcripts"
    assert transcripts_dir == expected
    assert "courtroom/courtroom" not in str(transcripts_dir)
    assert transcripts_dir.exists()
