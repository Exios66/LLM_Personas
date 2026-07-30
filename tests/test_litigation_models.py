"""Regression tests for OpenRouter model list and selection helpers."""

from __future__ import annotations

import pytest

from litigation import models as litigation_models


def test_openrouter_models_are_distinct_repo_ids() -> None:
    """Adjacent string literals without commas silently merge in Python."""
    models = litigation_models.OPENROUTER_MODELS
    assert len(models) >= 10
    assert len(models) == len(set(models))
    for model in models:
        assert "/" in model, f"expected org/repo slug, got {model!r}"
        assert "free" in model or model.startswith("openrouter/")


def test_free_only_filters_paid_entries() -> None:
    mixed = [
        "vendor/model-a:free",
        "vendor/model-b",
        "vendor/model-c:free",
    ]
    assert litigation_models._free_only(mixed) == [
        "vendor/model-a:free",
        "vendor/model-c:free",
    ]


def test_free_only_falls_back_when_no_free_models() -> None:
    assert litigation_models._free_only(["vendor/paid-only"]) == litigation_models.OPENROUTER_MODELS


def test_select_model_spin_returns_member(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pool = ["alpha/model:free", "beta/model:free"]
    monkeypatch.setattr(litigation_models.random, "choice", lambda xs: xs[1])
    monkeypatch.setattr(litigation_models.time, "sleep", lambda _s: None)

    picked = litigation_models.select_model_spin(pool)

    assert picked == "beta/model:free"
