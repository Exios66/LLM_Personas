"""Regression tests for courtroom portal generate post-processing."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
GENERATE_SCRIPT = REPO_ROOT / "courtroom" / "portal" / "generate.py"


def _load_generate_module():
    spec = importlib.util.spec_from_file_location("portal_generate", GENERATE_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_inject_courtroom_css(tmp_path: Path) -> None:
    mod = _load_generate_module()
    html_file = tmp_path / "page.html"
    html_file.write_text("<html><head></head><body></body></html>", encoding="utf-8")

    injected = mod.inject_courtroom_css(tmp_path)

    content = html_file.read_text(encoding="utf-8")
    assert injected == 1
    assert "MORNINGSTAR Courtroom Portal" in content
    assert "</head>" in content


def test_apply_personality_styling(tmp_path: Path) -> None:
    mod = _load_generate_module()
    transcript_dir = tmp_path / "courtroom" / "transcripts"
    transcript_dir.mkdir(parents=True)
    html_file = transcript_dir / "sample.html"
    html_file.write_text(
        "<p>MORNINGSTAR ruled YES while Architect voted NO and Scribe recorded ABSTAIN.</p>",
        encoding="utf-8",
    )

    styled = mod.apply_personality_styling(tmp_path)

    content = html_file.read_text(encoding="utf-8")
    assert styled == 1
    assert 'class="p-morningstar"' in content
    assert 'class="vote-yes"' in content
    assert 'class="vote-no"' in content
    assert 'class="vote-abstain"' in content


def test_generate_transcript_index(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    mod = _load_generate_module()
    transcripts_dir = tmp_path / "transcripts"
    transcripts_dir.mkdir()
    (transcripts_dir / "20260215_120000_framework_review.md").write_text("# Review\n", encoding="utf-8")
    (transcripts_dir / "README.md").write_text("ignore\n", encoding="utf-8")
    monkeypatch.setattr(mod, "BASE_DIR", tmp_path)

    index_path = mod.generate_transcript_index(tmp_path)

    assert index_path is not None
    html = Path(index_path).read_text(encoding="utf-8")
    assert "Framework Review" in html
    assert "courtroom/transcripts/20260215_120000_framework_review.html" in html
