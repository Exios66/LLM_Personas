"""Regression tests for executive override cryptographic proof (executive/proof.py)."""

from __future__ import annotations

import os

import pytest

from executive.proof import OverrideProof, SEPARATOR


@pytest.fixture
def secret_file(tmp_path, monkeypatch):
    """Provide a deterministic secret via file and clear env override."""
    monkeypatch.delenv("EXECUTIVE_PROOF_SECRET", raising=False)
    path = tmp_path / ".executive_secret"
    path.write_bytes(bytes.fromhex("ab" * 32))
    return path


def test_generate_and_verify_round_trip(secret_file) -> None:
    ts = "2026-06-09T12:00:00+00:00"
    proof = OverrideProof.generate(
        "2026-DEL-001",
        "emergency override",
        timestamp=ts,
        secret_path=secret_file,
    )
    assert proof.startswith(ts + SEPARATOR)
    assert OverrideProof.verify(
        proof,
        "2026-DEL-001",
        "emergency override",
        secret_path=secret_file,
    ) == ts


def test_verify_rejects_wrong_ruling_id(secret_file) -> None:
    ts = "2026-06-09T12:00:00+00:00"
    proof = OverrideProof.generate("2026-DEL-001", "reason", timestamp=ts, secret_path=secret_file)
    assert OverrideProof.verify(proof, "2026-DEL-002", "reason", secret_path=secret_file) is None


def test_verify_rejects_malformed_proof(secret_file) -> None:
    assert OverrideProof.verify("not-a-valid-proof", "2026-DEL-001", "reason", secret_path=secret_file) is None


def test_get_secret_from_env_hex(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("EXECUTIVE_PROOF_SECRET", "0x" + "cd" * 32)
    ts = "2026-06-09T12:00:00+00:00"
    proof = OverrideProof.generate("2026-DEL-001", "court approval", timestamp=ts)
    assert OverrideProof.verify(proof, "2026-DEL-001", "court approval") == ts


def test_generate_secret_file_creates_readable_secret(tmp_path, monkeypatch) -> None:
    monkeypatch.delenv("EXECUTIVE_PROOF_SECRET", raising=False)
    path = tmp_path / "new_secret"
    hex_secret = OverrideProof.generate_secret_file(path)
    assert len(hex_secret) == 64
    assert path.exists()
    assert path.read_text().strip() == hex_secret
