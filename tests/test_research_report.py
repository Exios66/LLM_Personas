"""Regression tests for research report workflow helpers."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from agents.workflows import research_report


def test_generate_report_id_format() -> None:
    report_id = research_report._generate_report_id()
    assert re.fullmatch(r"RPT_[A-Z0-9]{8}", report_id)


def test_ensure_html_wrapped_wraps_plain_text() -> None:
    wrapped = research_report._ensure_html_wrapped("Plain report text")
    assert wrapped.startswith("<div")
    assert "Plain report text" in wrapped


def test_ensure_html_wrapped_adds_style_div_for_fragment() -> None:
    wrapped = research_report._ensure_html_wrapped("<h2>Title</h2><p>Body</p>")
    assert "font-family" in wrapped
    assert "<h2>Title</h2>" in wrapped


def test_ensure_html_wrapped_leaves_full_document_unchanged() -> None:
    html = "<html><body><p>Full doc</p></body></html>"
    assert research_report._ensure_html_wrapped(html) == html


def test_save_report_writes_header_and_html(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    reports_dir = tmp_path / "reports"
    monkeypatch.setattr(research_report, "REPORTS_DIR", reports_dir)

    path = research_report.save_report("RPT_ABCD1234", "20260701_120000", "<p>HTML</p>", "Topic")

    content = path.read_text(encoding="utf-8")
    assert path.name == "RPT_ABCD1234_20260701_120000.html"
    assert "<!-- Report ID: RPT_ABCD1234" in content
    assert "<p>HTML</p>" in content
