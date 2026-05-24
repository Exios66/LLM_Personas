"""Unit tests for portal manifest basename and case-number parsing."""

from __future__ import annotations

from courtroom.portal.generate_manifest import extract_case_number, parse_basename


def test_parse_basename_iso_date_topic() -> None:
    date_display, title = parse_basename("2026-02-17-bench-trial")
    assert date_display == "2026-02-17"
    assert title == "Bench Trial"


def test_parse_basename_legacy_timestamp() -> None:
    date_display, title = parse_basename("20260216_120000_special_interest_topic")
    assert date_display == "2026-02-16 12:00"
    assert title == "Special Interest Topic"


def test_parse_basename_unknown_fallback() -> None:
    date_display, title = parse_basename("adhoc_notes")
    assert date_display == "Unknown"
    assert title == "Adhoc Notes"


def test_extract_case_number_prefers_case_no() -> None:
    content = "**Case No.**: 2026-SECU-042-001\n**Matter ID**: 2026-OLD-001\n"
    assert extract_case_number(content) == "2026-SECU-042-001"


def test_extract_case_number_matter_id_fallback() -> None:
    content = "**Matter ID**: 2026-LEGAL-001\n"
    assert extract_case_number(content) == "2026-LEGAL-001"


def test_extract_case_number_missing() -> None:
    assert extract_case_number("No header fields here.\n") is None
