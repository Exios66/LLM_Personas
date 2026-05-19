"""Regression tests for Court Reporter transcript audit and naming (core/case-format.md)."""

from __future__ import annotations

from pathlib import Path

import pytest

CERT = "Transcript certified by MORNINGSTAR::SCRIBE"


def _write(path: Path, body: str, *, certified: bool = False) -> None:
    text = body
    if certified:
        text = f"{body.rstrip()}\n\n{CERT}\n"
    path.write_text(text, encoding="utf-8")


def test_skip_file_ignores_handoff_and_readme(court_reporter) -> None:
    assert court_reporter._skip_file("HANDOFF-2026-DEL-001.md") is True
    assert court_reporter._skip_file("README.md") is True
    assert court_reporter._skip_file(".hidden.md") is True
    assert court_reporter._skip_file("2026-02-19-matter.md") is False


def test_extract_header_info_prefers_case_no_over_matter_id(court_reporter) -> None:
    content = (
        "**Case No.**: 2026-DEL-004-001\n"
        "**Date**: 2026-02-19\n"
    )
    info = court_reporter._extract_header_info(content)
    assert info["case_no"] == "2026-DEL-004-001"
    assert info["date"] == "2026-02-19"
    assert info["uses_matter_id"] is False


def test_extract_header_info_accepts_matter_id_legacy(court_reporter) -> None:
    content = "**Matter ID**: 2026-CONT-001-001\n**Date**: 2026-02-16\n"
    info = court_reporter._extract_header_info(content)
    assert info["case_no"] == "2026-CONT-001-001"
    assert info["uses_matter_id"] is True


def test_suggest_canonical_name_legacy_special_interest(court_reporter) -> None:
    path = Path("20260216_120000_internal_security.md")
    content = "**Date**: 2026-02-16\n"
    suggested = court_reporter._suggest_canonical_name(path, content)
    assert suggested == "20260216_120000_special_interest_internal-security.md"


def test_suggest_canonical_name_none_for_standard_stem(court_reporter) -> None:
    path = Path("2026-02-19-case-naming-and-numbering.md")
    content = "**Case No.**: 2026-DEL-004-001\n**Date**: 2026-02-19\n"
    assert court_reporter._suggest_canonical_name(path, content) is None


def test_audit_transcripts_certified_and_header_flags(
    tmp_path: Path, court_reporter, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(court_reporter, "REPO_ROOT", tmp_path)
    d = tmp_path / "transcripts"
    d.mkdir()
    _write(
        d / "2026-02-19-valid-matter.md",
        "**Case No.**: 2026-DEL-001-001\n**Date**: 2026-02-19\n",
        certified=True,
    )
    _write(
        d / "draft-matter.md",
        "**Case No.**: 2026-DEL-002-001\n**Date**: 2026-02-20\n",
        certified=False,
    )
    _write(d / "no-header.md", "# Notes only\n", certified=False)

    certified, uncertified = court_reporter.audit_transcripts(d)
    assert len(certified) == 1
    assert certified[0]["name"] == "2026-02-19-valid-matter.md"
    assert certified[0]["header_ok"] is True
    assert certified[0]["canonical"] is True

    assert len(uncertified) == 2
    by_name = {e["name"]: e for e in uncertified}
    assert by_name["draft-matter.md"]["header_ok"] is True
    assert by_name["draft-matter.md"]["certified"] is False
    assert by_name["no-header.md"]["header_ok"] is False


def test_do_renames_skips_certified_even_with_suggestion(
    tmp_path: Path, court_reporter, monkeypatch: pytest.MonkeyPatch
) -> None:
    d = tmp_path / "t"
    d.mkdir()
    legacy = d / "20260216_120000_topic.md"
    _write(legacy, "**Date**: 2026-02-16\n", certified=True)
    suggestion = court_reporter._suggest_canonical_name(legacy, legacy.read_text(encoding="utf-8"))
    assert suggestion is not None

    entry = {
        "certified": True,
        "rename_suggested": suggestion,
        "path_obj": legacy,
    }
    renamed = court_reporter._do_renames([entry], non_interactive=True)
    assert renamed == 0
    assert legacy.exists()
