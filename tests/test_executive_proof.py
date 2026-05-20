"""Regression tests for executive override cryptographic proofs."""

from __future__ import annotations

import os

import pytest

from executive.proof import SECRET_ENV, OverrideProof


def test_generate_and_verify_round_trip(tmp_path) -> None:
    secret_path = tmp_path / "secret"
    secret_path.write_bytes(bytes.fromhex("aa" * 32))

    proof = OverrideProof.generate(
        "ruling-42",
        "emergency containment",
        timestamp="2026-05-20T12:00:00+00:00",
        secret_path=secret_path,
    )
    ts = OverrideProof.verify(
        proof,
        "ruling-42",
        "emergency containment",
        secret_path=secret_path,
    )
    assert ts == "2026-05-20T12:00:00+00:00"


def test_verify_rejects_tampered_signature(tmp_path) -> None:
    secret_path = tmp_path / "secret"
    secret_path.write_bytes(b"test-secret-bytes")

    proof = OverrideProof.generate(
        "r1",
        "reason",
        timestamp="2026-01-01T00:00:00+00:00",
        secret_path=secret_path,
    )
    ts, sig = proof.split("||", 1)
    bad = f"{ts}||{'0' * len(sig)}"
    assert OverrideProof.verify(bad, "r1", "reason", secret_path=secret_path) is None


def test_verify_rejects_wrong_ruling_id(tmp_path) -> None:
    secret_path = tmp_path / "secret"
    secret_path.write_bytes(b"another-secret")

    proof = OverrideProof.generate("r1", "reason", secret_path=secret_path)
    assert OverrideProof.verify(proof, "r2", "reason", secret_path=secret_path) is None


def test_get_secret_from_env_hex(monkeypatch: pytest.MonkeyPatch, tmp_path) -> None:
    monkeypatch.setenv(SECRET_ENV, "0x" + "ab" * 32)
    proof = OverrideProof.generate("r", "why", timestamp="2026-05-20T00:00:00+00:00")
    assert OverrideProof.verify(proof, "r", "why") == "2026-05-20T00:00:00+00:00"


def test_missing_secret_raises(tmp_path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(SECRET_ENV, raising=False)
    with pytest.raises(FileNotFoundError, match=SECRET_ENV):
        OverrideProof.generate("r", "why", secret_path=tmp_path / "missing")
