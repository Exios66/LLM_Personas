"""Regression tests for append-only judicial decision log integrity."""

from __future__ import annotations

import json

from executive.judicial_log import JudicialLog, compute_ruling_hash


def test_append_chains_entries_and_verify_passes(tmp_path) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    log = JudicialLog(log_path=log_path)

    e1 = log.append("matter-a", compute_ruling_hash("ruling A"), "transcript-a.md")
    e2 = log.append("matter-b", compute_ruling_hash("ruling B"), "transcript-b.md")

    assert e1["prev_hash"] == ""
    assert e2["prev_hash"] == e1["entry_hash"]

    ok, errors = log.verify()
    assert ok is True
    assert errors == []
    assert len(log.entries()) == 2


def test_verify_detects_tampered_entry_hash(tmp_path) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    log = JudicialLog(log_path=log_path)
    log.append("matter", compute_ruling_hash("content"), "src.md")

    lines = log_path.read_text(encoding="utf-8").strip().split("\n")
    entry = json.loads(lines[0])
    entry["entry_hash"] = "0" * 64
    log_path.write_text(json.dumps(entry) + "\n", encoding="utf-8")

    ok, errors = log.verify()
    assert ok is False
    assert any("entry_hash mismatch" in e for e in errors)
