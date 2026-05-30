"""Tests for litigation transcript save and case number allocation."""

from __future__ import annotations

from pathlib import Path

import pytest

from litigation import run as litigation_run


def test_allocate_case_number_increments_registry(tmp_path: Path) -> None:
    registry = tmp_path / "case-registry.yaml"
    registry.write_text(
        'year: 2026\nlast_updated: "2026-01-01"\n\ncategories:\n  DEL: 7\n',
        encoding="utf-8",
    )
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", registry)
    try:
        case_no = litigation_run._allocate_case_number("DEL")
        assert case_no == "2026-DEL-007-001"
        updated = registry.read_text(encoding="utf-8")
        assert "DEL: 8" in updated
    finally:
        monkeypatch.undo()


def test_save_transcript_unique_case_numbers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    registry = tmp_path / "courtroom" / "case-registry.yaml"
    registry.parent.mkdir(parents=True)
    registry.write_text(
        'year: 2026\nlast_updated: "2026-01-01"\n\ncategories:\n  DEL: 20\n',
        encoding="utf-8",
    )
    (tmp_path / "courtroom" / "transcripts").mkdir(parents=True)

    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", registry)
    monkeypatch.setattr(litigation_run, "REPO_ROOT", tmp_path)

    p1 = litigation_run.save_transcript("first matter", "deliberation one", location="courtroom")
    p2 = litigation_run.save_transcript("second matter", "deliberation two", location="courtroom")

    assert "2026-DEL-020-001" in p1.read_text(encoding="utf-8")
    assert "2026-DEL-021-001" in p2.read_text(encoding="utf-8")
    assert "DEL: 22" in registry.read_text(encoding="utf-8")
