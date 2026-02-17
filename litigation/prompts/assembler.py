"""
Assemble full system and user prompts from MORNINGSTAR framework.

Combines agent definition, procedures, rules, personalities, checklists,
and best practices into a coherent prompt for the litigation runner.
"""

from typing import Optional, Tuple

from .loader import FrameworkLoader


def build_deliberation_prompts(
    matter: str,
    feasibility: str = "F3",
    state_summary: Optional[str] = None,
    *,
    include_procedures: bool = True,
    include_personalities: bool = True,
    include_rules: bool = True,
    include_checklists: bool = True,
    include_best_practices: bool = True,
    include_spectators: bool = False,
) -> Tuple[str, str]:
    """
    Build system and user prompts for a standard deliberation.

    Returns:
        (system_prompt, user_prompt)
    """
    loader = FrameworkLoader()

    # System prompt: agent + framework components
    parts = [loader.agent]

    if include_procedures and loader.procedures:
        parts.extend([
            "",
            "---",
            "## Deliberation Procedures (MUST FOLLOW)",
            "",
            loader.procedures,
        ])

    if include_personalities and loader.personalities:
        parts.extend([
            "",
            "---",
            "## Personality Definitions (Reference)",
            "",
            loader.personalities,
        ])

    if include_rules and loader.rules:
        parts.extend([
            "",
            "---",
            "## Courtroom Rules (Binding)",
            "",
            loader.rules,
        ])

    if include_checklists and loader.checklist_judge:
        parts.extend([
            "",
            "---",
            "## Judge Checklist (Presiding)",
            "",
            loader.checklist_judge,
        ])

    if include_checklists and loader.checklist_scribe:
        parts.extend([
            "",
            "---",
            "## Scribe Checklist (Transcript)",
            "",
            loader.checklist_scribe,
        ])

    if include_best_practices and loader.best_practices:
        parts.extend([
            "",
            "---",
            "## Best Practices",
            "",
            loader.best_practices,
        ])

    if include_spectators and loader.spectators:
        parts.extend([
            "",
            "---",
            "## Spectators (Optional Commentary)",
            "",
            loader.spectators,
        ])

    parts.extend([
        "",
        "---",
        "## Litigation Runner Instruction",
        "",
        "You are being invoked by the litigation runner. Produce a complete deliberation",
        "transcript following the Standard Deliberation Flow. Include all phases: Opening,",
        "Arguments, Hail-Mary, Vote, Ruling. Use markdown. End with Scribe certification.",
        "",
    ])

    system_prompt = "\n".join(parts)

    # User prompt
    user_parts = [
        "The court will now consider the following matter.",
        "",
        f"**MATTER:** " + matter,
        "",
        f"**Feasibility:** {feasibility}",
    ]

    if state_summary:
        user_parts.extend([
            "",
            "**Context from session state:**",
            "",
            state_summary,
        ])

    user_parts.extend([
        "",
        "Convene the court. Follow the Standard Deliberation Flow:",
        "",
        "1. **Opening** — Judge states the matter and feasibility",
        "2. **Arguments** — Architect, Engineer, Debugger, Prophet, Counsel (3–5 lines each)",
        "3. **Hail-Mary** — Prophet delivers exactly ONE radical alternative",
        "4. **Vote** — Each personality votes YES/NO/ABSTAIN with brief rationale (canonical order)",
        "5. **Ruling** — Decision, Vote tally, Rationale, Risk, Dissent",
        "",
        "Apply tie-breaking if needed: Prophet loses first, then Specialists, then Judge.",
        "Produce the full deliberation transcript in markdown.",
    ])

    user_prompt = "\n".join(user_parts)

    return system_prompt, user_prompt


def build_deliberation_user_prompt(
    matter: str,
    feasibility: str = "F3",
    state_summary: Optional[str] = None,
) -> str:
    """
    Build user prompt only (for backward compatibility).
    """
    _, user_prompt = build_deliberation_prompts(
        matter=matter,
        feasibility=feasibility,
        state_summary=state_summary,
    )
    return user_prompt


def load_morningstar_system_prompt() -> str:
    """
    Load MORNINGSTAR agent content only (for backward compatibility).
    """
    loader = FrameworkLoader()
    return loader.agent
