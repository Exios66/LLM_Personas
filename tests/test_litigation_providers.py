"""Regression tests for litigation provider factory selection and OpenRouter config."""

from __future__ import annotations

import pytest

from litigation.providers.factory import get_provider
from litigation.providers.ollama_provider import OllamaProvider
from litigation.providers.openai_compat_provider import OpenAICompatProvider


def test_get_provider_ollama() -> None:
    p = get_provider("ollama", "llama3.2", ollama_base_url="http://host:11434")
    assert isinstance(p, OllamaProvider)
    assert p.model == "llama3.2"
    assert p.base_url == "http://host:11434"


def test_get_provider_lm_studio() -> None:
    p = get_provider("lm_studio", "local-model", lm_studio_base_url="http://127.0.0.1:1234/v1")
    assert isinstance(p, OpenAICompatProvider)
    assert p.model == "local-model"
    assert p.base_url == "http://127.0.0.1:1234/v1"
    assert p.api_key == "lm-studio"


def test_get_provider_openrouter_with_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    cfg = {
        "app_attribution": {"http_referer": "https://example.com", "x_title": "TestApp"},
        "provider": {"sort": "price"},
        "user": "user-42",
    }
    p = get_provider(
        "openrouter",
        "anthropic/claude-3.5-sonnet",
        openrouter_api_key="sk-test",
        openrouter_config=cfg,
    )
    assert isinstance(p, OpenAICompatProvider)
    assert p.api_key == "sk-test"
    assert p.base_url == "https://openrouter.ai/api/v1"
    assert p.default_headers == {"HTTP-Referer": "https://example.com", "X-Title": "TestApp"}
    assert p.extra_body == {"provider": {"sort": "price"}, "user": "user-42"}


def test_get_provider_openrouter_uses_env_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "env-key")
    p = get_provider("openrouter", "openai/gpt-4o-mini")
    assert isinstance(p, OpenAICompatProvider)
    assert p.api_key == "env-key"


def test_get_provider_openrouter_missing_key_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "openai/gpt-4o-mini")


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("anthropic_direct", "claude-3")
