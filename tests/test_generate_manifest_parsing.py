"""Unit tests for courtroom portal manifest basename and case-number parsing."""

from __future__ import annotations

from courtroom.portal.generate_manifest import extract_case_number, parse_basename


def test_parse_basename_iso_date_slug() -> None:
    date_display, title = parse_basename("2026-02-17-bench-trial")
    assert date_display == "2026-02-17"
    assert title == "Bench Trial"


def test_parse_basename_legacy_timestamp_slug() -> None:
    date_display, title = parse_basename("20260216_133000_special_interest_security")
    assert date_display == "2026-02-16 13:30"
    assert title == "Special Interest Security"


def test_parse_basename_unknown_format_fallback() -> None:
    date_display, title = parse_basename("adhoc_notes")
    assert date_display == "Unknown"
    assert title == "Adhoc Notes"


def test_extract_case_number_prefers_case_no() -> None:
    content = "**Case No.**: 2026-SECU-042-001\n**Matter ID**: 2026-LEGAL-001\n"
    assert extract_case_number(content) == "2026-SECU-042-001"


def test_extract_case_number_matter_id_legacy() -> None:
    content = "**Matter ID**: 2026-LEGAL-001\n"
    assert extract_case_number(content) == "2026-LEGAL-001"


def test_extract_case_number_missing_returns_none() -> None:
    assert extract_case_number("No case header here.") is None
