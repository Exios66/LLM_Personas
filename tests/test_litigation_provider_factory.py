"""Tests for litigation provider factory OpenRouter config helpers."""

from __future__ import annotations

import pytest

from litigation.providers.factory import (
    _openrouter_extra_body,
    _openrouter_headers,
    get_provider,
)


def test_openrouter_headers_from_attribution() -> None:
    cfg = {
        "app_attribution": {
            "http_referer": "https://example.test/app",
            "x_title": "Morningstar Litigation",
        }
    }
    assert _openrouter_headers(cfg) == {
        "HTTP-Referer": "https://example.test/app",
        "X-Title": "Morningstar Litigation",
    }


def test_openrouter_headers_ignores_non_dict_attribution() -> None:
    assert _openrouter_headers({"app_attribution": "bad"}) == {}


def test_openrouter_extra_body_provider_and_user() -> None:
    cfg = {
        "provider": {"order": ["openai"], "allow_fallbacks": False},
        "user": "matter-99",
    }
    body = _openrouter_extra_body(cfg)
    assert body["provider"] == {"order": ["openai"], "allow_fallbacks": False}
    assert body["user"] == "matter-99"


def test_get_provider_openrouter_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "org/model:free")


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("not-a-provider", "m")
