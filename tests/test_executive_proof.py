"""Regression tests for executive override cryptographic proofs."""

from __future__ import annotations

import pytest

from executive.proof import OverrideProof, SEPARATOR


def test_generate_and_verify_round_trip(tmp_path) -> None:
    secret_path = tmp_path / ".executive_secret"
    OverrideProof.generate_secret_file(secret_path)

    proof = OverrideProof.generate(
        "2026-RUL-001",
        "emergency containment",
        timestamp="2026-06-02T12:00:00+00:00",
        secret_path=secret_path,
    )
    ts = OverrideProof.verify(
        proof,
        "2026-RUL-001",
        "emergency containment",
        secret_path=secret_path,
    )
    assert ts == "2026-06-02T12:00:00+00:00"
    assert SEPARATOR in proof


def test_verify_rejects_tampered_signature(tmp_path) -> None:
    secret_path = tmp_path / ".executive_secret"
    OverrideProof.generate_secret_file(secret_path)
    proof = OverrideProof.generate(
        "2026-RUL-002",
        "court-approved override",
        timestamp="2026-06-02T12:00:00+00:00",
        secret_path=secret_path,
    )
    ts_part, sig = proof.split(SEPARATOR, 1)
    tampered = f"{ts_part}{SEPARATOR}{'0' * len(sig)}"
    assert (
        OverrideProof.verify(
            tampered,
            "2026-RUL-002",
            "court-approved override",
            secret_path=secret_path,
        )
        is None
    )


def test_get_secret_from_env_hex(monkeypatch: pytest.MonkeyPatch, tmp_path) -> None:
    monkeypatch.setenv("EXECUTIVE_PROOF_SECRET", "ab" * 32)
    proof = OverrideProof.generate(
        "2026-RUL-003",
        "env secret path",
        timestamp="2026-06-02T12:00:00+00:00",
        secret_path=tmp_path / "unused",
    )
    assert (
        OverrideProof.verify(
            proof,
            "2026-RUL-003",
            "env secret path",
            secret_path=tmp_path / "unused",
        )
        == "2026-06-02T12:00:00+00:00"
    )
    monkeypatch.delenv("EXECUTIVE_PROOF_SECRET", raising=False)


def test_missing_secret_raises(tmp_path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("EXECUTIVE_PROOF_SECRET", raising=False)
    with pytest.raises(FileNotFoundError, match="Executive proof secret"):
        OverrideProof.generate(
            "2026-RUL-004",
            "no secret configured",
            secret_path=tmp_path / "missing",
        )
