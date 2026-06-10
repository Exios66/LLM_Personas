"""Regression tests for executive watchdog override proof enforcement."""

from __future__ import annotations

import json

from executive.proof import OverrideProof
from executive.watchdog import run_checks


def _write_actions(path, actions: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for action in actions:
            f.write(json.dumps(action) + "\n")


def test_unapproved_action_with_fake_proof_fails(tmp_path, monkeypatch) -> None:
    secret_path = tmp_path / ".executive_secret"
    OverrideProof.generate_secret_file(secret_path)

    actions_path = tmp_path / "logs" / "executive_actions.log"
    _write_actions(
        actions_path,
        [
            {
                "action_type": "override_deploy",
                "ruling_id": "2026-DEL-999",
                "description": "Emergency rollback",
                "override_proof": "fake-proof",
            }
        ],
    )

    monkeypatch.setattr("executive.watchdog._actions_log_path", lambda: actions_path)
    monkeypatch.setattr("executive.proof.DEFAULT_SECRET_PATH", secret_path)

    ok, alerts = run_checks()
    assert ok is False
    assert any("Invalid override proof" in msg for msg in alerts)


def test_unapproved_action_with_valid_proof_passes(tmp_path, monkeypatch) -> None:
    secret_path = tmp_path / ".executive_secret"
    OverrideProof.generate_secret_file(secret_path)

    ruling_id = "2026-DEL-999"
    reason = "Emergency rollback per court approval"
    proof = OverrideProof.generate(ruling_id, reason, secret_path=secret_path)

    actions_path = tmp_path / "logs" / "executive_actions.log"
    _write_actions(
        actions_path,
        [
            {
                "action_type": "override_deploy",
                "ruling_id": ruling_id,
                "description": reason,
                "override_proof": proof,
            }
        ],
    )

    monkeypatch.setattr("executive.watchdog._actions_log_path", lambda: actions_path)
    monkeypatch.setattr("executive.proof.DEFAULT_SECRET_PATH", secret_path)

    ok, alerts = run_checks()
    assert ok is True
    assert alerts == []


def test_override_action_type_no_longer_bypasses_proof_check(tmp_path, monkeypatch) -> None:
    """Actions with 'override' in action_type previously skipped all proof checks."""
    secret_path = tmp_path / ".executive_secret"
    OverrideProof.generate_secret_file(secret_path)

    actions_path = tmp_path / "logs" / "executive_actions.log"
    _write_actions(
        actions_path,
        [
            {
                "action_type": "emergency_override",
                "ruling_id": "2026-DEL-888",
                "description": "Bypass attempt",
            }
        ],
    )

    monkeypatch.setattr("executive.watchdog._actions_log_path", lambda: actions_path)
    monkeypatch.setattr("executive.proof.DEFAULT_SECRET_PATH", secret_path)

    ok, alerts = run_checks()
    assert ok is False
    assert any("no override proof" in msg for msg in alerts)
