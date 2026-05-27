"""Regression tests for executive watchdog oversight checks."""

from __future__ import annotations

import json

from executive.judicial_log import JudicialLog, compute_ruling_hash
from executive.watchdog import OVERRIDE_THRESHOLD, run_checks


def test_run_checks_passes_with_valid_log_and_no_actions(tmp_path, monkeypatch) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "logs" / "executive_actions.log"
    actions_path.parent.mkdir(parents=True, exist_ok=True)

    log = JudicialLog(log_path=log_path)
    log.append(
        "2026-DEL-001: matter",
        compute_ruling_hash("approved"),
        "courtroom/transcripts/example.md",
    )

    monkeypatch.setattr("executive.watchdog._actions_log_path", lambda: actions_path)
    monkeypatch.setattr("executive.watchdog.JudicialLog", lambda: JudicialLog(log_path=log_path))

    ok, alerts = run_checks()
    assert ok is True
    assert alerts == []


def test_run_checks_flags_action_without_approval_or_proof(tmp_path, monkeypatch) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "logs" / "executive_actions.log"
    actions_path.parent.mkdir(parents=True, exist_ok=True)

    JudicialLog(log_path=log_path).append(
        "other matter",
        compute_ruling_hash("x"),
        "src.md",
    )

    with open(actions_path, "w", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {
                    "timestamp": "2026-05-27T12:00:00+00:00",
                    "action_type": "execute",
                    "ruling_id": "2026-UNKNOWN-999",
                    "description": "unapproved",
                }
            )
            + "\n"
        )

    monkeypatch.setattr("executive.watchdog._actions_log_path", lambda: actions_path)
    monkeypatch.setattr("executive.watchdog.JudicialLog", lambda: JudicialLog(log_path=log_path))

    ok, alerts = run_checks()
    assert ok is False
    assert any("no override proof" in a for a in alerts)


def test_run_checks_flags_override_frequency(tmp_path, monkeypatch) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "logs" / "executive_actions.log"
    actions_path.parent.mkdir(parents=True, exist_ok=True)

    JudicialLog(log_path=log_path)

    lines = []
    for i in range(OVERRIDE_THRESHOLD + 1):
        lines.append(
            json.dumps(
                {
                    "timestamp": f"2026-05-27T12:00:{i:02d}+00:00",
                    "action_type": "override",
                    "ruling_id": f"2026-DEL-{i:03d}",
                    "description": "override",
                    "override_proof": f"ts||{'a' * 64}",
                }
            )
        )
    actions_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    monkeypatch.setattr("executive.watchdog._actions_log_path", lambda: actions_path)
    monkeypatch.setattr("executive.watchdog.JudicialLog", lambda: JudicialLog(log_path=log_path))

    ok, alerts = run_checks()
    assert ok is False
    assert any("Override frequency" in a for a in alerts)
