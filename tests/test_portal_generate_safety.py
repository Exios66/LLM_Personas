"""Tests for portal generate.py output directory safety guards."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

from courtroom.portal import generate as portal_generate


def test_validate_rejects_transcript_directory(tmp_path: Path) -> None:
    transcripts = tmp_path / "transcripts"
    transcripts.mkdir()
    (transcripts / "2026-05-28-sample.md").write_text("# sample\n", encoding="utf-8")

    with pytest.raises(SystemExit):
        portal_generate._validate_output_path(transcripts, force=True)


def test_validate_requires_force_for_non_default(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    custom = tmp_path / "custom-out"
    custom.mkdir()
    monkeypatch.setattr(portal_generate, "OUTPUT_DIR", tmp_path / "default-out")
    monkeypatch.setattr(portal_generate, "SCRIPT_DIR", tmp_path / "portal")
    monkeypatch.setattr(portal_generate, "BASE_DIR", tmp_path)

    with pytest.raises(SystemExit):
        portal_generate._validate_output_path(custom, force=False)


def test_validate_allows_default_output(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    default_out = tmp_path / "output"
    default_out.mkdir()
    monkeypatch.setattr(portal_generate, "OUTPUT_DIR", default_out)
    monkeypatch.setattr(portal_generate, "SCRIPT_DIR", tmp_path / "portal")
    monkeypatch.setattr(portal_generate, "BASE_DIR", tmp_path)

    portal_generate._validate_output_path(default_out, force=False)
