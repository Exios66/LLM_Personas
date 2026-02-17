"""Courtroom litigation prompts — loads and assembles MORNINGSTAR framework."""

from .assembler import (
    build_deliberation_prompts,
    build_deliberation_user_prompt,
    load_morningstar_system_prompt,
)
from .loader import FrameworkLoader

__all__ = [
    "FrameworkLoader",
    "build_deliberation_prompts",
    "build_deliberation_user_prompt",
    "load_morningstar_system_prompt",
]
