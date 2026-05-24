"""Regression tests for litigation LLM provider factory (OpenRouter config)."""

from __future__ import annotations

import pytest

from litigation.providers.factory import (
    _openrouter_extra_body,
    _openrouter_headers,
    get_provider,
)
from litigation.providers.ollama_provider import OllamaProvider
from litigation.providers.openai_compat_provider import OpenAICompatProvider


def test_openrouter_headers_from_app_attribution() -> None:
    cfg = {
        "app_attribution": {
            "http_referer": "https://example.com/app",
            "x_title": "Morningstar",
        }
    }
    assert _openrouter_headers(cfg) == {
        "HTTP-Referer": "https://example.com/app",
        "X-Title": "Morningstar",
    }


def test_openrouter_headers_empty_when_attribution_missing() -> None:
    assert _openrouter_headers({}) == {}
    assert _openrouter_headers({"app_attribution": "not-a-dict"}) == {}


def test_openrouter_extra_body_provider_and_user() -> None:
    cfg = {
        "provider": {"order": ["Together"]},
        "user": "session-abc",
    }
    body = _openrouter_extra_body(cfg)
    assert body["provider"] == {"order": ["Together"]}
    assert body["user"] == "session-abc"


def test_get_provider_ollama() -> None:
    p = get_provider("ollama", "llama3", ollama_base_url="http://127.0.0.1:11434")
    assert isinstance(p, OllamaProvider)


def test_get_provider_openrouter_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "meta-llama/llama-3.2-3b-instruct:free")


def test_get_provider_openrouter_passes_headers_and_extra_body(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test")
    cfg = {
        "app_attribution": {"http_referer": "https://repo.test", "x_title": "Test"},
        "provider": {"allow_fallbacks": False},
        "user": "u1",
    }
    p = get_provider("openrouter", "org/model:free", openrouter_config=cfg)
    assert isinstance(p, OpenAICompatProvider)
    assert p.default_headers == {
        "HTTP-Referer": "https://repo.test",
        "X-Title": "Test",
    }
    assert p.extra_body == {"provider": {"allow_fallbacks": False}, "user": "u1"}


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("anthropic", "claude")
