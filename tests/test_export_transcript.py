"""Regression tests for courtroom portal transcript export paths and parsing."""

from __future__ import annotations

import importlib.util
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPORT_SCRIPT = REPO_ROOT / "courtroom" / "portal" / "export_transcript.py"


def _load_export_module():
    spec = importlib.util.spec_from_file_location("export_transcript", EXPORT_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_transcripts_dir_resolves_to_courtroom_transcripts():
    """Export script must read courtroom/transcripts, not courtroom/courtroom/transcripts."""
    mod = _load_export_module()
    expected = REPO_ROOT / "courtroom" / "transcripts"
    assert mod.TRANSCRIPTS_DIR == expected
    assert mod.TRANSCRIPTS_DIR.exists()


def test_extract_title_from_h1():
    mod = _load_export_module()
    path = Path("2026-02-15-framework-enhancement-analysis.md")
    content = "# Framework Enhancement Analysis\n\nBody."
    assert mod.extract_title(path, content) == "Framework Enhancement Analysis"


def test_extract_title_from_dated_filename():
    mod = _load_export_module()
    path = Path("2026-02-15-framework-enhancement-analysis.md")
    assert mod.extract_title(path, "") == "Framework Enhancement Analysis"
