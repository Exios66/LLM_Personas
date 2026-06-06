"""Regression tests for courtroom portal transcript HTML export."""

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


def test_md_to_html_fenced_code_escapes_html():
    mod = _load_export_module()
    html = mod.md_to_html("```\n<script>alert(1)</script>\n```")
    assert "<script>" not in html
    assert "&lt;script&gt;" in html


def test_md_to_html_headers_and_bold():
    mod = _load_export_module()
    html = mod.md_to_html("# Title\n\n**bold** text")
    assert "<h1>Title</h1>" in html
    assert "<strong>bold</strong>" in html


def test_md_to_html_table_skips_separator_row():
    mod = _load_export_module()
    md = "| A | B |\n| --- | --- |\n| one | two |"
    html = mod.md_to_html(md)
    assert "<table>" in html
    assert "<td>one</td>" in html
    assert "<td>two</td>" in html
    assert "---" not in html


def test_apply_personality_styling_wraps_votes():
    mod = _load_export_module()
    html = mod.apply_personality_styling("<p>MORNINGSTAR votes YES</p>")
    assert 'class="p-morningstar"' in html
    assert 'class="vote-yes"' in html


def test_extract_title_from_h1():
    mod = _load_export_module()
    path = Path("2026-02-15-framework-enhancement-analysis.md")
    content = "# Framework Enhancement Analysis\n\nBody."
    assert mod.extract_title(path, content) == "Framework Enhancement Analysis"


def test_extract_title_from_legacy_timestamp_stem():
    mod = _load_export_module()
    path = Path("20260216_120000_special_inquiry_bohemian_grove.md")
    assert mod.extract_title(path, "") == "Special Inquiry Bohemian Grove"


def test_extract_title_from_dated_stem():
    mod = _load_export_module()
    path = Path("2026-02-15-contempt-hearing-xenon.md")
    assert mod.extract_title(path, "") == "Contempt Hearing Xenon"
