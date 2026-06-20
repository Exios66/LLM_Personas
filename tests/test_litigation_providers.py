"""Regression tests for litigation LLM provider factory."""

from __future__ import annotations

import os

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


def test_get_provider_openrouter_uses_env_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test-key")
    provider = get_provider("openrouter", "anthropic/claude-3.5-sonnet")
    assert isinstance(provider, OpenAICompatProvider)
    assert provider.api_key == "sk-test-key"
    assert provider.base_url == "https://openrouter.ai/api/v1"


def test_get_provider_openrouter_missing_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "anthropic/claude-3.5-sonnet")


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("azure", "gpt-4")


def test_openrouter_headers_from_config() -> None:
    cfg = {
        "app_attribution": {
            "http_referer": "https://example.com",
            "x_title": "Morningstar Court",
        }
    }
    headers = _openrouter_headers(cfg)
    assert headers == {
        "HTTP-Referer": "https://example.com",
        "X-Title": "Morningstar Court",
    }


def test_openrouter_extra_body_from_config() -> None:
    cfg = {
        "provider": {"sort": "price", "allow_fallbacks": False},
        "user": "court-session-42",
    }
    body = _openrouter_extra_body(cfg)
    assert body == {
        "provider": {"sort": "price", "allow_fallbacks": False},
        "user": "court-session-42",
    }


def test_get_provider_openrouter_passes_headers_and_extra_body(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test")
    cfg = {
        "app_attribution": {"http_referer": "https://court.test", "x_title": "Litigation"},
        "provider": {"sort": "throughput"},
        "user": "run-1",
    }
    provider = get_provider(
        " OpenRouter ",
        "openai/gpt-4o",
        openrouter_api_key=os.environ["OPENROUTER_API_KEY"],
        openrouter_config=cfg,
    )
    assert provider.default_headers == {
        "HTTP-Referer": "https://court.test",
        "X-Title": "Litigation",
    }
    assert provider.extra_body == {
        "provider": {"sort": "throughput"},
        "user": "run-1",
    }
