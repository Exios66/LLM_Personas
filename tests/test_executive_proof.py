"""Regression tests for executive override cryptographic proofs."""

from __future__ import annotations

import secrets

import pytest

from executive.proof import OverrideProof, _get_secret


def test_override_proof_generate_and_verify_roundtrip(tmp_path) -> None:
    secret_file = tmp_path / ".executive_secret"
    secret_file.write_text(secrets.token_hex(32), encoding="utf-8")
    ts = "2026-05-31T12:00:00+00:00"

    proof = OverrideProof.generate(
        "2026-DEL-001",
        "court-approved emergency",
        timestamp=ts,
        secret_path=secret_file,
    )
    verified = OverrideProof.verify(
        proof,
        "2026-DEL-001",
        "court-approved emergency",
        secret_path=secret_file,
    )
    assert verified == ts


def test_override_proof_verify_rejects_tampered_signature(tmp_path) -> None:
    secret_file = tmp_path / ".executive_secret"
    secret_file.write_text(secrets.token_hex(32), encoding="utf-8")
    proof = OverrideProof.generate(
        "2026-DEL-001",
        "reason",
        timestamp="2026-05-31T12:00:00+00:00",
        secret_path=secret_file,
    )
    ts, sig = proof.split("||", 1)
    bad_proof = f"{ts}||{'0' * len(sig)}"

    assert (
        OverrideProof.verify(
            bad_proof,
            "2026-DEL-001",
            "reason",
            secret_path=secret_file,
        )
        is None
    )


def test_override_proof_verify_rejects_malformed_proof_string(tmp_path) -> None:
    secret_file = tmp_path / ".executive_secret"
    secret_file.write_text(secrets.token_hex(32), encoding="utf-8")
    assert (
        OverrideProof.verify(
            "not-a-valid-proof",
            "2026-DEL-001",
            "reason",
            secret_path=secret_file,
        )
        is None
    )


def test_get_secret_from_env_hex_with_0x_prefix(monkeypatch: pytest.MonkeyPatch) -> None:
    raw = secrets.token_hex(32)
    monkeypatch.setenv("EXECUTIVE_PROOF_SECRET", f"0x{raw}")
    assert _get_secret() == bytes.fromhex(raw)


def test_get_secret_missing_raises(tmp_path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("EXECUTIVE_PROOF_SECRET", raising=False)
    missing = tmp_path / "no-secret-here"
    with pytest.raises(FileNotFoundError, match="Executive proof secret"):
        _get_secret(secret_path=missing)
