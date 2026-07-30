"""Tests for litigation LLM provider factory."""

from __future__ import annotations

import pytest

from litigation.providers.factory import (
    _openrouter_extra_body,
    _openrouter_headers,
    get_provider,
)
from litigation.providers.ollama_provider import OllamaProvider
from litigation.providers.openai_compat_provider import OpenAICompatProvider


def test_openrouter_headers_from_config() -> None:
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


def test_openrouter_headers_empty_when_missing() -> None:
    assert _openrouter_headers({}) == {}
    assert _openrouter_headers({"app_attribution": "not-a-dict"}) == {}


def test_openrouter_extra_body_provider_prefs() -> None:
    cfg = {"provider": {"sort": "price"}, "user": "uid-1"}
    body = _openrouter_extra_body(cfg)
    assert body["provider"] == {"sort": "price"}
    assert body["user"] == "uid-1"


def test_get_provider_ollama() -> None:
    p = get_provider("ollama", "llama3", ollama_base_url="http://host:9999")
    assert isinstance(p, OllamaProvider)
    assert p.model == "llama3"
    assert p.base_url == "http://host:9999"


def test_get_provider_lm_studio() -> None:
    p = get_provider(
        "lm_studio",
        "local-model",
        lm_studio_base_url="http://localhost:9999/v1",
    )
    assert isinstance(p, OpenAICompatProvider)
    assert p.base_url == "http://localhost:9999/v1"
    assert p.api_key == "lm-studio"


def test_get_provider_openrouter_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test")
    p = get_provider(
        "openrouter",
        "anthropic/claude-3",
        openrouter_config={
            "app_attribution": {"http_referer": "https://app.test", "x_title": "Test"},
            "provider": {"allow_fallbacks": False},
            "user": "u1",
        },
    )
    assert isinstance(p, OpenAICompatProvider)
    assert p.api_key == "sk-test"
    assert p.default_headers["HTTP-Referer"] == "https://app.test"
    assert p.extra_body["provider"] == {"allow_fallbacks": False}
    assert p.extra_body["user"] == "u1"


def test_get_provider_openrouter_missing_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "model")


def test_get_provider_unknown() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("azure", "model")
