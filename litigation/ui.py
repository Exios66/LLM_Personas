"""Terminal UI helpers for the litigation runner — menus, prompts, and navigation."""

import sys
from typing import Callable, List, Optional, Tuple


def _out(msg: str = "", file=None) -> None:
    """Print to stderr by default (so stdout stays clean for transcript output)."""
    (file or sys.stderr).write(msg + "\n")
    (file or sys.stderr).flush()


def _in(prompt: str = "") -> str:
    """Read line from stdin."""
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        _out("\nCancelled.")
        sys.exit(0)


def section(title: str, width: int = 60) -> None:
    """Print a clear section header."""
    _out()
    _out("═" * width)
    _out(f"  {title}")
    _out("═" * width)


def sub_section(title: str, width: int = 60) -> None:
    """Print a subsection header."""
    _out()
    _out(f"── {title} ──")


def menu(
    title: str,
    choices: List[Tuple[str, str]],
    *,
    prompt: str = "Choice",
    default: Optional[int] = None,
) -> int:
    """
    Display a numbered menu and return the selected index (0-based).
    choices: list of (label, description) or (label,) tuples.
    """
    _out()
    _out(f"  {title}")
    _out()
    for i, item in enumerate([tuple[str, str] for tuple in choices], 1):
        label = tuple[0]
        desc = tuple[1] if len(tuple) > 1 else ""
        if desc:
            _out(f"    {i}. {label}")
            _out(f"       {desc}")
        else:
            _out(f"    {i}. {label}")
    _out()
    default_hint = f" (default: {default})" if default is not None else ""
    while True:
        try:
            raw = _in(f"  {prompt} [1-{len(choices)}]{default_hint}: ").strip()
            if not raw and default is not None:
                return default - 1
            n = int(raw)
            if 1 <= n <= len(choices):
                return n - 1
        except ValueError:
            pass
        _out("  Invalid. Enter a number from the list.")


def prompt_text(
    label: str,
    *,
    default: str = "",
    required: bool = True,
    multiline: bool = False,
) -> str:
    """Prompt for text input. Returns trimmed string."""
    _out()
    _out(f"  {label}")
    if default:
        _out(f"  [default: {default}]")
    if multiline:
        _out("  (Enter a blank line when done)")
    _out()
    if multiline:
        lines = []
        while True:
            line = _in("  > " if not lines else "  … ")
            if not line:
                if lines:
                    break
                if not required:
                    return default
                _out("  Please enter at least one line.")
                continue
            lines.append(line)
        return "\n".join(lines)
    else:
        val = _in("  > ")
        if not val:
            if default:
                return default
            if required:
                _out("  This field is required.")
                return prompt_text(label, default=default, required=required, multiline=multiline)
        return val or default


def confirm(message: str, default: bool = True) -> bool:
    """Ask yes/no. Returns True for yes, False for no."""
    hint = "Y/n" if default else "y/N"
    while True:
        raw = _in(f"  {message} [{hint}]: ").strip().lower()
        if not raw:
            return default
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        _out("  Enter y or n.")


def show_summary(items: List[Tuple[str, str]]) -> None:
    """Display a key-value summary before running."""
    _out()
    _out("  Current settings:")
    for k, v in items:
        _out(f"    • {k}: {v}")
    _out()


def divider(width: int = 60) -> None:
    """Print a simple divider."""
    _out("-" * width)


def interactive_main_menu(
    config: dict,
    providers: List[str],
    hearing_types: List[Tuple[str, str]],
) -> Optional[dict]:
    """
    Show main menu and return run parameters, or None to exit.
    Returns dict with: matter, provider, model, feasibility, hearing_type, no_spectators, save_location
    """
    section("MORNINGSTAR Court — Litigation Runner")

    choices = [
        ("Quick run", "Enter matter + optional configure (all CLI options available)"),
        ("Full run", "Configure: provider, model, feasibility, hearing-type, spectators, save"),
        ("Help", "Show all command-line options"),
        ("Exit", "Quit"),
    ]
    idx = menu("What would you like to do?", choices, default=1)

    if idx == 2:  # Help
        _out()
        _out("  Command-line usage:")
        _out("    python litigation/run.py [MATTER] [OPTIONS]")
        _out()
        _out("  Options (all available in Full run / Configure):")
        _out("    -f, --feasibility F0-F5   Feasibility level (default: F3)")
        _out("    --provider NAME           ollama | lm_studio | openrouter")
        _out("    --model NAME              Override model (e.g. llama3.2, openai/gpt-4o)")
        _out("    --model-select            [OpenRouter] Pick model from list (interactive)")
        _out("    --model-spin              [OpenRouter] Slot machine: random from list (default)")
        _out("    --hearing-type TYPE       standard | expedited | special_inquiry | contempt")
        _out("    --no-spectators           Exclude spectator commentary")
        _out("    --no-save                  Don't save transcript")
        _out("    --menu                    Show this interactive menu")
        _out()
        _out("  Examples:")
        _out('    python litigation/run.py "Should we adopt a new API convention?"')
        _out("    python litigation/run.py --hearing-type expedited -f F2")
        _out("    python litigation/run.py --provider ollama --model llama3.2")
        _out("    python litigation/run.py --menu")
        _out()
        return interactive_main_menu(config, providers, hearing_types)  # Show menu again

    if idx == 3:  # Exit
        return None

    provider_name = config.get("provider", "openrouter")
    feasibility = "F3"
    hearing_type = "standard"
    no_spectators = False
    save_location = "litigation"  # default: litigation/transcripts/
    model = None

    if idx == 0:  # Quick run
        sub_section("Enter the matter for the court to deliberate")
        _out("  (Press Enter alone to return to menu)")
        matter = prompt_text("Matter", required=False)
        if not matter:
            return interactive_main_menu(config, providers, hearing_types)
        if confirm("Configure options (provider, model, feasibility, hearing type, etc.)?", default=False):
            return _run_config_flow(config, providers, hearing_types, matter, provider_name)
        return {
            "matter": matter,
            "provider": provider_name,
            "model": model,
            "feasibility": feasibility,
            "hearing_type": hearing_type,
            "no_spectators": no_spectators,
            "save_location": save_location,
        }

    # idx == 1: Full run
    sub_section("Matter")
    _out("  (Press Enter alone to return to menu)")
    matter = prompt_text("Matter for the court to deliberate", required=False)
    if not matter:
        return interactive_main_menu(config, providers, hearing_types)

    return _run_config_flow(config, providers, hearing_types, matter, provider_name)


def _run_config_flow(
    config: dict,
    providers: List[str],
    hearing_types: List[Tuple[str, str]],
    matter: str,
    provider_name: str,
) -> Optional[dict]:
    """Run through provider, model, feasibility, hearing type, spectators, save. Returns params dict."""
    sub_section("Provider")
    provider_choices = [(p, "") for p in providers]
    pidx = menu("Select provider", provider_choices, default=(providers.index(provider_name) + 1) if provider_name in providers else 1)
    provider_name = providers[pidx]

    model = None
    if provider_name == "openrouter":
        sub_section("Model (OpenRouter)")
        model_choices = [
            ("Random (slot machine)", "Let the court choose (--model-spin)"),
            ("Select from list", "Pick from list (--model-select)"),
            ("Enter model name", "Override with specific model (e.g. openai/gpt-4o)"),
        ]
        midx = menu("Model selection", model_choices, default=1)
        if midx == 0:
            from litigation.models import select_model_spin, OPENROUTER_MODELS
            models = config.get("openrouter", {}).get("models") or OPENROUTER_MODELS
            model = select_model_spin(models)
        elif midx == 1:
            from litigation.models import select_model_interactive, OPENROUTER_MODELS
            models = config.get("openrouter", {}).get("models") or OPENROUTER_MODELS
            model = select_model_interactive(models)
        else:
            model = prompt_text("Model name (e.g. openai/gpt-4o, nvidia/nemotron-nano-9b-v2:free)", default="", required=False)
            if not model:
                from litigation.models import select_model_spin, OPENROUTER_MODELS
                models = config.get("openrouter", {}).get("models") or OPENROUTER_MODELS
                model = select_model_spin(models)
    else:
        prov_cfg = config.get(provider_name, {}) or {}
        model = prov_cfg.get("model") or ("llama3.2" if provider_name == "ollama" else "")
        if provider_name == "lm_studio" and not model:
            model = prompt_text("LM Studio model name", default="", required=False)
        elif not model:
            model = prompt_text("Model name", default="llama3.2", required=False) or "llama3.2"

    sub_section("Feasibility")
    f_choices = [
        ("F0", "Trivial — no deliberation"),
        ("F1", "Simple — optional"),
        ("F2", "Moderate — recommended"),
        ("F3", "Complex — mandatory (default)"),
        ("F4", "Critical — mandatory + transcript"),
        ("F5", "Existential — full record"),
    ]
    fidx = menu("Feasibility level", f_choices, default=4)
    feasibility = f"F{fidx}"

    sub_section("Hearing type")
    ht_choices = [(t[0], t[1]) for t in hearing_types]
    hidx = menu("Hearing type", ht_choices, default=1)
    hearing_type = hearing_types[hidx][0]

    no_spectators = not confirm("Include spectators (Dr. Echo, Dr. Harley, Uncle Ruckus)?", default=True)

    sub_section("Save transcript")
    save_choices = [
        ("litigation/transcripts/ (local, default)", "Save to litigation runner directory"),
        ("courtroom/transcripts/", "Save to main courtroom transcripts"),
        ("Don't save", "No transcript file"),
    ]
    sidx = menu("Where to save transcript?", save_choices, default=1)
    save_location = "litigation" if sidx == 0 else ("courtroom" if sidx == 1 else None)

    show_summary([
        ("Matter", matter[:50] + ("..." if len(matter) > 50 else "")),
        ("Provider", provider_name),
        ("Model", model or "(from config)"),
        ("Feasibility", feasibility),
        ("Hearing type", hearing_type),
        ("Spectators", "No" if no_spectators else "Yes"),
        ("Save transcript", ("litigation/transcripts/" if save_location == "litigation" else "courtroom/transcripts/") if save_location else "No"),
    ])

    if not confirm("Proceed with deliberation?", default=True):
        return interactive_main_menu(config, providers, hearing_types)

    return {
        "matter": matter,
        "provider": provider_name,
        "model": model,
        "feasibility": feasibility,
        "hearing_type": hearing_type,
        "no_spectators": no_spectators,
        "save_location": save_location,
    }
