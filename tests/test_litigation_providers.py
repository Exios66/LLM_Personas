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


def test_openrouter_headers_from_app_attribution() -> None:
    cfg = {
        "app_attribution": {
            "http_referer": "https://example.test",
            "x_title": "MORNINGSTAR",
        }
    }
    assert _openrouter_headers(cfg) == {
        "HTTP-Referer": "https://example.test",
        "X-Title": "MORNINGSTAR",
    }


def test_openrouter_extra_body_includes_provider_prefs() -> None:
    cfg = {"provider": {"order": ["Together"]}, "user": "court-1"}
    body = _openrouter_extra_body(cfg)
    assert body["provider"] == {"order": ["Together"]}
    assert body["user"] == "court-1"


def test_get_provider_ollama() -> None:
    p = get_provider("ollama", "llama3", ollama_base_url="http://127.0.0.1:11434")
    assert isinstance(p, OllamaProvider)


def test_get_provider_openrouter_requires_api_key(monkeypatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "org/model:free")


def test_get_provider_openrouter_with_key(monkeypatch) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test")
    p = get_provider(
        "openrouter",
        "org/model:free",
        openrouter_config={"app_attribution": {"x_title": "Test"}},
    )
    assert isinstance(p, OpenAICompatProvider)


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("not-a-provider", "m")
