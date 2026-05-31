"""Regression tests for executive watchdog oversight checks."""

from __future__ import annotations

import json

import pytest

from executive.judicial_log import JudicialLog, compute_ruling_hash
from executive.watchdog import (
    OVERRIDE_THRESHOLD,
    _read_actions,
    record_action,
    run_checks,
)


@pytest.fixture
def isolated_watchdog_logs(tmp_path, monkeypatch: pytest.MonkeyPatch):
    """Point watchdog and judicial logs at a temp directory."""
    actions_log = tmp_path / "executive_actions.log"
    judicial_log = tmp_path / "judicial_decisions.log"
    actions_log.parent.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(
        "executive.watchdog._actions_log_path",
        lambda: actions_log,
    )
    monkeypatch.setattr(
        "executive.watchdog.JudicialLog",
        lambda: JudicialLog(log_path=judicial_log),
    )
    return actions_log, judicial_log


def test_run_checks_passes_when_action_matches_judicial_log(
    isolated_watchdog_logs,
) -> None:
    _, judicial_log_path = isolated_watchdog_logs
    log = JudicialLog(log_path=judicial_log_path)
    log.append(
        "2026-DEL-001: approved matter",
        compute_ruling_hash("ruling"),
        "courtroom/transcripts/2026-05-31-deliberation.md",
    )

    record_action("execute", "2026-DEL-001", "carry out ruling")
    ok, alerts = run_checks()
    assert ok is True
    assert alerts == []


def test_run_checks_flags_action_without_approval_or_proof(
    isolated_watchdog_logs,
) -> None:
    record_action("execute", "2026-DEL-999", "unapproved execution")
    ok, alerts = run_checks()
    assert ok is False
    assert any("without judicial approval" in a for a in alerts)


def test_run_checks_allows_override_when_proof_present(
    isolated_watchdog_logs, tmp_path
) -> None:
    secret_file = tmp_path / ".executive_secret"
    secret_file.write_bytes(b"test-secret-bytes-for-hmac\n")

    from executive.proof import OverrideProof

    proof = OverrideProof.generate(
        "2026-DEL-999",
        "emergency override",
        timestamp="2026-05-31T12:00:00+00:00",
        secret_path=secret_file,
    )
    record_action(
        "override_execute",
        "2026-DEL-999",
        "emergency",
        proof=proof,
    )
    ok, alerts = run_checks()
    assert ok is True
    assert alerts == []


def test_run_checks_alerts_when_override_frequency_exceeds_threshold(
    isolated_watchdog_logs, tmp_path
) -> None:
    secret_file = tmp_path / ".executive_secret"
    secret_file.write_bytes(b"override-secret\n")
    from executive.proof import OverrideProof

    for i in range(OVERRIDE_THRESHOLD + 1):
        proof = OverrideProof.generate(
            f"2026-DEL-{i:03d}",
            "batch override",
            timestamp=f"2026-05-31T12:00:{i:02d}+00:00",
            secret_path=secret_file,
        )
        record_action("override", f"2026-DEL-{i:03d}", "test", proof=proof)

    ok, alerts = run_checks()
    assert ok is False
    assert any("Override frequency exceeds threshold" in a for a in alerts)


def test_read_actions_skips_invalid_json_lines(isolated_watchdog_logs) -> None:
    actions_log, _ = isolated_watchdog_logs
    actions_log.write_text(
        '{"action_type":"execute","ruling_id":"x"}\n'
        "not json\n"
        '{"action_type":"execute","ruling_id":"y"}\n',
        encoding="utf-8",
    )
    actions = _read_actions()
    assert len(actions) == 2
    assert actions[0]["ruling_id"] == "x"
    assert actions[1]["ruling_id"] == "y"
