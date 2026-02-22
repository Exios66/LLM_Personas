#!/usr/bin/env python3
"""
Courtroom Litigation Runner

Run MORNINGSTAR deliberation protocol via Ollama, LM Studio, or OpenRouter.
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Add project root for imports
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

# Load .env from litigation/providers/ (OPENROUTER_API_KEY, etc.)
_env_path = Path(__file__).resolve().parent / "providers" / ".env"
if _env_path.exists():
    try:
        from dotenv import load_dotenv
        load_dotenv(_env_path)
    except ImportError:
        pass  # python-dotenv not installed; rely on system env


def load_config() -> dict:
    """Load config from YAML file."""
    config_path = os.environ.get(
        "LITIGATION_CONFIG",
        REPO_ROOT / "litigation" / "config.yaml",
    )
    path = Path(config_path)
    if not path.exists():
        example = REPO_ROOT / "litigation" / "config.example.yaml"
        if example.exists():
            print(
                f"Config not found at {path}. Copy from config.example.yaml:\n"
                f"  cp litigation/config.example.yaml litigation/config.yaml",
                file=sys.stderr,
            )
        raise SystemExit(1)

    try:
        import yaml

        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception as e:
        print(f"Failed to load config: {e}", file=sys.stderr)
        raise SystemExit(1)


def slugify(text: str) -> str:
    """Create a URL-safe slug from matter text."""
    s = text.lower()[:60]
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-") or "matter"


def save_transcript(matter: str, deliberation: str, *, location: str = "litigation") -> Path:
    """Save transcript to litigation/transcripts/ (default) or courtroom/transcripts/."""
    today = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(matter)
    if location == "courtroom":
        transcripts_dir = REPO_ROOT / "courtroom" / "transcripts"
    else:
        transcripts_dir = Path(__file__).resolve().parent / "transcripts"
    transcripts_dir.mkdir(parents=True, exist_ok=True)

    # Avoid overwriting
    base_name = f"{today}-{slug}"
    path = transcripts_dir / f"{base_name}.md"
    counter = 1
    while path.exists():
        path = transcripts_dir / f"{base_name}-{counter}.md"
        counter += 1

    header = f"""# Transcript: In Re: {matter[:80]}{'...' if len(matter) > 80 else ''}

**Case No.:** {datetime.now().strftime('%Y')}-DEL-{counter:03d}
**Date:** {today}
**Feasibility:** F3
**Presiding:** The Honorable Lucius J. Morningstar

---

"""
    full_content = header + deliberation
    if not full_content.strip().endswith("\n\n> *Transcript certified by MORNINGSTAR::SCRIBE*"):
        full_content = full_content.rstrip() + "\n\n---\n\n> *Transcript certified by MORNINGSTAR::SCRIBE*\n"

    path.write_text(full_content, encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run MORNINGSTAR courtroom deliberation via local/free LLMs",
    )
    parser.add_argument(
        "matter",
        nargs="?",
        help="Matter for the court to deliberate (or enter interactively)",
    )
    parser.add_argument(
        "-f", "--feasibility",
        default="F3",
        help="Feasibility level F0-F5 (default: F3)",
    )
    parser.add_argument(
        "--provider",
        help="Override config provider (ollama, lm_studio, openrouter)",
    )
    parser.add_argument(
        "--model",
        help="Override config model",
    )
    model_group = parser.add_mutually_exclusive_group()
    model_group.add_argument(
        "--model-select",
        action="store_true",
        help="[OpenRouter] Prompt to select model from list",
    )
    model_group.add_argument(
        "--model-spin",
        action="store_true",
        help="[OpenRouter] Slot machine: random model from list (default when no model set)",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Do not save transcript",
    )
    parser.add_argument(
        "--save-to",
        choices=["litigation", "courtroom"],
        default="litigation",
        help="Save transcript to litigation/transcripts/ (default) or courtroom/transcripts/",
    )
    parser.add_argument(
        "--hearing-type",
        choices=["standard", "expedited", "special_inquiry", "contempt"],
        default="standard",
        help="Hearing type: standard (full deliberation), expedited (F2 brief), special_inquiry (investigative, no vote), contempt",
    )
    parser.add_argument(
        "--no-spectators",
        action="store_true",
        help="Exclude spectators (Dr. Echo, Dr. Harley, Uncle Ruckus) from system prompt",
    )
    parser.add_argument(
        "--menu",
        action="store_true",
        help="Show interactive menu (even when matter is provided)",
    )
    args = parser.parse_args()

    config = load_config()
    providers = ["ollama", "lm_studio", "openrouter"]
    hearing_types = [
        ("standard", "Full deliberation — Opening, Arguments, Hail-Mary, Vote, Ruling"),
        ("expedited", "Brief format for F2 matters"),
        ("special_inquiry", "Investigative hearing, no vote"),
        ("contempt", "Adversarial proceeding"),
    ]

    # Interactive menu when no matter, or when --menu requested
    if not args.matter or args.menu:
        from litigation.ui import interactive_main_menu
        params = interactive_main_menu(config, providers, hearing_types)
        if params is None:
            raise SystemExit(0)
        matter = params["matter"]
        provider_name = params["provider"]
        model = params.get("model")
        args.feasibility = params.get("feasibility", args.feasibility)
        args.hearing_type = params.get("hearing_type", args.hearing_type)
        args.no_spectators = params.get("no_spectators", args.no_spectators)
        save_loc = params.get("save_location", "litigation")
        args.no_save = save_loc is None
        args.save_to = save_loc if save_loc else "litigation"
        # Override provider; model handled below
        args.provider = provider_name
        if model is not None:
            args.model = model
    else:
        matter = args.matter
        provider_name = args.provider or config.get("provider", "openrouter")
        model = args.model

    if not matter:
        print("No matter provided.", file=sys.stderr)
        raise SystemExit(1)

    provider_name = args.provider or config.get("provider", "openrouter")
    model = args.model or config.get("model") or "llama3.2"
    # Provider-specific model override (only when not set via --model)
    if not args.model:
        provider_config = config.get(provider_name, {})
        if isinstance(provider_config, dict) and provider_config.get("model"):
            model = provider_config["model"]

    # OpenRouter: model selection from list (interactive or slot machine)
    # When no --model: default to slot machine; use --model-select for interactive
    if provider_name == "openrouter" and not args.model:
        from litigation.models import (
            OPENROUTER_MODELS,
            select_model_interactive,
            select_model_spin,
        )
        models = (
            config.get("openrouter", {}).get("models")
            or OPENROUTER_MODELS
        )
        if args.model_select:
            model = select_model_interactive(models)
        else:
            model = select_model_spin(models)
    max_tokens = config.get("max_tokens", 8192)
    # Cap to avoid "maximum context length" errors (most models: 8k–128k)
    max_tokens = min(int(max_tokens), 32768)
    temperature = config.get("temperature", 0.7)

    # Resolve provider
    from litigation.providers import get_provider, ProviderError

    try:
        provider = get_provider(
            provider=provider_name,
            model=model,
            ollama_base_url=config.get("ollama", {}).get("base_url", "http://localhost:11434"),
            lm_studio_base_url=config.get("lm_studio", {}).get("base_url", "http://localhost:1234/v1"),
            openrouter_base_url=config.get("openrouter", {}).get("base_url", "https://openrouter.ai/api/v1"),
            openrouter_config=config.get("openrouter") if provider_name == "openrouter" else None,
        )
    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        raise SystemExit(1)

    # Build prompts (full framework: procedures, rules, personalities, checklists, experts, MFAF)
    from litigation.prompts import FrameworkLoader, build_deliberation_prompts

    loader = FrameworkLoader()
    state_summary = loader.state_summary()
    system_prompt, user_prompt = build_deliberation_prompts(
        matter=matter,
        feasibility=args.feasibility,
        state_summary=state_summary,
        hearing_type=args.hearing_type,
        include_spectators=not args.no_spectators,
    )

    print("", file=sys.stderr)
    print("Convening the court...", file=sys.stderr)
    print(f"  Provider: {provider_name}  |  Model: {model}", file=sys.stderr)
    print("-" * 60, file=sys.stderr)

    try:
        response = provider.complete(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )
    except ProviderError as e:
        err_str = str(e)
        is_data_policy = "data policy" in err_str.lower() or "openrouter.ai/settings/privacy" in err_str
        is_context_length = "context length" in err_str.lower() or "maximum context" in err_str.lower()
        print(f"LLM request failed: {e}", file=sys.stderr)
        print("", file=sys.stderr)
        if is_context_length:
            print("  Context limit: Reduce max_tokens in litigation/config.yaml (capped at 32k).", file=sys.stderr)
            print("  Or exclude components: --no-spectators, or use a smaller framework.", file=sys.stderr)
            print("", file=sys.stderr)
        if is_data_policy:
            print("  OpenRouter free models: Configure privacy at https://openrouter.ai/settings/privacy", file=sys.stderr)
            print("  Enable 'Model Training' or relax restrictions for free model access.", file=sys.stderr)
            print("", file=sys.stderr)
        print("Install or configure one of the following:", file=sys.stderr)
        print("", file=sys.stderr)
        print("  OpenRouter (default):", file=sys.stderr)
        print("    export OPENROUTER_API_KEY=sk-or-v1-your-key", file=sys.stderr)
        if not is_data_policy:
            print("    Privacy (free models): https://openrouter.ai/settings/privacy", file=sys.stderr)
        print("    Edit litigation/config.yaml and set provider: openrouter", file=sys.stderr)
        print("", file=sys.stderr)
        print("  Ollama:", file=sys.stderr)
        print("    pip install ollama", file=sys.stderr)
        print("    ollama pull llama3.2", file=sys.stderr)
        print("    Edit litigation/config.yaml and set provider: ollama", file=sys.stderr)
        print("", file=sys.stderr)
        print("  LM Studio:", file=sys.stderr)
        print("    Install from lmstudio.ai, load model, Start Server", file=sys.stderr)
        print("    Edit litigation/config.yaml and set provider: lm_studio", file=sys.stderr)
        print("", file=sys.stderr)
        print("See litigation/README.md for setup.", file=sys.stderr)
        raise SystemExit(1)

    print(response)

    if not args.no_save:
        save_to = getattr(args, "save_to", "litigation")
        path = save_transcript(matter, response, location=save_to)
        print("-" * 60, file=sys.stderr)
        print(f"Transcript saved: {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
