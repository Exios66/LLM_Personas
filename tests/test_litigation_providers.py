"""Regression tests for litigation LLM provider factory."""

from __future__ import annotations

import pytest

from litigation.providers.factory import get_provider
from litigation.providers.ollama_provider import OllamaProvider
from litigation.providers.openai_compat_provider import OpenAICompatProvider


def test_get_provider_ollama() -> None:
    provider = get_provider("ollama", "llama3.2", ollama_base_url="http://127.0.0.1:11434")
    assert isinstance(provider, OllamaProvider)
    assert provider.model == "llama3.2"


def test_get_provider_lm_studio() -> None:
    provider = get_provider("lm_studio", "local-model")
    assert isinstance(provider, OpenAICompatProvider)
    assert provider.api_key == "lm-studio"
    assert provider.model == "local-model"


def test_get_provider_openrouter_missing_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "anthropic/claude-3-haiku")


def test_get_provider_openrouter_with_env_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test-key")
    provider = get_provider(
        "openrouter",
        "meta-llama/llama-3.2-3b-instruct",
        openrouter_config={
            "app_attribution": {
                "http_referer": "https://example.com",
                "x_title": "MORNINGSTAR",
            },
            "provider": {"sort": "price"},
            "user": "court-session-1",
        },
    )
    assert isinstance(provider, OpenAICompatProvider)
    assert provider.api_key == "sk-or-test-key"
    assert provider.default_headers == {
        "HTTP-Referer": "https://example.com",
        "X-Title": "MORNINGSTAR",
    }
    assert provider.extra_body == {
        "provider": {"sort": "price"},
        "user": "court-session-1",
    }


def test_get_provider_openrouter_explicit_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    provider = get_provider("openrouter", "model", openrouter_api_key="explicit-key")
    assert provider.api_key == "explicit-key"


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("azure", "gpt-4")


def test_get_provider_normalizes_name() -> None:
    provider = get_provider("  OLLAMA  ", "llama3.2")
    assert isinstance(provider, OllamaProvider)
