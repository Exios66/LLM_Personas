"""Unit tests for courtroom portal manifest basename and case-number parsing."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "courtroom" / "portal"))

from generate_manifest import extract_case_number, parse_basename  # noqa: E402


def test_parse_basename_iso_date_topic() -> None:
    date_display, title = parse_basename("2026-02-17-bench-trial-topic")
    assert date_display == "2026-02-17"
    assert title == "Bench Trial Topic"


def test_parse_basename_legacy_timestamp() -> None:
    date_display, title = parse_basename("20260216_133000_special_interest_security")
    assert date_display == "2026-02-16 13:30"
    assert title == "Special Interest Security"


def test_parse_basename_unknown_fallback() -> None:
    date_display, title = parse_basename("adhoc_notes")
    assert date_display == "Unknown"
    assert "Adhoc" in title or "adhoc" in title.lower()


def test_extract_case_number_prefers_case_no() -> None:
    content = "**Case No.**: 2026-SECU-042-001\n**Matter ID**: 2026-LEGAL-001\n"
    assert extract_case_number(content) == "2026-SECU-042-001"


def test_extract_case_number_legacy_matter_id() -> None:
    content = "**Matter ID**: 2026-DELIB-007\n"
    assert extract_case_number(content) == "2026-DELIB-007"


def test_extract_case_number_missing() -> None:
    assert extract_case_number("No structured header.\n") is None
