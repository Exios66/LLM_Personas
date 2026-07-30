"""Regression tests for litigation LLM provider factory."""

from __future__ import annotations

import pytest

from litigation.providers import get_provider
from litigation.providers.factory import _openrouter_extra_body, _openrouter_headers
from litigation.providers.ollama_provider import OllamaProvider
from litigation.providers.openai_compat_provider import OpenAICompatProvider


def test_get_provider_ollama() -> None:
    p = get_provider("ollama", "llama3.2", ollama_base_url="http://127.0.0.1:11434")
    assert isinstance(p, OllamaProvider)
    assert p.model == "llama3.2"
    assert p.base_url == "http://127.0.0.1:11434"


def test_get_provider_lm_studio() -> None:
    p = get_provider("lm_studio", "local-model", lm_studio_base_url="http://127.0.0.1:1234/v1")
    assert isinstance(p, OpenAICompatProvider)
    assert p.model == "local-model"
    assert p.base_url == "http://127.0.0.1:1234/v1"
    assert p.api_key == "lm-studio"


def test_get_provider_openrouter_uses_env_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test-key")
    p = get_provider("openrouter", "anthropic/claude-3.5-sonnet")
    assert isinstance(p, OpenAICompatProvider)
    assert p.api_key == "sk-test-key"
    assert p.base_url == "https://openrouter.ai/api/v1"


def test_get_provider_openrouter_missing_key_raises(monkeypatch: pytest.MonkeyPatch) -> None:
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
    assert _openrouter_headers(cfg) == {
        "HTTP-Referer": "https://example.com",
        "X-Title": "Morningstar Court",
    }


def test_openrouter_extra_body_from_config() -> None:
    cfg = {
        "provider": {"sort": "price"},
        "user": "court-session-1",
    }
    assert _openrouter_extra_body(cfg) == {
        "provider": {"sort": "price"},
        "user": "court-session-1",
    }


def test_get_provider_openrouter_passes_headers_and_extra_body(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test")
    cfg = {
        "app_attribution": {"http_referer": "https://court.test", "x_title": "Litigation"},
        "provider": {"allow_fallbacks": False},
        "user": "u1",
    }
    p = get_provider("openrouter", "openai/gpt-4o", openrouter_config=cfg)
    assert p.default_headers == {"HTTP-Referer": "https://court.test", "X-Title": "Litigation"}
    assert p.extra_body == {"provider": {"allow_fallbacks": False}, "user": "u1"}
