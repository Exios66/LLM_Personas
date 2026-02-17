"""Base provider interface for LLM inference."""

from abc import ABC, abstractmethod


class ProviderError(Exception):
    """Raised when an LLM provider fails."""

    pass


class BaseProvider(ABC):
    """Abstract base for LLM providers."""

    @abstractmethod
    def complete(
        self,
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 2048,
        temperature: float = 0.7,
    ) -> str:
        """
        Generate a completion.

        Args:
            system_prompt: System/instruction prompt.
            user_prompt: User message.
            max_tokens: Maximum tokens to generate.
            temperature: Sampling temperature (0–1).

        Returns:
            Generated text.
        """
        pass
