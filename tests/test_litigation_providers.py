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
    provider = get_provider("ollama", "llama3.2", ollama_base_url="http://localhost:11434")
    assert isinstance(provider, OllamaProvider)
    assert provider.model == "llama3.2"
    assert provider.base_url == "http://localhost:11434"


def test_get_provider_lm_studio() -> None:
    provider = get_provider("lm_studio", "local-model", lm_studio_base_url="http://localhost:1234/v1")
    assert isinstance(provider, OpenAICompatProvider)
    assert provider.model == "local-model"
    assert provider.base_url == "http://localhost:1234/v1"
    assert provider.api_key == "lm-studio"


def test_get_provider_openrouter_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "openai/gpt-4o-mini")


def test_get_provider_openrouter_with_env_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test-key")
    provider = get_provider("openrouter", "openai/gpt-4o-mini")
    assert isinstance(provider, OpenAICompatProvider)
    assert provider.api_key == "sk-or-test-key"
    assert provider.base_url == "https://openrouter.ai/api/v1"


def test_get_provider_openrouter_headers_and_extra_body(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-or-test-key")
    cfg = {
        "app_attribution": {"http_referer": "https://example.com", "x_title": "MORNINGSTAR"},
        "provider": {"sort": "price"},
        "user": "court-session-1",
    }
    provider = get_provider("openrouter", "model", openrouter_config=cfg)
    assert provider.default_headers == {
        "HTTP-Referer": "https://example.com",
        "X-Title": "MORNINGSTAR",
    }
    assert provider.extra_body == {"provider": {"sort": "price"}, "user": "court-session-1"}


def test_openrouter_headers_skips_non_dict_attribution() -> None:
    assert _openrouter_headers({"app_attribution": "invalid"}) == {}


def test_openrouter_extra_body_empty_when_no_prefs() -> None:
    assert _openrouter_extra_body({}) == {}
    assert _openrouter_extra_body({"provider": "not-a-dict"}) == {}


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("anthropic", "claude-3")
