"""Ollama provider for local LLM inference."""

from .base import BaseProvider, ProviderError


class OllamaProvider(BaseProvider):
    """Provider for Ollama (local LLMs)."""

    def __init__(self, model: str, base_url: str = "http://localhost:11434"):
        self.model = model
        self.base_url = base_url.rstrip("/")

    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 2048,
        temperature: float = 0.7,
    ) -> str:
        try:
            from ollama import Client

            client = Client(host=self.base_url)
            response = client.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                options={
                    "num_predict": max_tokens,
                    "temperature": temperature,
                },
            )
            msg = response.get("message")
            if msg is None:
                raise ProviderError("Ollama returned no message")
            return msg.get("content", "")
        except ImportError as e:
            raise ProviderError(
                "ollama package not installed. Run: pip install ollama"
            ) from e
        except Exception as e:
            raise ProviderError(f"Ollama request failed: {e}") from e
