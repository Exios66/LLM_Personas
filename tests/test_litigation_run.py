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


def test_allocate_case_no_without_registry(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    missing_registry = tmp_path / "case-registry.yaml"
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", missing_registry)

    case_no = litigation_run.allocate_case_no("DEL")

    year = litigation_run.datetime.now().strftime("%Y")
    assert case_no == f"{year}-DEL-001-001"
    assert not missing_registry.exists()


def test_allocate_case_no_custom_category_and_deliberation(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    registry = tmp_path / "case-registry.yaml"
    registry.write_text(
        yaml.dump({"year": 2026, "categories": {"SECU": 3}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", registry)

    case_no = litigation_run.allocate_case_no("SECU", deliberation=2)

    assert case_no == "2026-SECU-003-002"
    data = yaml.safe_load(registry.read_text(encoding="utf-8"))
    assert data["categories"]["SECU"] == 4


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("Simple Matter", "simple-matter"),
        ("!!!", "matter"),
        ("a" * 80, "a" * 60),
        ("  Mixed Case #42  ", "mixed-case-42"),
    ],
)
def test_slugify(raw: str, expected: str) -> None:
    assert litigation_run.slugify(raw) == expected


def test_save_transcript_courtroom_location(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(litigation_run, "REPO_ROOT", tmp_path)
    missing_registry = tmp_path / "courtroom" / "case-registry.yaml"
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", missing_registry)

    path = litigation_run.save_transcript("court matter", "Deliberation body.", location="courtroom")

    assert path.parent == tmp_path / "courtroom" / "transcripts"
    assert path.exists()


def test_save_transcript_appends_scribe_certification(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(litigation_run, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", tmp_path / "missing-registry.yaml")

    fake_module = tmp_path / "litigation_pkg"
    fake_module.mkdir()
    (fake_module / "run.py").write_text("", encoding="utf-8")
    (fake_module / "transcripts").mkdir()
    monkeypatch.setattr(litigation_run, "__file__", str(fake_module / "run.py"))

    path = litigation_run.save_transcript("cert test", "Body without footer.")
    content = path.read_text(encoding="utf-8")

    assert "> *Transcript certified by MORNINGSTAR::SCRIBE*" in content


def test_save_transcript_truncates_long_matter_title(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(litigation_run, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(litigation_run, "REGISTRY_PATH", tmp_path / "missing-registry.yaml")

    fake_module = tmp_path / "litigation_pkg"
    fake_module.mkdir()
    (fake_module / "run.py").write_text("", encoding="utf-8")
    (fake_module / "transcripts").mkdir()
    monkeypatch.setattr(litigation_run, "__file__", str(fake_module / "run.py"))

    long_matter = "x" * 100
    path = litigation_run.save_transcript(long_matter, "Body.")
    content = path.read_text(encoding="utf-8")

    assert "# Transcript: In Re: " + ("x" * 80) + "..." in content
