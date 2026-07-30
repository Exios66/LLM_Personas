"""Regression tests for litigation provider factory."""

from __future__ import annotations

import os

import pytest

from litigation.providers.factory import get_provider
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


def test_get_provider_openrouter_with_explicit_key() -> None:
    provider = get_provider(
        "openrouter",
        "anthropic/claude-3.5-sonnet",
        openrouter_api_key="sk-test",
        openrouter_config={
            "app_attribution": {
                "http_referer": "https://example.test",
                "x_title": "Test App",
            },
            "provider": {"sort": "price"},
            "user": "user-42",
        },
    )
    assert isinstance(provider, OpenAICompatProvider)
    assert provider.api_key == "sk-test"
    assert provider.default_headers == {
        "HTTP-Referer": "https://example.test",
        "X-Title": "Test App",
    }
    assert provider.extra_body == {"provider": {"sort": "price"}, "user": "user-42"}


def test_get_provider_openrouter_reads_env_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "env-key")
    provider = get_provider("openrouter", "openai/gpt-4o-mini")
    assert provider.api_key == "env-key"


def test_get_provider_openrouter_missing_key_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "openai/gpt-4o-mini")


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("azure", "gpt-4")
