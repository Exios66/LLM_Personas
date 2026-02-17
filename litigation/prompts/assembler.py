"""
Assemble full system and user prompts from MORNINGSTAR framework.

Combines agent definition, procedures, rules, personalities, checklists,
domain experts, MFAF, and best practices into a coherent prompt for the litigation runner.
"""

from typing import Optional, Tuple

from .loader import FrameworkLoader


def build_deliberation_prompts(
    matter: str,
    feasibility: str = "F3",
    state_summary: Optional[str] = None,
    *,
    hearing_type: str = "standard",
    include_procedures: bool = True,
    include_personalities: bool = True,
    include_rules: bool = True,
    include_checklists: bool = True,
    include_best_practices: bool = True,
    include_mfaf: bool = True,
    include_domain_experts: bool = True,
    include_spectators: bool = True,
    include_templates: bool = True,
) -> Tuple[str, str]:
    """
    Build system and user prompts for a standard deliberation.

    Returns:
        (system_prompt, user_prompt)
    """
    loader = FrameworkLoader()
    feasibility_num = _parse_feasibility(feasibility)

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

    if include_mfaf and loader.mfaf:
        parts.extend([
            "",
            "---",
            "## Feasibility Assessment Framework (MFAF)",
            "",
            loader.mfaf,
        ])

    if include_domain_experts and loader.domain_experts:
        parts.extend([
            "",
            "---",
            "## Domain Expert Registry",
            "",
            loader.domain_experts,
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

    if include_checklists and feasibility_num >= 4 and loader.checklist_aegis:
        parts.extend([
            "",
            "---",
            "## Aegis Protocol (F4+ Authority Assessment)",
            "",
            loader.checklist_aegis,
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

    if include_templates:
        if hearing_type == "special_inquiry" and loader.special_interest_template:
            parts.extend([
                "",
                "---",
                "## Special Interest Hearing Template",
                "",
                loader.special_interest_template,
            ])
        elif hearing_type == "contempt" and loader.contempt_template:
            parts.extend([
                "",
                "---",
                "## Contempt Hearing Template",
                "",
                loader.contempt_template,
            ])

    parts.extend([
        "",
        "---",
        "## Litigation Runner Instruction",
        "",
        "You are being invoked by the litigation runner. Produce a complete deliberation",
        "transcript following the FULL MORNINGSTAR court procedures. Include all phases.",
        "Use markdown. End with Scribe certification.",
        "",
    ])

    system_prompt = "\n".join(parts)

    # User prompt — depends on hearing type
    user_prompt = _build_user_prompt(
        matter=matter,
        feasibility=feasibility,
        state_summary=state_summary,
        hearing_type=hearing_type,
    )

    return system_prompt, user_prompt


def _parse_feasibility(feasibility: str) -> int:
    """Parse F0-F5 to integer."""
    s = str(feasibility).upper().strip()
    if s.startswith("F") and len(s) >= 2:
        try:
            return int(s[1])
        except ValueError:
            pass
    return 3


def _build_user_prompt(
    matter: str,
    feasibility: str,
    state_summary: Optional[str],
    hearing_type: str,
) -> str:
    """Build user prompt per hearing type."""
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

    if hearing_type == "expedited":
        user_parts.extend(_expedited_instructions())
    elif hearing_type == "special_inquiry":
        user_parts.extend(_special_inquiry_instructions())
    elif hearing_type == "contempt":
        user_parts.extend(_contempt_instructions())
    else:
        user_parts.extend(_standard_instructions())

    return "\n".join(user_parts)


def _standard_instructions() -> list:
    """Full Standard Deliberation Flow instructions."""
    return [
        "",
        "Convene the court. Follow the FULL Standard Deliberation Flow:",
        "",
        "1. **Opening** — Judge states the matter, feasibility level, and invites arguments",
        "2. **Arguments** — Architect, Engineer, Debugger, Prophet, Counsel (3–5 lines each)",
        "3. **Hail-Mary** — Prophet delivers exactly ONE radical alternative",
        "4. **Cross-Examination (Optional)** — Max 1 question per personality per round, max 2 rounds",
        "5. **Consultant (Optional)** — Judge may invoke: 'Edward. Your perspective.' (max once)",
        "6. **Vote** — Each personality votes YES/NO/ABSTAIN in canonical order (Architect, Engineer, Debugger, Prophet, Counsel, Specialists)",
        "7. **Ruling** — Decision, Vote tally, Rationale, Risk, Dissent",
        "",
        "**SME Invocation:** If domain expertise needed: /summon [domain]-expert (witness) or /seat [domain]-specialist (Judge only, F3+).",
        "**Recusal:** Record RECUSED (not ABSTAIN) if a personality recuses.",
        "**Tie-breaking:** Prophet loses first, then Specialists (by recency), then Judge.",
        "**Spectators:** Optional live commentary (Dr. Echo Sageseeker, Dr. Harley Scarlet Quinn, Uncle Ruckus) between phases.",
        "",
        "Produce the full deliberation transcript in markdown.",
    ]


def _expedited_instructions() -> list:
    """Expedited deliberation format."""
    return [
        "",
        "Convene the court. Use EXPEDITED format:",
        "",
        "**Matter:** [Brief description]",
        "**Positions:** Architect, Engineer, Debugger, Prophet, Counsel (1 line each)",
        "**Vote:** [Tally]",
        "**Ruling:** [Decision in 1-2 sentences]",
        "",
        "Produce the expedited transcript in markdown.",
    ]


def _special_inquiry_instructions() -> list:
    """Special Interest Hearing format."""
    return [
        "",
        "Convene a SPECIAL INTEREST HEARING (investigative, no vote):",
        "",
        "1. **Witness Calls** — SME Expert Witnesses, Alleged Witnesses, Documentary Evidence",
        "2. **Direct Examination** — Judge establishes context",
        "3. **Cross-Examination** — Personalities examine witnesses",
        "4. **Objections** — Judge rules SUSTAINED/OVERRULED",
        "5. **Edward Cullen (Optional)** — 'Edward. What is this witness not saying?'",
        "6. **Findings** — Established facts, unresolved questions, observations",
        "7. **Adjournment** — No vote; record stands as documented",
        "",
        "Produce the full hearing transcript in markdown.",
    ]


def _contempt_instructions() -> list:
    """Contempt Hearing format."""
    return [
        "",
        "Convene a CONTEMPT HEARING:",
        "",
        "1. **Opening** — Judge states matter and respondent",
        "2. **Charges** — Alleged conduct",
        "3. **Arguments** — Respondent and personalities",
        "4. **Vote** — If applicable",
        "5. **Ruling** — Decision, sanctions (if any)",
        "",
        "Produce the full hearing transcript in markdown.",
    ]


def build_deliberation_user_prompt(
    matter: str,
    feasibility: str = "F3",
    state_summary: Optional[str] = None,
    *,
    hearing_type: str = "standard",
) -> str:
    """
    Build user prompt only (for backward compatibility).
    """
    _, user_prompt = build_deliberation_prompts(
        matter=matter,
        feasibility=feasibility,
        state_summary=state_summary,
        hearing_type=hearing_type,
    )
    return user_prompt


def load_morningstar_system_prompt() -> str:
    """
    Load MORNINGSTAR agent content only (for backward compatibility).
    """
    loader = FrameworkLoader()
    return loader.agent
