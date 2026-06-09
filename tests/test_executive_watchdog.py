"""Regression tests for executive watchdog oversight (executive/watchdog.py)."""

from __future__ import annotations

import json

import pytest

from executive import watchdog
from executive.judicial_log import JudicialLog, compute_ruling_hash


@pytest.fixture
def isolated_watchdog(tmp_path, monkeypatch):
    """Point watchdog and judicial log at temp directories."""
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "executive_actions.log"

    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions_path)
    monkeypatch.setattr(
        "executive.judicial_log._log_path",
        lambda base_dir=None: log_path,
    )
    return {"log_path": log_path, "actions_path": actions_path}


def test_run_checks_passes_with_approved_action(isolated_watchdog) -> None:
    log = JudicialLog()
    log.append(
        "2026-DEL-001: deploy",
        compute_ruling_hash("approved ruling"),
        "courtroom/transcripts/2026-06-09-deliberation.md",
    )
    watchdog.record_action("execute", "2026-DEL-001", "deploy per ruling")

    ok, alerts = watchdog.run_checks()
    assert ok is True
    assert alerts == []


def test_run_checks_alerts_unapproved_action_without_proof(isolated_watchdog) -> None:
    watchdog.record_action("execute", "2026-DEL-999", "action without approval")

    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("no override proof" in a for a in alerts)


def test_run_checks_alerts_on_log_integrity_failure(isolated_watchdog) -> None:
    log_path = isolated_watchdog["log_path"]
    log = JudicialLog(log_path=log_path)
    log.append("matter", compute_ruling_hash("content"), "src.md")

    lines = log_path.read_text(encoding="utf-8").strip().split("\n")
    entry = json.loads(lines[0])
    entry["entry_hash"] = "0" * 64
    log_path.write_text(json.dumps(entry) + "\n", encoding="utf-8")

    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("Log integrity" in a for a in alerts)


def test_run_checks_alerts_override_frequency_threshold(isolated_watchdog, monkeypatch) -> None:
    monkeypatch.setattr(watchdog, "OVERRIDE_THRESHOLD", 2)
    for i in range(3):
        watchdog.record_action(
            "override",
            f"2026-DEL-{i:03d}",
            f"override {i}",
            proof=f"2026-06-09T12:00:0{i}+00:00||{'ab' * 32}",
        )

    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("Override frequency exceeds threshold" in a for a in alerts)


def test_read_actions_skips_malformed_lines(isolated_watchdog) -> None:
    actions_path = isolated_watchdog["actions_path"]
    actions_path.parent.mkdir(parents=True, exist_ok=True)
    actions_path.write_text(
        '{"action_type":"execute","ruling_id":"2026-DEL-001","description":"ok"}\n'
        "not json\n"
        '{"action_type":"execute","ruling_id":"2026-DEL-002","description":"also ok"}\n',
        encoding="utf-8",
    )

    actions = watchdog._read_actions()
    assert len(actions) == 2
    assert actions[0]["ruling_id"] == "2026-DEL-001"
