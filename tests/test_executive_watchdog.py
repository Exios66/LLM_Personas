"""Regression tests for executive watchdog approval and override checks."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from executive import watchdog
from executive.judicial_log import JudicialLog, compute_ruling_hash


def _write_action(path: Path, entry: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


@pytest.fixture
def isolated_logs(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "executive_actions.log"
    judicial = JudicialLog(log_path=log_path)

    monkeypatch.setattr(watchdog, "JudicialLog", lambda: judicial)
    monkeypatch.setattr(watchdog, "_actions_log_path", lambda: actions_path)
    return judicial, actions_path


def test_run_checks_passes_with_empty_actions(isolated_logs) -> None:
    ok, alerts = watchdog.run_checks()
    assert ok is True
    assert alerts == []


def test_run_checks_flags_action_without_approval_or_proof(
    isolated_logs,
) -> None:
    _, actions_path = isolated_logs
    _write_action(
        actions_path,
        {
            "action_type": "deploy",
            "ruling_id": "2026-SECU-999",
            "description": "unapproved deploy",
        },
    )
    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("no override proof" in a for a in alerts)


def test_run_checks_allows_action_when_ruling_in_judicial_log(
    isolated_logs,
) -> None:
    judicial, actions_path = isolated_logs
    judicial.append(
        "2026-SECU-042: approved matter",
        compute_ruling_hash("ruling"),
        "courtroom/transcripts/2026-SECU-042.md",
    )
    _write_action(
        actions_path,
        {
            "action_type": "deploy",
            "ruling_id": "2026-SECU-042",
            "description": "approved deploy",
        },
    )
    ok, alerts = watchdog.run_checks()
    assert ok is True
    assert alerts == []


def test_run_checks_flags_excessive_overrides(isolated_logs) -> None:
    _, actions_path = isolated_logs
    for i in range(watchdog.OVERRIDE_THRESHOLD + 1):
        _write_action(
            actions_path,
            {
                "action_type": "override",
                "ruling_id": f"2026-SECU-{i:03d}",
                "description": "override",
                "override_proof": f"ts||sig{i}",
            },
        )
    ok, alerts = watchdog.run_checks()
    assert ok is False
    assert any("Override frequency" in a for a in alerts)
