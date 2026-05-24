"""Regression tests for executive watchdog approval and override checks."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from executive.judicial_log import JudicialLog, compute_ruling_hash
from executive import watchdog


def _write_action(path: Path, entry: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def test_run_checks_ok_with_approved_ruling(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    judicial = tmp_path / "judicial_decisions.log"
    actions = tmp_path / "executive_actions.log"
    log = JudicialLog(log_path=judicial)
    log.append("2026-DEL-001: approved", compute_ruling_hash("ruling"), "t.md")
    _write_action(
        actions,
        {
            "ruling_id": "2026-DEL-001",
            "action_type": "execute",
            "description": "carry out ruling",
        },
    )

    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions)
    monkeypatch.setattr(
        "executive.judicial_log._log_path",
        lambda base_dir=None: judicial,
    )

    ok, alerts = watchdog.run_checks()
    assert ok is True
    assert alerts == []


def test_run_checks_flags_unapproved_action_without_proof(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    judicial = tmp_path / "judicial_decisions.log"
    actions = tmp_path / "executive_actions.log"
    JudicialLog(log_path=judicial)  # empty judicial log
    _write_action(
        actions,
        {
            "ruling_id": "2026-SECU-099",
            "action_type": "execute",
            "description": "unapproved",
        },
    )

    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions)
    monkeypatch.setattr(
        "executive.judicial_log._log_path",
        lambda base_dir=None: judicial,
    )

    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("without judicial approval" in a for a in alerts)


def test_run_checks_allows_override_with_proof(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    judicial = tmp_path / "judicial_decisions.log"
    actions = tmp_path / "executive_actions.log"
    JudicialLog(log_path=judicial)
    _write_action(
        actions,
        {
            "ruling_id": "2026-SECU-099",
            "action_type": "override_execute",
            "description": "emergency override",
            "override_proof": "signed-proof-blob",
        },
    )

    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions)
    monkeypatch.setattr(
        "executive.judicial_log._log_path",
        lambda base_dir=None: judicial,
    )

    ok, alerts = watchdog.run_checks()
    assert ok is True
    assert alerts == []


def test_run_checks_flags_override_frequency_threshold(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    judicial = tmp_path / "judicial_decisions.log"
    actions = tmp_path / "executive_actions.log"
    JudicialLog(log_path=judicial)
    for i in range(watchdog.OVERRIDE_THRESHOLD + 1):
        _write_action(
            actions,
            {
                "ruling_id": f"2026-OVR-{i:03d}",
                "action_type": "override",
                "description": f"override {i}",
                "override_proof": f"proof-{i}",
            },
        )

    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions)
    monkeypatch.setattr(
        "executive.judicial_log._log_path",
        lambda base_dir=None: judicial,
    )

    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("Override frequency exceeds threshold" in a for a in alerts)
