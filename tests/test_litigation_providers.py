"""Regression tests for litigation LLM provider factory."""

from __future__ import annotations

import pytest

from litigation.providers.factory import (
    _openrouter_extra_body,
    _openrouter_headers,
    get_provider,
)
from litigation.providers.ollama_provider import OllamaProvider
from litigation.providers.openai_compat_provider import OpenAICompatProvider


def test_get_provider_ollama() -> None:
    provider = get_provider("ollama", "llama3", ollama_base_url="http://localhost:11434")
    assert isinstance(provider, OllamaProvider)
    assert provider.model == "llama3"
    assert provider.base_url == "http://localhost:11434"


def test_get_provider_lm_studio() -> None:
    provider = get_provider("lm_studio", "local-model")
    assert isinstance(provider, OpenAICompatProvider)
    assert provider.model == "local-model"
    assert provider.api_key == "lm-studio"
    assert provider.base_url == "http://localhost:1234/v1"


def test_get_provider_openrouter_with_config(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
    cfg = {
        "app_attribution": {"http_referer": "https://example.com", "x_title": "Court App"},
        "provider": {"sort": "price"},
        "user": "uid-42",
    }
    provider = get_provider("openrouter", "anthropic/claude", openrouter_config=cfg)
    assert isinstance(provider, OpenAICompatProvider)
    assert provider.api_key == "test-key"
    assert provider.default_headers["HTTP-Referer"] == "https://example.com"
    assert provider.default_headers["X-Title"] == "Court App"
    assert provider.extra_body["provider"] == {"sort": "price"}
    assert provider.extra_body["user"] == "uid-42"


def test_get_provider_openrouter_missing_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "model")


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("azure", "model")


def test_openrouter_headers_skips_invalid_attribution() -> None:
    assert _openrouter_headers({"app_attribution": "not-a-dict"}) == {}


def test_openrouter_extra_body_skips_empty_provider_prefs() -> None:
    assert _openrouter_extra_body({"provider": {}}) == {}
    assert _openrouter_extra_body({"user": ""}) == {}
