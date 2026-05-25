"""Regression tests for executive override cryptographic proof."""

from __future__ import annotations

import pytest

from executive.proof import OverrideProof, SECRET_ENV


def test_generate_and_verify_roundtrip(tmp_path) -> None:
    secret_path = tmp_path / ".executive_secret"
    secret_path.write_bytes(bytes.fromhex("ab" * 32))

    proof = OverrideProof.generate(
        "2026-DEL-001",
        "emergency containment",
        timestamp="2026-05-25T12:00:00+00:00",
        secret_path=secret_path,
    )
    ts = OverrideProof.verify(
        proof,
        "2026-DEL-001",
        "emergency containment",
        secret_path=secret_path,
    )
    assert ts == "2026-05-25T12:00:00+00:00"


def test_verify_rejects_tampered_reason(tmp_path) -> None:
    secret_path = tmp_path / ".executive_secret"
    secret_path.write_bytes(bytes.fromhex("cd" * 32))

    proof = OverrideProof.generate(
        "2026-DEL-001",
        "court-approved override",
        timestamp="2026-05-25T12:00:00+00:00",
        secret_path=secret_path,
    )
    assert (
        OverrideProof.verify(
            proof,
            "2026-DEL-001",
            "different reason",
            secret_path=secret_path,
        )
        is None
    )


def test_verify_rejects_malformed_proof(tmp_path) -> None:
    secret_path = tmp_path / ".executive_secret"
    secret_path.write_bytes(bytes.fromhex("ef" * 32))

    assert (
        OverrideProof.verify("not-a-valid-proof", "2026-DEL-001", "reason", secret_path=secret_path)
        is None
    )


def test_get_secret_from_env_hex_with_prefix(
    tmp_path, monkeypatch: pytest.MonkeyPatch
) -> None:
    secret_hex = "11" * 32
    monkeypatch.setenv(SECRET_ENV, f"0x{secret_hex}")

    proof = OverrideProof.generate(
        "2026-SECU-042",
        "test",
        timestamp="2026-01-01T00:00:00+00:00",
        secret_path=tmp_path / "unused",
    )
    # Env takes precedence over missing file path when secret_path points to nonexistent
    assert (
        OverrideProof.verify(
            proof,
            "2026-SECU-042",
            "test",
            secret_path=tmp_path / "unused",
        )
        == "2026-01-01T00:00:00+00:00"
    )
    monkeypatch.delenv(SECRET_ENV, raising=False)
