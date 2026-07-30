"""Regression tests for litigation transcript viewer filename parsing."""

from __future__ import annotations

from pathlib import Path

from litigation.viewer import _collect_transcripts, _resolve_transcript, _transcript_meta


def test_transcript_meta_iso_date_slug() -> None:
    date_str, topic = _transcript_meta(Path("2026-03-01-border-dispute.md"))
    assert date_str == "2026-03-01"
    assert topic == "Border Dispute"


def test_transcript_meta_non_iso_fallback() -> None:
    date_str, topic = _transcript_meta(Path("legacy_notes.md"))
    assert date_str == "—"
    assert topic == "Legacy Notes"


def test_collect_transcripts_skips_readme_and_dotfiles(tmp_path: Path, monkeypatch) -> None:
    transcripts = tmp_path / "transcripts"
    transcripts.mkdir()
    (transcripts / "README.md").write_text("docs", encoding="utf-8")
    (transcripts / ".hidden.md").write_text("x", encoding="utf-8")
    (transcripts / "2026-01-01-sample.md").write_text("# t", encoding="utf-8")

    import litigation.viewer as viewer

    monkeypatch.setattr(viewer, "TRANSCRIPTS_DIR", transcripts)
    rows = _collect_transcripts()
    assert len(rows) == 1
    assert rows[0][0].name == "2026-01-01-sample.md"
    assert rows[0][1] == "2026-01-01"
    assert rows[0][2] == "Sample"


def test_resolve_transcript_prefers_exact_suffix_over_broader_match(tmp_path: Path) -> None:
    """Short topic queries must not match unrelated longer stems (e.g. bar vs foo-bar)."""
    bar = tmp_path / "2026-06-01-bar.md"
    foo_bar = tmp_path / "2026-06-01-foo-bar.md"
    bar.write_text("# bar", encoding="utf-8")
    foo_bar.write_text("# foo bar", encoding="utf-8")

    rows = [
        (foo_bar, "2026-06-01", "Foo Bar"),
        (bar, "2026-06-01", "Bar"),
    ]
    resolved = _resolve_transcript("bar", rows)
    assert resolved == bar
