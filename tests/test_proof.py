"""Regression tests for executive override cryptographic proofs."""

from __future__ import annotations

import secrets

from executive.proof import OverrideProof


def test_override_proof_round_trip(tmp_path) -> None:
    secret_path = tmp_path / "secret"
    secret_path.write_text(secrets.token_hex(32), encoding="utf-8")
    ts = "2026-06-05T12:00:00+00:00"

    proof = OverrideProof.generate(
        "2026-DEL-001",
        "emergency",
        timestamp=ts,
        secret_path=secret_path,
    )
    assert OverrideProof.verify(proof, "2026-DEL-001", "emergency", secret_path=secret_path) == ts


def test_override_proof_rejects_tampered_reason(tmp_path) -> None:
    secret_path = tmp_path / "secret"
    secret_path.write_text(secrets.token_hex(32), encoding="utf-8")
    proof = OverrideProof.generate(
        "2026-DEL-001",
        "emergency",
        timestamp="2026-06-05T12:00:00+00:00",
        secret_path=secret_path,
    )
    assert OverrideProof.verify(proof, "2026-DEL-001", "other reason", secret_path=secret_path) is None


def test_override_proof_rejects_malformed_proof_string(tmp_path) -> None:
    secret_path = tmp_path / "secret"
    secret_path.write_text(secrets.token_hex(32), encoding="utf-8")
    assert OverrideProof.verify("not-a-valid-proof", "2026-DEL-001", "x", secret_path=secret_path) is None
