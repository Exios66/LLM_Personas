"""OpenAI-compatible provider for LM Studio and OpenRouter."""

from typing import Any, Optional

from .base import BaseProvider, ProviderError


class OpenAICompatProvider(BaseProvider):
    """
    Provider for OpenAI-compatible APIs:
    - LM Studio (localhost:1234)
    - OpenRouter (openrouter.ai)

    OpenRouter best practices: app attribution headers (HTTP-Referer, X-Title),
    provider routing (sort, allow_fallbacks, etc.). See litigation/OPENROUTER_BEST_PRACTICES.md.
    """

    def __init__(
        self,
        model: str,
        base_url: str,
        api_key: Optional[str] = None,
        *,
        default_headers: Optional[dict[str, str]] = None,
        extra_body: Optional[dict[str, Any]] = None,
    ):
        self.model = model
        # OpenAI client appends /chat/completions to base_url. Use base_url with /v1 for
        # OpenRouter (https://openrouter.ai/api/v1) and LM Studio (http://localhost:1234/v1).
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key or "not-needed"  # LM Studio often accepts any key
        self.default_headers = default_headers or {}
        self.extra_body = extra_body or {}

    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 2048,
        temperature: float = 0.7,
    ) -> str:
        try:
            from openai import OpenAI

            client = OpenAI(
                base_url=self.base_url,
                api_key=self.api_key,
                default_headers=self.default_headers if self.default_headers else None,
            )
            kwargs: dict[str, Any] = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "max_tokens": max_tokens,
                "temperature": temperature,
            }
            if self.extra_body:
                kwargs["extra_body"] = self.extra_body
            response = client.chat.completions.create(**kwargs)
            if isinstance(response, str):
                raise ProviderError(f"API returned error or unexpected format: {response[:200]}")
            if not hasattr(response, "choices"):
                raise ProviderError(
                    f"Unexpected API response (no choices): {type(response).__name__}. "
                    "Check model name and API status."
                )
            choice = response.choices[0] if response.choices else None
            if choice is None:
                raise ProviderError("OpenAI-compat API returned no choices")
            return choice.message.content or ""
        except ImportError as e:
            raise ProviderError(
                "openai package not installed. Run: pip install openai"
            ) from e
        except Exception as e:
            raise ProviderError(f"OpenAI-compat request failed: {e}") from e
