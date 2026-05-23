"""Regression tests for executive watchdog oversight checks."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import patch

from executive.judicial_log import JudicialLog, compute_ruling_hash
from executive.watchdog import OVERRIDE_THRESHOLD, record_action, run_checks


def _write_actions(path: Path, entries: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(e) for e in entries) + ("\n" if entries else ""),
        encoding="utf-8",
    )


def test_run_checks_passes_with_approved_ruling(tmp_path: Path) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "executive_actions.log"
    log = JudicialLog(log_path=log_path)
    log.append(
        "2026-DEL-001: Approved deploy",
        compute_ruling_hash("ruling body"),
        "litigation/transcripts/2026-DEL-001-topic.md",
    )
    _write_actions(
        actions_path,
        [
            {
                "timestamp": "2026-05-19T12:00:00+00:00",
                "action_type": "execute",
                "ruling_id": "2026-DEL-001",
                "description": "deploy per ruling",
            }
        ],
    )

    with (
        patch("executive.watchdog.JudicialLog", return_value=log),
        patch("executive.watchdog._actions_log_path", return_value=actions_path),
    ):
        ok, alerts = run_checks()

    assert ok is True
    assert alerts == []


def test_run_checks_alerts_on_unapproved_action_without_proof(tmp_path: Path) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "executive_actions.log"
    log = JudicialLog(log_path=log_path)
    log.append("other matter", compute_ruling_hash("x"), "src.md")
    _write_actions(
        actions_path,
        [
            {
                "timestamp": "2026-05-19T12:00:00+00:00",
                "action_type": "execute",
                "ruling_id": "2026-SEC-999",
                "description": "no matching judicial entry",
            }
        ],
    )

    with (
        patch("executive.watchdog.JudicialLog", return_value=log),
        patch("executive.watchdog._actions_log_path", return_value=actions_path),
    ):
        ok, alerts = run_checks()

    assert ok is False
    assert any("without judicial approval" in a for a in alerts)


def test_run_checks_alerts_on_tampered_judicial_log(tmp_path: Path) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "executive_actions.log"
    log = JudicialLog(log_path=log_path)
    log.append("matter", compute_ruling_hash("content"), "src.md")

    lines = log_path.read_text(encoding="utf-8").strip().split("\n")
    entry = json.loads(lines[0])
    entry["entry_hash"] = "0" * 64
    log_path.write_text(json.dumps(entry) + "\n", encoding="utf-8")
    _write_actions(actions_path, [])

    with (
        patch("executive.watchdog.JudicialLog", return_value=JudicialLog(log_path=log_path)),
        patch("executive.watchdog._actions_log_path", return_value=actions_path),
    ):
        ok, alerts = run_checks()

    assert ok is False
    assert any("Log integrity" in a for a in alerts)


def test_run_checks_override_frequency_threshold(tmp_path: Path) -> None:
    log_path = tmp_path / "judicial_decisions.log"
    actions_path = tmp_path / "executive_actions.log"
    log = JudicialLog(log_path=log_path)
    log.append("matter", compute_ruling_hash("x"), "src.md")

    overrides = [
        {
            "timestamp": "2026-05-19T12:00:00+00:00",
            "action_type": "override",
            "ruling_id": "2026-DEL-001",
            "description": f"override {i}",
            "override_proof": f"ts||sig{i}",
        }
        for i in range(OVERRIDE_THRESHOLD + 1)
    ]
    _write_actions(actions_path, overrides)

    with (
        patch("executive.watchdog.JudicialLog", return_value=log),
        patch("executive.watchdog._actions_log_path", return_value=actions_path),
    ):
        ok, alerts = run_checks()

    assert ok is False
    assert any("Override frequency exceeds threshold" in a for a in alerts)


def test_record_action_appends_ndjson(tmp_path: Path) -> None:
    actions_path = tmp_path / "executive_actions.log"
    with patch("executive.watchdog._actions_log_path", return_value=actions_path):
        record_action("execute", "2026-DEL-001", "did the thing", proof=None)

    lines = actions_path.read_text(encoding="utf-8").strip().split("\n")
    assert len(lines) == 1
    entry = json.loads(lines[0])
    assert entry["ruling_id"] == "2026-DEL-001"
    assert entry["action_type"] == "execute"
