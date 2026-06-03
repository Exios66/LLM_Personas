"""Regression tests for Court Reporter transcript audit and naming (core/case-format.md)."""

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


def test_regenerate_manifest_uses_courtroom_portal_script(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Manifest path must stay under courtroom/portal/, not courtroom/courtroom/."""
    portal = tmp_path / "courtroom" / "portal"
    portal.mkdir(parents=True)
    script = portal / "generate_manifest.py"
    script.write_text("#!/usr/bin/env python3\n", encoding="utf-8")
    monkeypatch.setattr(reporter, "REPO_ROOT", tmp_path)

    assert reporter.regenerate_manifest() is True


def test_regenerate_manifest_false_when_script_missing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(reporter, "REPO_ROOT", tmp_path)
    assert reporter.regenerate_manifest() is False


def test_do_renames_skips_certified_even_with_suggestion(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    d = tmp_path / "t"
    d.mkdir()
    legacy = d / "20260216_120000_topic.md"
    legacy.write_text(
        f"**Date**: 2026-02-16\n\n{CERTIFICATION_MARKER}\n",
        encoding="utf-8",
    )
    suggestion = _suggest_canonical_name(legacy, legacy.read_text(encoding="utf-8"))
    assert suggestion is not None

    entry = {
        "certified": True,
        "rename_suggested": suggestion,
        "path_obj": legacy,
    }
    renamed = reporter._do_renames([entry], non_interactive=True)
    assert renamed == 0
    assert legacy.exists()
