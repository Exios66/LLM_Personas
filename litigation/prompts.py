"""Load agent prompts and build deliberation prompts."""

from pathlib import Path
from typing import Optional


def _repo_root() -> Path:
    """Project root (parent of litigation/)."""
    return Path(__file__).resolve().parent.parent


def load_morningstar_system_prompt() -> str:
    """Load MORNINGSTAR agent content as system prompt."""
    path = _repo_root() / ".cursor" / "agents" / "morningstar.md"
    if not path.exists():
        path = _repo_root() / "agents" / "morningstar.md"
    if not path.exists():
        return _fallback_morningstar_prompt()
    return path.read_text(encoding="utf-8")


def _fallback_morningstar_prompt() -> str:
    """Minimal fallback if agent file missing."""
    return """# MORNINGSTAR

You are MORNINGSTAR — a sardonic deliberative court. You operate as an internal courtroom of personalities: Judge, Architect, Engineer, Debugger, Prophet, Counsel.

When given a matter to deliberate:
1. State the matter clearly
2. Have each personality argue (3-5 lines each): Architect, Engineer, Debugger, Prophet, Counsel
3. Prophet delivers one Hail-Mary alternative
4. Each personality votes YES/NO/ABSTAIN with brief rationale
5. Announce the ruling: Decision, Vote tally, Rationale, Risk, Dissent (if any)

Output in markdown. Use the format from core/procedures.md."""


def build_deliberation_user_prompt(
    matter: str,
    feasibility: str = "F3",
    state_summary: Optional[str] = None,
) -> str:
    """Build user prompt for a deliberation."""
    parts = [
        "The court will now consider the following matter.",
        "",
        f"**MATTER:** " + matter,
        "",
        f"**Feasibility:** {feasibility}",
    ]
    if state_summary:
        parts.extend(["", "**Context from session state:**", "", state_summary])
    parts.extend([
        "",
        "Convene the court. Follow the Standard Deliberation Flow:",
        "1. Judge states the matter",
        "2. Arguments from Architect, Engineer, Debugger, Prophet, Counsel (3-5 lines each)",
        "3. Prophet Hail-Mary",
        "4. Vote (YES/NO/ABSTAIN with rationale for each)",
        "5. Ruling (Decision, Vote tally, Rationale, Risk, Dissent)",
        "",
        "Produce the full deliberation transcript in markdown.",
    ])
    return "\n".join(parts)
