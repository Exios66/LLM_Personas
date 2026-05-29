"""Regression tests for executive watchdog oversight checks."""

from __future__ import annotations

import json

import pytest

from executive import watchdog
from executive.judicial_log import JudicialLog, compute_ruling_hash


@pytest.fixture
def isolated_watchdog(tmp_path, monkeypatch):
    """Point watchdog and judicial log at temp files."""
    actions_log = tmp_path / "executive_actions.log"
    judicial_log = tmp_path / "judicial_decisions.log"

    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions_log)
    monkeypatch.setattr(
        "executive.judicial_log._log_path",
        lambda: judicial_log,
    )
    return actions_log, judicial_log


def test_run_checks_passes_with_approved_action(isolated_watchdog) -> None:
    actions_log, judicial_log = isolated_watchdog
    log = JudicialLog(log_path=judicial_log)
    log.append("2026-DEL-001: matter", compute_ruling_hash("ruling"), "src.md")

    watchdog.record_action("execute", "2026-DEL-001", "carry out ruling")

    ok, alerts = watchdog.run_checks()
    assert ok is True
    assert alerts == []
    assert actions_log.exists()


def test_run_checks_alerts_on_unapproved_action_without_proof(isolated_watchdog) -> None:
    _actions_log, judicial_log = isolated_watchdog
    JudicialLog(log_path=judicial_log)  # empty approvals

    watchdog.record_action("execute", "2026-UNKNOWN-999", "unapproved action")

    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("no override proof" in a for a in alerts)


def test_run_checks_allows_override_with_proof(isolated_watchdog, tmp_path) -> None:
    _actions_log, judicial_log = isolated_watchdog
    JudicialLog(log_path=judicial_log)

    secret_path = tmp_path / "secret"
    secret_path.write_bytes(b"watchdog-test-secret")
    from executive.proof import OverrideProof

    proof = OverrideProof.generate(
        "2026-SECU-042",
        "emergency override",
        timestamp="2026-05-29T12:00:00+00:00",
        secret_path=secret_path,
    )
    watchdog.record_action(
        "override execute",
        "2026-SECU-042",
        "emergency containment",
        proof=proof,
    )

    ok, alerts = watchdog.run_checks()
    assert ok is True
    assert alerts == []


def test_run_checks_alerts_on_tampered_judicial_log(isolated_watchdog) -> None:
    _actions_log, judicial_log = isolated_watchdog
    log = JudicialLog(log_path=judicial_log)
    log.append("matter", compute_ruling_hash("content"), "src.md")

    lines = judicial_log.read_text(encoding="utf-8").strip().split("\n")
    entry = json.loads(lines[0])
    entry["entry_hash"] = "0" * 64
    judicial_log.write_text(json.dumps(entry) + "\n", encoding="utf-8")

    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("Log integrity" in a for a in alerts)
