"""Regression tests for executive watchdog approval and override checks."""

from __future__ import annotations

import json

from executive import watchdog
from executive.judicial_log import JudicialLog, compute_ruling_hash
from executive.proof import OverrideProof


def _write_actions(path, entries: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(e, ensure_ascii=False) for e in entries) + "\n",
        encoding="utf-8",
    )


def test_watchdog_ok_when_action_matches_judicial_log(tmp_path, monkeypatch) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    log = JudicialLog(log_path=log_path)
    log.append("2026-DEL-001: approved deploy", compute_ruling_hash("ruling"), "src.md")

    actions_path = tmp_path / "executive_actions.log"
    _write_actions(
        actions_path,
        [{"ruling_id": "2026-DEL-001", "action_type": "deploy", "description": "ok"}],
    )

    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions_path)
    monkeypatch.setattr(watchdog, "JudicialLog", lambda: JudicialLog(log_path=log_path))

    ok, alerts = watchdog.run_checks()
    assert ok is True
    assert alerts == []


def test_watchdog_flags_unapproved_action_without_proof(tmp_path, monkeypatch) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    JudicialLog(log_path=log_path).append(
        "2026-DEL-001: matter", compute_ruling_hash("ruling"), "src.md"
    )

    actions_path = tmp_path / "executive_actions.log"
    _write_actions(
        actions_path,
        [{"ruling_id": "2026-UNKNOWN-999", "action_type": "deploy", "description": "rogue"}],
    )

    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions_path)
    monkeypatch.setattr(watchdog, "JudicialLog", lambda: JudicialLog(log_path=log_path))

    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("without judicial approval" in msg for msg in alerts)


def test_watchdog_allows_override_with_valid_proof(tmp_path, monkeypatch) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    JudicialLog(log_path=log_path).append(
        "2026-DEL-001: matter", compute_ruling_hash("ruling"), "src.md"
    )

    secret_path = tmp_path / "secret"
    secret_path.write_text("ab" * 32, encoding="utf-8")
    proof = OverrideProof.generate(
        "2026-UNKNOWN-999",
        "court-approved emergency",
        timestamp="2026-06-05T12:00:00+00:00",
        secret_path=secret_path,
    )

    actions_path = tmp_path / "executive_actions.log"
    _write_actions(
        actions_path,
        [
            {
                "ruling_id": "2026-UNKNOWN-999",
                "action_type": "override deploy",
                "description": "emergency",
                "override_proof": proof,
            }
        ],
    )

    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions_path)
    monkeypatch.setattr(watchdog, "JudicialLog", lambda: JudicialLog(log_path=log_path))

    ok, alerts = watchdog.run_checks()
    assert ok is True
    assert alerts == []
