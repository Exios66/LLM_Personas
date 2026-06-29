"""Regression tests for litigation provider factory (Ollama, LM Studio, OpenRouter)."""

from __future__ import annotations

import pytest

from litigation.providers.factory import _openrouter_extra_body, _openrouter_headers, get_provider
from litigation.providers.ollama_provider import OllamaProvider
from litigation.providers.openai_compat_provider import OpenAICompatProvider


def test_get_provider_ollama() -> None:
    p = get_provider("ollama", "llama3.2", ollama_base_url="http://127.0.0.1:11434")
    assert isinstance(p, OllamaProvider)
    assert p.model == "llama3.2"
    assert p.base_url == "http://127.0.0.1:11434"


def test_get_provider_lm_studio() -> None:
    p = get_provider("lm_studio", "local-model", lm_studio_base_url="http://localhost:9999/v1")
    assert isinstance(p, OpenAICompatProvider)
    assert p.model == "local-model"
    assert p.base_url == "http://localhost:9999/v1"
    assert p.api_key == "lm-studio"


def test_get_provider_openrouter_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_provider("openrouter", "qwen/qwen3:free")


def test_get_provider_openrouter_builds_headers_and_extra_body(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test-key")
    cfg = {
        "app_attribution": {"http_referer": "https://example.test", "x_title": "MORNINGSTAR"},
        "provider": {"sort": "price", "allow_fallbacks": True},
        "user": "court-session-1",
    }
    p = get_provider("openrouter", "meta-llama/llama-3:free", openrouter_config=cfg)
    assert isinstance(p, OpenAICompatProvider)
    assert p.api_key == "sk-test-key"
    assert p.default_headers == {
        "HTTP-Referer": "https://example.test",
        "X-Title": "MORNINGSTAR",
    }
    assert p.extra_body == {
        "provider": {"sort": "price", "allow_fallbacks": True},
        "user": "court-session-1",
    }


def test_openrouter_headers_ignores_non_dict_attribution() -> None:
    assert _openrouter_headers({"app_attribution": "bad"}) == {}


def test_openrouter_extra_body_omits_empty_provider() -> None:
    assert _openrouter_extra_body({}) == {}
    assert _openrouter_extra_body({"provider": "not-a-dict"}) == {}


def test_get_provider_unknown_raises() -> None:
    with pytest.raises(ValueError, match="Unknown provider"):
        get_provider("anthropic", "claude-3")
