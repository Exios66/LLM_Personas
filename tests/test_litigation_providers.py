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
    provider = get_provider("ollama", "llama3", ollama_base_url="http://127.0.0.1:11434")
    assert isinstance(provider, OllamaProvider)
    assert provider.model == "llama3"
    assert provider.base_url == "http://127.0.0.1:11434"


def test_get_provider_lm_studio() -> None:
    provider = get_provider("lm_studio", "local-model", lm_studio_base_url="http://127.0.0.1:1234/v1")
    assert isinstance(provider, OpenAICompatProvider)
    assert provider.model == "local-model"
    assert provider.base_url == "http://127.0.0.1:1234/v1"
    assert provider.api_key == "lm-studio"


def test_get_provider_openrouter_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "anthropic/claude-3.5-sonnet")


def test_get_provider_openrouter_wires_headers_and_extra_body(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
    cfg = {
        "app_attribution": {"http_referer": "https://example.test", "x_title": "Litigation"},
        "provider": {"sort": "price"},
        "user": "court-1",
    }
    provider = get_provider("openrouter", "openai/gpt-4o-mini", openrouter_config=cfg)
    assert isinstance(provider, OpenAICompatProvider)
    assert provider.api_key == "test-key"
    assert provider.default_headers == {
        "HTTP-Referer": "https://example.test",
        "X-Title": "Litigation",
    }
    assert provider.extra_body == {"provider": {"sort": "price"}, "user": "court-1"}


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("anthropic", "claude-3")


def test_openrouter_headers_ignores_non_dict_attribution() -> None:
    assert _openrouter_headers({"app_attribution": "bad"}) == {}


def test_openrouter_extra_body_omits_empty_sections() -> None:
    assert _openrouter_extra_body({}) == {}
    assert _openrouter_extra_body({"provider": "bad", "user": ""}) == {}
