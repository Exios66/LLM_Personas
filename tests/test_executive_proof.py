"""Regression tests for executive override cryptographic proof."""

from __future__ import annotations

import os

import pytest

from executive.proof import OverrideProof, SECRET_ENV


def test_override_proof_generate_and_verify_round_trip(tmp_path) -> None:
    secret_path = tmp_path / "secret"
    secret_path.write_bytes(bytes.fromhex("ab" * 32))

    proof = OverrideProof.generate(
        "2026-DEL-001",
        "emergency containment",
        timestamp="2026-05-29T12:00:00+00:00",
        secret_path=secret_path,
    )
    ts = OverrideProof.verify(
        proof,
        "2026-DEL-001",
        "emergency containment",
        secret_path=secret_path,
    )
    assert ts == "2026-05-29T12:00:00+00:00"


def test_override_proof_verify_rejects_tampered_signature(tmp_path) -> None:
    secret_path = tmp_path / "secret"
    secret_path.write_bytes(b"test-secret-bytes")

    proof = OverrideProof.generate(
        "2026-DEL-001",
        "court approval",
        timestamp="2026-05-29T12:00:00+00:00",
        secret_path=secret_path,
    )
    ts, sig = proof.split("||", 1)
    tampered = f"{ts}||{'0' * len(sig)}"
    assert OverrideProof.verify(tampered, "2026-DEL-001", "court approval", secret_path=secret_path) is None


def test_get_secret_from_env_hex(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(SECRET_ENV, "0x" + ("cd" * 32))
    proof = OverrideProof.generate(
        "2026-SECU-042",
        "approved override",
        timestamp="2026-05-29T12:00:00+00:00",
    )
    assert OverrideProof.verify(proof, "2026-SECU-042", "approved override") == "2026-05-29T12:00:00+00:00"
    monkeypatch.delenv(SECRET_ENV, raising=False)


def test_get_secret_missing_raises(tmp_path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(SECRET_ENV, raising=False)
    missing = tmp_path / "no-secret"
    with pytest.raises(FileNotFoundError, match="Executive proof secret not found"):
        OverrideProof.generate("2026-DEL-001", "reason", secret_path=missing)
