"""Provider factory for courtroom litigation runner."""

import os
from typing import Any, Optional

from .base import BaseProvider
from .ollama_provider import OllamaProvider
from .openai_compat_provider import OpenAICompatProvider


def _openrouter_headers(openrouter_config: dict) -> dict[str, str]:
    """Build app attribution headers from config. See OPENROUTER_BEST_PRACTICES.md."""
    headers: dict[str, str] = {}
    attr = openrouter_config.get("app_attribution") or {}
    if isinstance(attr, dict):
        if attr.get("http_referer"):
            headers["HTTP-Referer"] = str(attr["http_referer"])
        if attr.get("x_title"):
            headers["X-Title"] = str(attr["x_title"])
    return headers


def _openrouter_extra_body(openrouter_config: dict) -> dict[str, Any]:
    """Build OpenRouter-only request body (provider, user, etc.). See OPENROUTER_BEST_PRACTICES.md."""
    body: dict[str, Any] = {}
    provider_prefs = openrouter_config.get("provider")
    if isinstance(provider_prefs, dict) and provider_prefs:
        body["provider"] = provider_prefs
    user_id = openrouter_config.get("user")
    if user_id:
        body["user"] = str(user_id)
    return body


def get_provider(
    provider: str,
    model: str,
    *,
    ollama_base_url: str = "http://localhost:11434",
    lm_studio_base_url: str = "http://localhost:1234/v1",
    openrouter_base_url: str = "https://openrouter.ai/api/v1",
    openrouter_api_key: Optional[str] = None,
    openrouter_config: Optional[dict] = None,
) -> BaseProvider:
    """
    Create an LLM provider instance.

    Args:
        provider: One of "ollama", "lm_studio", "openrouter".
        model: Model identifier.
        ollama_base_url: Ollama API base URL.
        lm_studio_base_url: LM Studio OpenAI-compat base URL.
        openrouter_base_url: OpenRouter API base URL.
        openrouter_api_key: OpenRouter API key (or OPENROUTER_API_KEY env).

    Returns:
        Configured provider instance.
    """
    provider = provider.lower().strip()

    if provider == "ollama":
        return OllamaProvider(model=model, base_url=ollama_base_url)

    if provider == "lm_studio":
        return OpenAICompatProvider(
            model=model,
            base_url=lm_studio_base_url,
            api_key="lm-studio",  # LM Studio accepts any key
        )

    if provider == "openrouter":
        api_key = openrouter_api_key or os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError(
                "OpenRouter requires OPENROUTER_API_KEY environment variable"
            )
        cfg = openrouter_config or {}
        default_headers = _openrouter_headers(cfg)
        extra_body = _openrouter_extra_body(cfg)
        return OpenAICompatProvider(
            model=model,
            base_url=openrouter_base_url,
            api_key=api_key,
            default_headers=default_headers or None,
            extra_body=extra_body or None,
        )

    raise ValueError(
        f"Unknown provider: {provider}. Use ollama, lm_studio, or openrouter."
    )
