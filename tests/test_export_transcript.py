"""Regression tests for portal transcript markdown → HTML export."""

from __future__ import annotations

from pathlib import Path

from courtroom.portal.export_transcript import (
    apply_personality_styling,
    extract_title,
    md_to_html,
)


def test_md_to_html_escapes_angle_brackets_in_code_blocks() -> None:
    md = "```\nif x < 1 and y > 0:\n    pass\n```"
    html = md_to_html(md)
    assert "&lt;" in html
    assert "<pre><code>" in html
    assert "if x &lt; 1" in html


def test_md_to_html_renders_table_skipping_separator_row() -> None:
    md = "| A | B |\n| --- | --- |\n| 1 | 2 |"
    html = md_to_html(md)
    assert "<table>" in html
    assert "<td>1</td>" in html
    assert "<td>2</td>" in html
    assert "---" not in html


def test_apply_personality_styling_wraps_votes() -> None:
    html = apply_personality_styling("Vote: YES or NO or ABSTAIN")
    assert 'class="vote-yes"' in html
    assert 'class="vote-no"' in html
    assert 'class="vote-abstain"' in html


def test_extract_title_from_first_h1() -> None:
    content = "# Framework Enhancement\n\nBody."
    title = extract_title(
        Path("2026-02-15-framework-enhancement-analysis.md"),
        content,
    )
    assert title == "Framework Enhancement"
