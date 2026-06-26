"""Litigation LLM provider factory selection and OpenRouter configuration."""

from __future__ import annotations

import pytest

from litigation.providers.factory import get_provider
from litigation.providers.ollama_provider import OllamaProvider
from litigation.providers.openai_compat_provider import OpenAICompatProvider


def test_get_provider_ollama() -> None:
    provider = get_provider("ollama", "llama3.2", ollama_base_url="http://127.0.0.1:11434")
    assert isinstance(provider, OllamaProvider)
    assert provider.model == "llama3.2"
    assert provider.base_url == "http://127.0.0.1:11434"


def test_get_provider_lm_studio() -> None:
    provider = get_provider("lm_studio", "local-model", lm_studio_base_url="http://localhost:1234/v1")
    assert isinstance(provider, OpenAICompatProvider)
    assert provider.model == "local-model"
    assert provider.base_url == "http://localhost:1234/v1"
    assert provider.api_key == "lm-studio"


def test_get_provider_openrouter_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "anthropic/claude-3.5-sonnet")


def test_get_provider_openrouter_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test")
    provider = get_provider("openrouter", "openai/gpt-4o-mini")
    assert isinstance(provider, OpenAICompatProvider)
    assert provider.api_key == "sk-or-test"
    assert provider.base_url == "https://openrouter.ai/api/v1"


def test_get_provider_openrouter_explicit_key_and_config() -> None:
    provider = get_provider(
        "openrouter",
        "anthropic/claude-3.5-sonnet",
        openrouter_api_key="sk-explicit",
        openrouter_config={
            "app_attribution": {
                "http_referer": "https://example.com/app",
                "x_title": "Litigation Runner",
            },
            "provider": {"sort": "price", "allow_fallbacks": True},
            "user": "court-session-1",
        },
    )
    assert provider.api_key == "sk-explicit"
    assert provider.default_headers["HTTP-Referer"] == "https://example.com/app"
    assert provider.default_headers["X-Title"] == "Litigation Runner"
    assert provider.extra_body["provider"] == {"sort": "price", "allow_fallbacks": True}
    assert provider.extra_body["user"] == "court-session-1"


def test_get_provider_normalizes_name() -> None:
    provider = get_provider("  OLLAMA  ", "mistral")
    assert isinstance(provider, OllamaProvider)


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("azure", "gpt-4")
