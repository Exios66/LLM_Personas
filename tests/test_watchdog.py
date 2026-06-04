"""Regression tests for executive watchdog approval and override checks."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from executive import watchdog
from executive.judicial_log import JudicialLog, compute_ruling_hash


def test_run_checks_flags_action_without_approval_or_proof(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "logs" / "executive_actions.log"
    actions_path.parent.mkdir(parents=True)

    log = JudicialLog(log_path=log_path)
    log.append("matter", compute_ruling_hash("ruling"), "2026-TEST-001-transcript.md")

    actions_path.write_text(
        json.dumps(
            {
                "action_type": "execute",
                "ruling_id": "2026-UNAPPROVED-999",
                "description": "run without proof",
            }
        )
        + "\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions_path)
    monkeypatch.setattr(
        "executive.judicial_log._log_path", lambda base_dir=None: log_path
    )

    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("without judicial approval" in a for a in alerts)


def test_run_checks_allows_override_with_proof(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "logs" / "executive_actions.log"
    actions_path.parent.mkdir(parents=True)
    actions_path.write_text(
        json.dumps(
            {
                "action_type": "execute",
                "ruling_id": "2026-UNAPPROVED-999",
                "description": "emergency",
                "override_proof": "signed-proof",
            }
        )
        + "\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions_path)
    monkeypatch.setattr(
        "executive.judicial_log._log_path", lambda base_dir=None: log_path
    )

    ok, alerts = watchdog.run_checks()
    assert ok is True
    assert alerts == []
