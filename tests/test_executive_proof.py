"""Regression tests for executive override cryptographic proof."""

from __future__ import annotations

from executive.proof import OverrideProof


def test_generate_and_verify_roundtrip(tmp_path) -> None:
    secret_path = tmp_path / ".executive_secret"
    secret_path.write_text("a" * 64, encoding="utf-8")
    ts = "2026-06-01T12:00:00+00:00"

    proof = OverrideProof.generate(
        "2026-SECU-042",
        "emergency patch",
        timestamp=ts,
        secret_path=secret_path,
    )
    verified_ts = OverrideProof.verify(
        proof,
        "2026-SECU-042",
        "emergency patch",
        secret_path=secret_path,
    )
    assert verified_ts == ts


def test_verify_rejects_tampered_ruling_id(tmp_path) -> None:
    secret_path = tmp_path / ".executive_secret"
    secret_path.write_text("b" * 64, encoding="utf-8")
    proof = OverrideProof.generate(
        "2026-LEGAL-001",
        "court approval",
        timestamp="2026-06-01T12:00:00+00:00",
        secret_path=secret_path,
    )
    assert (
        OverrideProof.verify(
            proof,
            "2026-LEGAL-002",
            "court approval",
            secret_path=secret_path,
        )
        is None
    )


def test_verify_rejects_malformed_proof_string(tmp_path) -> None:
    secret_path = tmp_path / ".executive_secret"
    secret_path.write_text("c" * 64, encoding="utf-8")
    assert (
        OverrideProof.verify(
            "not-a-valid-proof",
            "2026-SECU-001",
            "reason",
            secret_path=secret_path,
        )
        is None
    )
