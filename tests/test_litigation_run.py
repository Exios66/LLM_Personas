"""Regression tests for litigation runner transcript save and case numbering."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from litigation import run as litigation_run


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


def test_slugify_strips_special_chars_and_truncates() -> None:
    assert litigation_run.slugify("Hello, World!") == "hello-world"
    assert litigation_run.slugify("!!!") == "matter"
    assert len(litigation_run.slugify("a" * 100)) <= 60


def test_allocate_case_no_without_registry(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    missing = tmp_path / "missing-registry.yaml"
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", missing)

    case_no = litigation_run.allocate_case_no("DEL", deliberation=2)

    assert case_no.endswith("-DEL-001-002")
    assert case_no[:4].isdigit()


def test_save_transcript_courtroom_location(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    registry = tmp_path / "case-registry.yaml"
    registry.write_text(
        yaml.dump({"year": 2026, "categories": {"DEL": 1}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", registry)
    monkeypatch.setattr(litigation_run, "REPO_ROOT", tmp_path)

    courtroom_dir = tmp_path / "courtroom" / "transcripts"
    path = litigation_run.save_transcript("bench matter", "Ruling text.", location="courtroom")

    assert path.parent == courtroom_dir
    assert path.exists()
    assert "bench matter" in path.read_text(encoding="utf-8")


def test_save_transcript_appends_scribe_certification(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    registry = tmp_path / "case-registry.yaml"
    registry.write_text(
        yaml.dump({"year": 2026, "categories": {"DEL": 3}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", registry)

    fake_module = tmp_path / "litigation_pkg"
    fake_module.mkdir()
    (fake_module / "run.py").write_text("", encoding="utf-8")
    (fake_module / "transcripts").mkdir()
    monkeypatch.setattr(litigation_run, "__file__", str(fake_module / "run.py"))

    path = litigation_run.save_transcript("scribe test", "Body without footer.")
    content = path.read_text(encoding="utf-8")

    assert content.rstrip().endswith("> *Transcript certified by MORNINGSTAR::SCRIBE*")
    assert "Body without footer." in content
