"""Regression tests for litigation LLM provider factory helpers."""

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
            "http_referer": "https://example.com",
            "x_title": "Morningstar",
        }
    }
    assert _openrouter_headers(cfg) == {
        "HTTP-Referer": "https://example.com",
        "X-Title": "Morningstar",
    }


def test_openrouter_extra_body_provider_and_user() -> None:
    cfg = {"provider": {"order": ["anthropic"]}, "user": "court-1"}
    body = _openrouter_extra_body(cfg)
    assert body["provider"] == {"order": ["anthropic"]}
    assert body["user"] == "court-1"


def test_get_provider_openrouter_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "anthropic/claude-3-haiku")


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("not-a-provider", "model")
