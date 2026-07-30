"""Regression tests for litigation runner transcript save and case numbering."""

from __future__ import annotations

import concurrent.futures
import datetime as dt_module
import re
from pathlib import Path

import pytest
import yaml

from litigation import run as litigation_run


def _patch_calendar_year(monkeypatch: pytest.MonkeyPatch, year: int) -> None:
    class FixedDatetime:
        @staticmethod
        def now(tz=None):
            return dt_module.datetime(year, 6, 14)

        @staticmethod
        def strftime(fmt: str) -> str:
            return dt_module.datetime(year, 6, 14).strftime(fmt)

    monkeypatch.setattr(litigation_run, "datetime", FixedDatetime)


def _case_no(content: str) -> str:
    match = re.search(r"\*\*Case No\.:\*\*\s*(.+)", content)
    assert match is not None, content
    return match.group(1).strip()


def test_allocate_case_no_creates_registry_when_missing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _patch_calendar_year(monkeypatch, 2026)
    registry = tmp_path / "case-registry.yaml"
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", registry)

    first = litigation_run.allocate_case_no("DEL")
    second = litigation_run.allocate_case_no("DEL")

    assert first == "2026-DEL-001-001"
    assert second == "2026-DEL-002-001"
    assert registry.exists()
    data = yaml.safe_load(registry.read_text(encoding="utf-8"))
    assert data["categories"]["DEL"] == 3


def test_allocate_case_no_resets_sequences_on_year_rollover(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _patch_calendar_year(monkeypatch, 2026)
    registry = tmp_path / "case-registry.yaml"
    registry.write_text(
        yaml.dump({"year": 2025, "categories": {"DEL": 9, "ARCH": 4}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", registry)

    case_no = litigation_run.allocate_case_no("DEL")

    assert case_no == "2026-DEL-001-001"
    data = yaml.safe_load(registry.read_text(encoding="utf-8"))
    assert data["year"] == 2026
    assert data["categories"]["DEL"] == 2
    assert data["categories"]["ARCH"] == 1


def test_allocate_case_no_increments_registry(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    registry = tmp_path / "case-registry.yaml"
    registry.write_text(
        yaml.dump({"year": 2026, "categories": {"DEL": 5}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", registry)

    first = litigation_run.allocate_case_no("DEL")
    second = litigation_run.allocate_case_no("DEL")

    assert first == "2026-DEL-005-001"
    assert second == "2026-DEL-006-001"
    data = yaml.safe_load(registry.read_text(encoding="utf-8"))
    assert data["categories"]["DEL"] == 7


def test_save_transcript_assigns_unique_case_numbers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    registry = tmp_path / "case-registry.yaml"
    registry.write_text(
        yaml.dump({"year": 2026, "categories": {"DEL": 12}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", registry)

    fake_module = tmp_path / "litigation_pkg"
    fake_module.mkdir()
    (fake_module / "run.py").write_text("", encoding="utf-8")
    (fake_module / "transcripts").mkdir()
    monkeypatch.setattr(litigation_run, "__file__", str(fake_module / "run.py"))

    path1 = litigation_run.save_transcript("first matter", "Deliberation one.")
    path2 = litigation_run.save_transcript("second matter", "Deliberation two.")

    assert "**Case No.:** 2026-DEL-012-001" in path1.read_text(encoding="utf-8")
    assert "**Case No.:** 2026-DEL-013-001" in path2.read_text(encoding="utf-8")


def test_save_transcript_filename_suffix_independent_of_case_no(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    registry = tmp_path / "case-registry.yaml"
    registry.write_text(
        yaml.dump({"year": 2026, "categories": {"DEL": 20}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", registry)

    fake_module = tmp_path / "litigation_pkg"
    fake_module.mkdir()
    (fake_module / "run.py").write_text("", encoding="utf-8")
    transcripts_dir = fake_module / "transcripts"
    transcripts_dir.mkdir()
    monkeypatch.setattr(litigation_run, "__file__", str(fake_module / "run.py"))

    today = litigation_run.datetime.now().strftime("%Y-%m-%d")
    slug = litigation_run.slugify("collision test")
    (transcripts_dir / f"{today}-{slug}.md").write_text("existing\n", encoding="utf-8")

    path = litigation_run.save_transcript("collision test", "New body.")
    content = path.read_text(encoding="utf-8")

    assert path.name.endswith("-1.md")
    assert "**Case No.:** 2026-DEL-020-001" in content


def test_allocate_case_no_concurrent_assignments_are_unique(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    registry = tmp_path / "case-registry.yaml"
    registry.write_text(
        yaml.dump({"year": 2026, "categories": {"DEL": 40}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", registry)

    fake_module = tmp_path / "litigation_pkg"
    fake_module.mkdir()
    (fake_module / "run.py").write_text("", encoding="utf-8")
    transcripts_dir = fake_module / "transcripts"
    transcripts_dir.mkdir()
    monkeypatch.setattr(litigation_run, "__file__", str(fake_module / "run.py"))

    def save_one(i: int) -> str:
        path = litigation_run.save_transcript(f"matter {i}", f"body {i}")
        return _case_no(path.read_text(encoding="utf-8"))

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        case_numbers = list(executor.map(save_one, range(8)))

    assert len(set(case_numbers)) == len(case_numbers)
    assert yaml.safe_load(registry.read_text(encoding="utf-8"))["categories"]["DEL"] == 48
