"""Tests for litigation LLM provider factory and OpenRouter config helpers."""

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


def test_openrouter_headers_from_app_attribution() -> None:
    cfg = {
        "app_attribution": {
            "http_referer": "https://example.test/app",
            "x_title": "MORNINGSTAR",
        }
    }
    assert _openrouter_headers(cfg) == {
        "HTTP-Referer": "https://example.test/app",
        "X-Title": "MORNINGSTAR",
    }


def test_openrouter_extra_body_provider_prefs_and_user() -> None:
    cfg = {
        "provider": {"sort": "price", "allow_fallbacks": True},
        "user": "court-session-1",
    }
    body = _openrouter_extra_body(cfg)
    assert body["provider"] == {"sort": "price", "allow_fallbacks": True}
    assert body["user"] == "court-session-1"


def test_get_provider_ollama() -> None:
    p = get_provider("ollama", "llama3", ollama_base_url="http://127.0.0.1:11434")
    assert isinstance(p, OllamaProvider)
    assert p.model == "llama3"


def test_get_provider_openrouter_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "meta-llama/model:free")


def test_get_provider_openrouter_passes_attribution(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test")
    cfg = {
        "app_attribution": {"http_referer": "https://court.test", "x_title": "Court"},
        "provider": {"sort": "throughput"},
    }
    p = get_provider("openrouter", "org/model:free", openrouter_config=cfg)
    assert isinstance(p, OpenAICompatProvider)
    assert p.default_headers["HTTP-Referer"] == "https://court.test"
    assert p.extra_body["provider"] == {"sort": "throughput"}


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("azure", "gpt-4")
