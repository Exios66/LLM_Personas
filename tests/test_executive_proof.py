"""Regression tests for executive override cryptographic proofs."""

from __future__ import annotations

import pytest

from executive.proof import SEPARATOR, OverrideProof, _get_secret


def test_generate_and_verify_round_trip(tmp_path, monkeypatch) -> None:
    secret_path = tmp_path / "secret"
    secret_hex = OverrideProof.generate_secret_file(secret_path)
    monkeypatch.delenv("EXECUTIVE_PROOF_SECRET", raising=False)

    proof = OverrideProof.generate(
        "2026-DEL-001",
        "emergency containment",
        timestamp="2026-05-27T12:00:00+00:00",
        secret_path=secret_path,
    )
    ts = OverrideProof.verify(
        proof,
        "2026-DEL-001",
        "emergency containment",
        secret_path=secret_path,
    )
    assert ts == "2026-05-27T12:00:00+00:00"
    assert secret_hex  # setup wrote a 64-char hex secret


def test_verify_rejects_tampered_signature(tmp_path, monkeypatch) -> None:
    secret_path = tmp_path / "secret"
    OverrideProof.generate_secret_file(secret_path)
    monkeypatch.delenv("EXECUTIVE_PROOF_SECRET", raising=False)

    proof = OverrideProof.generate(
        "2026-DEL-002",
        "court approval",
        timestamp="2026-05-27T12:00:00+00:00",
        secret_path=secret_path,
    )
    ts, sig = proof.split(SEPARATOR, 1)
    tampered = f"{ts}{SEPARATOR}{'0' * len(sig)}"

    assert (
        OverrideProof.verify(
            tampered,
            "2026-DEL-002",
            "court approval",
            secret_path=secret_path,
        )
        is None
    )


def test_verify_rejects_malformed_proof_string(tmp_path, monkeypatch) -> None:
    secret_path = tmp_path / "secret"
    OverrideProof.generate_secret_file(secret_path)
    monkeypatch.delenv("EXECUTIVE_PROOF_SECRET", raising=False)

    assert (
        OverrideProof.verify("no-separator-here", "id", "reason", secret_path=secret_path)
        is None
    )


def test_get_secret_from_env_hex(monkeypatch) -> None:
    monkeypatch.setenv("EXECUTIVE_PROOF_SECRET", "0x" + "ab" * 32)
    secret = _get_secret()
    assert secret == bytes.fromhex("ab" * 32)


def test_get_secret_missing_raises(tmp_path, monkeypatch) -> None:
    monkeypatch.delenv("EXECUTIVE_PROOF_SECRET", raising=False)
    missing = tmp_path / "nope"
    with pytest.raises(FileNotFoundError, match="Executive proof secret"):
        _get_secret(secret_path=missing)
