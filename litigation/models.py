"""OpenRouter model list and selection (interactive or slot machine)."""

import random
import sys
import time

# OpenRouter models available for selection (free tier only — :free suffix required)
OPENROUTER_MODELS = [
    "arcee-ai/trinity-large-preview:free",
    "nvidia/nemotron-nano-9b-v2:free",
    "qwen/qwen3-next-80b-a3b-instruct:free",
    "openai/gpt-oss-20b:free",
    "z-ai/glm-4.5-air:free",
]


def _free_only(models):
    """Filter to free-tier models only (avoids insufficient funds)."""
    return [m for m in models if ":free" in m] or OPENROUTER_MODELS


def select_model_interactive(models=None):
    """
    Prompt user to select a model from the list.
    Returns the selected model string.
    """
    models = _free_only(models or OPENROUTER_MODELS)
    print("\n  OpenRouter models (free tier):", file=sys.stderr)
    print("  " + "-" * 50, file=sys.stderr)
    for i, m in enumerate(models, 1):
        short = m.split("/")[-1].replace(":free", "") if "/" in m else m
        print(f"    {i}. {short}", file=sys.stderr)
    print(f"    0. Random (slot machine)", file=sys.stderr)
    print("", file=sys.stderr)
    while True:
        try:
            choice = input(f"  Select [1-{len(models)} or 0 for random]: ").strip()
            if not choice:
                return select_model_spin(models)
            n = int(choice)
            if n == 0:
                return select_model_spin(models)
            if 1 <= n <= len(models):
                model = models[n - 1]
                print(f"\n  Selected: {model}", file=sys.stderr)
                return model
        except ValueError:
            pass
        print("  Invalid. Enter a number from the list.", file=sys.stderr)


def _short_model(m: str) -> str:
    """Short display name for model."""
    return m.split("/")[-1].replace(":free", "") if "/" in m else m[:45]


def select_model_spin(models=None):
    """
    Slot machine animation: cycle through random models, slow down, land on one.
    Returns the selected model string.
    """
    models = _free_only(models or OPENROUTER_MODELS)
    model = random.choice(models)
    width = 50
    spins = 12
    for i in range(spins):
        display = random.choice(models)
        print("\r  [ {} ]".format(_short_model(display)[:width].ljust(width)), end="", file=sys.stderr)
        sys.stderr.flush()
        delay = 0.05 + (i / spins) * 0.25
        time.sleep(delay)
    print("\r  [ {} ]".format(_short_model(model)[:width].ljust(width)), file=sys.stderr)
    print("\n  Selected: {}".format(model), file=sys.stderr)
    return model
