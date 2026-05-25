"""Regression tests for executive watchdog approval and log integrity checks."""

from __future__ import annotations

import json

import pytest

from executive import watchdog
from executive.judicial_log import JudicialLog, compute_ruling_hash
from executive.proof import OverrideProof


def _write_action(path, **fields) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(fields, ensure_ascii=False) + "\n")


def test_run_checks_passes_with_approved_ruling(tmp_path, monkeypatch: pytest.MonkeyPatch) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "executive_actions.log"

    log = JudicialLog(log_path=log_path)
    log.append(
        "deploy hotfix",
        compute_ruling_hash("approved"),
        "courtroom/transcripts/2026-DEL-001-bench.md",
    )

    _write_action(
        actions_path,
        action_type="execute",
        ruling_id="2026-DEL-001",
        description="apply ruling",
    )

    monkeypatch.setattr(watchdog, "JudicialLog", lambda: JudicialLog(log_path=log_path))
    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions_path)

    ok, alerts = watchdog.run_checks()
    assert ok is True
    assert alerts == []


def test_run_checks_alerts_on_unapproved_action_without_proof(
    tmp_path, monkeypatch: pytest.MonkeyPatch
) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "executive_actions.log"

    JudicialLog(log_path=log_path)  # empty approvals

    _write_action(
        actions_path,
        action_type="execute",
        ruling_id="2026-UNKNOWN-999",
        description="rogue execution",
    )

    monkeypatch.setattr(watchdog, "JudicialLog", lambda: JudicialLog(log_path=log_path))
    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions_path)

    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("without judicial approval" in a for a in alerts)


def test_run_checks_alerts_on_tampered_judicial_log(
    tmp_path, monkeypatch: pytest.MonkeyPatch
) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "executive_actions.log"

    log = JudicialLog(log_path=log_path)
    log.append("matter", compute_ruling_hash("x"), "src.md")
    lines = log_path.read_text(encoding="utf-8").strip().split("\n")
    entry = json.loads(lines[0])
    entry["entry_hash"] = "0" * 64
    log_path.write_text(json.dumps(entry) + "\n", encoding="utf-8")

    monkeypatch.setattr(watchdog, "JudicialLog", lambda: JudicialLog(log_path=log_path))
    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions_path)

    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("Log integrity" in a for a in alerts)


def test_run_checks_override_frequency_threshold(
    tmp_path, monkeypatch: pytest.MonkeyPatch
) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "executive_actions.log"
    secret_path = tmp_path / ".executive_secret"
    secret_path.write_bytes(bytes.fromhex("99" * 32))

    proof = OverrideProof.generate(
        "2026-DEL-001",
        "emergency",
        timestamp="2026-05-25T12:00:00+00:00",
        secret_path=secret_path,
    )
    for i in range(3):
        _write_action(
            actions_path,
            action_type="override",
            ruling_id=f"2026-DEL-00{i}",
            description="override",
            override_proof=proof,
        )

    monkeypatch.setattr(watchdog, "JudicialLog", lambda: JudicialLog(log_path=log_path))
    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions_path)
    monkeypatch.setattr(watchdog, "OVERRIDE_THRESHOLD", 2)

    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("Override frequency exceeds threshold" in a for a in alerts)
