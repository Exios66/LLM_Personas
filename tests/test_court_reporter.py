"""Regression tests for courtroom transcript audit helpers (reporter.py)."""

from __future__ import annotations

from pathlib import Path

import pytest

from courtroom import reporter
from courtroom.reporter import (
    CERTIFICATION_MARKER,
    _extract_header_info,
    _skip_file,
    _suggest_canonical_name,
    audit_transcripts,
)


def test_skip_file_ignores_handoff_and_readme() -> None:
    assert _skip_file("README.md") is True
    assert _skip_file(".hidden.md") is True
    assert _skip_file("HANDOFF-session.md") is True
    assert _skip_file("2026-02-17-bench-trial.md") is False


def test_extract_header_info_case_no_and_date() -> None:
    content = (
        "**Case No.**: 2026-SECU-042-001\n"
        "**Date**: 2026-02-17\n"
    )
    info = _extract_header_info(content)
    assert info["case_no"] == "2026-SECU-042-001"
    assert info["date"] == "2026-02-17"
    assert info["uses_matter_id"] is False


def test_extract_header_info_matter_id_flagged() -> None:
    content = "**Matter ID**: 2026-LEGAL-001\n**Date**: 2026-01-15\n"
    info = _extract_header_info(content)
    assert info["case_no"] == "2026-LEGAL-001"
    assert info["uses_matter_id"] is True


def test_suggest_canonical_name_legacy_special_interest() -> None:
    path = Path("20260216_120000_bohemian_grove.md")
    content = "**Date**: 2026-02-16\n"
    suggested = _suggest_canonical_name(path, content)
    assert suggested == "20260216_120000_special_interest_bohemian-grove.md"


def test_suggest_canonical_name_none_when_already_canonical() -> None:
    path = Path("2026-02-17-bench-trial-topic.md")
    assert _suggest_canonical_name(path, "") is None
    path2 = Path("20260216_133000_special_interest_security.md")
    assert _suggest_canonical_name(path2, "") is None


def test_audit_transcripts_certified_and_header_flags(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(reporter, "REPO_ROOT", tmp_path)
    good = tmp_path / "2026-02-17-sample-matter.md"
    good.write_text(
        "**Case No.**: 2026-TEST-001\n"
        "**Date**: 2026-02-17\n"
        f"{CERTIFICATION_MARKER}\n",
        encoding="utf-8",
    )
    bad_header = tmp_path / "20260216_120000_legacy_topic.md"
    bad_header.write_text("No header fields.\n", encoding="utf-8")

    certified, uncertified = audit_transcripts(tmp_path)

    assert len(certified) == 1
    assert certified[0]["name"] == good.name
    assert certified[0]["header_ok"] is True
    assert certified[0]["canonical"] is True

    assert len(uncertified) == 1
    assert uncertified[0]["name"] == bad_header.name
    assert uncertified[0]["header_ok"] is False
    assert uncertified[0]["format_ok"] is True  # legacy pattern grandfathered
    assert uncertified[0]["rename_suggested"] is not None


def test_audit_transcripts_skips_handoff(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(reporter, "REPO_ROOT", tmp_path)
    handoff = tmp_path / "HANDOFF-notes.md"
    handoff.write_text("draft\n", encoding="utf-8")
    certified, uncertified = audit_transcripts(tmp_path)
    assert certified == []
    assert uncertified == []


def test_audit_transcripts_missing_dir(tmp_path: Path) -> None:
    missing = tmp_path / "nope"
    certified, uncertified = audit_transcripts(missing)
    assert certified == []
    assert uncertified == []
