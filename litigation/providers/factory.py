"""Provider factory for courtroom litigation runner."""

import os
from typing import Optional

from .base import BaseProvider
from .ollama_provider import OllamaProvider
from .openai_compat_provider import OpenAICompatProvider


def get_provider(
    provider: str,
    model: str,
    *,
    ollama_base_url: str = "http://localhost:11434",
    lm_studio_base_url: str = "http://localhost:1234",
    openrouter_base_url: str = "https://openrouter.ai/api",
    openrouter_api_key: Optional[str] = None,
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
        return OpenAICompatProvider(
            model=model,
            base_url=openrouter_base_url,
            api_key=api_key,
        )

    raise ValueError(
        f"Unknown provider: {provider}. Use ollama, lm_studio, or openrouter."
    )
