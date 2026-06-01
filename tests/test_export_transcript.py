"""Regression tests for portal transcript markdown-to-HTML export."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
_EXPORT_SCRIPT = REPO_ROOT / "courtroom" / "portal" / "export_transcript.py"


def _load_export_module():
    name = "courtroom_portal_export_transcript"
    spec = importlib.util.spec_from_file_location(name, _EXPORT_SCRIPT)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def export_mod():
    return _load_export_module()


def test_md_to_html_escapes_angle_brackets_in_code_blocks(export_mod) -> None:
    md = "```\nif a < b:\n    pass\n```"
    html = export_mod.md_to_html(md)
    assert "&lt;" in html
    assert "<pre><code>" in html


def test_md_to_html_table_skips_separator_row(export_mod) -> None:
    md = "| A | B |\n| --- | --- |\n| 1 | 2 |"
    html = export_mod.md_to_html(md)
    assert "<table>" in html
    assert "1" in html and "2" in html
    assert html.count("<tr>") == 2


def test_extract_title_from_first_h1(export_mod) -> None:
    content = "# Bench Trial Summary\n\nBody."
    title = export_mod.extract_title(Path("anything.md"), content)
    assert title == "Bench Trial Summary"


def test_extract_title_from_dated_filename(export_mod) -> None:
    title = export_mod.extract_title(
        Path("2026-02-15-framework-enhancement-analysis.md"), ""
    )
    assert title == "Framework Enhancement Analysis"


def test_apply_personality_styling_wraps_votes(export_mod) -> None:
    html = export_mod.apply_personality_styling("Vote: YES and NO")
    assert 'class="vote-yes"' in html
    assert 'class="vote-no"' in html


def test_main_rejects_non_md(tmp_path: Path, export_mod, monkeypatch) -> None:
    bad = tmp_path / "notes.txt"
    bad.write_text("x", encoding="utf-8")
    monkeypatch.setattr(
        sys,
        "argv",
        ["export_transcript.py", str(bad)],
    )
    assert export_mod.main() == 1
