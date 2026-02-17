"""OpenRouter model list and selection (interactive or slot machine)."""

import random
import sys
import time

# OpenRouter models available for selection
OPENROUTER_MODELS = [
    "arcee-ai/trinity-large-preview:free",
    "nvidia/nemotron-nano-9b-v2:free",
    "qwen/qwen3-next-80b-a3b-instruct:free",
    "openai/gpt-oss-20b:free",
    "z-ai/glm-4.5-air:free",
    "qwen/qwen3-235b-a22b-thinking-2507",
]


def select_model_interactive(models=None):
    """
    Prompt user to select a model from the list.
    Returns the selected model string.
    """
    models = models or OPENROUTER_MODELS
    print("\nOpenRouter models:", file=sys.stderr)
    for i, m in enumerate(models, 1):
        print(f"  {i}. {m}", file=sys.stderr)
    print("  0. Random (slot machine)", file=sys.stderr)
    print("", file=sys.stderr)
    while True:
        try:
            choice = input("Select model [1-{}] (or 0 for random): ".format(len(models))).strip()
            if not choice:
                return select_model_spin(models)
            n = int(choice)
            if n == 0:
                return select_model_spin(models)
            if 1 <= n <= len(models):
                model = models[n - 1]
                print("\nSelected: {}".format(model), file=sys.stderr)
                return model
        except ValueError:
            pass
        print("Invalid choice. Try again.", file=sys.stderr)


def select_model_spin(models=None):
    """
    Slot machine animation: cycle through random models, slow down, land on one.
    Returns the selected model string.
    """
    models = models or OPENROUTER_MODELS
    model = random.choice(models)
    # Spin: show random models cycling, slowing down
    spins = 14
    for i in range(spins):
        display = random.choice(models)
        print("\r  [ {} ]".format(display[:60].ljust(60)), end="", file=sys.stderr)
        sys.stderr.flush()
        # Slow down as we approach the end
        delay = 0.04 + (i / spins) * 0.3
        time.sleep(delay)
    print("\r  [ {} ]".format(model[:60].ljust(60)), file=sys.stderr)
    print("\n  Selected: {}".format(model), file=sys.stderr)
    return model
