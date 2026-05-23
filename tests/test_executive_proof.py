"""Regression tests for executive override cryptographic proof."""

from __future__ import annotations

import os

import pytest

from executive.proof import OverrideProof, SECRET_ENV


def test_generate_and_verify_roundtrip(tmp_path) -> None:
    secret_file = tmp_path / ".executive_secret"
    secret_file.write_text("a" * 64, encoding="utf-8")

    proof = OverrideProof.generate(
        "2026-DEL-001",
        "emergency court approval",
        timestamp="2026-05-19T12:00:00+00:00",
        secret_path=secret_file,
    )
    ts = OverrideProof.verify(
        proof,
        "2026-DEL-001",
        "emergency court approval",
        secret_path=secret_file,
    )
    assert ts == "2026-05-19T12:00:00+00:00"


def test_verify_rejects_tampered_signature(tmp_path) -> None:
    secret_file = tmp_path / ".executive_secret"
    secret_file.write_text("b" * 64, encoding="utf-8")

    proof = OverrideProof.generate(
        "2026-DEL-002",
        "approved override",
        timestamp="2026-05-19T12:00:00+00:00",
        secret_path=secret_file,
    )
    ts, sig = proof.split("||", 1)
    bad = f"{ts}||{'0' * len(sig)}"

    assert (
        OverrideProof.verify(
            bad,
            "2026-DEL-002",
            "approved override",
            secret_path=secret_file,
        )
        is None
    )


def test_get_secret_from_env_hex_prefix(monkeypatch: pytest.MonkeyPatch, tmp_path) -> None:
    raw = "ab" * 32
    monkeypatch.setenv(SECRET_ENV, f"0x{raw}")

    proof = OverrideProof.generate(
        "2026-DEL-003",
        "env secret",
        timestamp="2026-05-19T13:00:00+00:00",
        secret_path=tmp_path / "missing",
    )
    assert (
        OverrideProof.verify(
            proof,
            "2026-DEL-003",
            "env secret",
            secret_path=tmp_path / "missing",
        )
        == "2026-05-19T13:00:00+00:00"
    )


def test_missing_secret_raises(
    monkeypatch: pytest.MonkeyPatch, tmp_path
) -> None:
    monkeypatch.delenv(SECRET_ENV, raising=False)
    with pytest.raises(FileNotFoundError, match="Executive proof secret"):
        OverrideProof.generate(
            "2026-DEL-004",
            "no secret",
            secret_path=tmp_path / "nope",
        )
