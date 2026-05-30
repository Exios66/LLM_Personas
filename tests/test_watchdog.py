"""Regression tests for executive watchdog override detection."""

from __future__ import annotations

import json
from pathlib import Path

from executive.watchdog import run_checks


def _write_actions_log(path: Path, entries: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def test_watchdog_alerts_on_override_without_proof(
    tmp_path: Path, monkeypatch
) -> None:
    actions_log = tmp_path / "logs" / "executive_actions.log"
    judicial_log = tmp_path / "logs" / "judicial_decisions.log"
    judicial_log.parent.mkdir(parents=True)

    _write_actions_log(
        actions_log,
        [
            {
                "timestamp": "2026-05-30T00:00:00+00:00",
                "action_type": "override_emergency",
                "ruling_id": "2026-FAKE-001",
                "description": "unauthorized override",
            }
        ],
    )

    monkeypatch.setattr("executive.watchdog._actions_log_path", lambda: actions_log)
    monkeypatch.setattr("executive.watchdog._log_path", lambda base_dir=None: judicial_log)
    monkeypatch.setattr(
        "executive.judicial_log._log_path",
        lambda base_dir=None: judicial_log,
    )

    ok, alerts = run_checks()
    assert ok is False
    assert any("missing cryptographic proof" in a for a in alerts)
