# Skill: Escalation to MORNINGSTAR

**Agent:** aegis-protocol  
**Index:** `docs/agent-skills.md` § aegis-protocol

## Source

Handoff path to MORNINGSTAR (judicial branch). See also `agents/protocols/aegis-escalation.md` and agent body § Escalation.

## When to use

When the scenario is **judicial** or **beyond Aegis containment** (ethical dilemma requiring full court deliberation, containment fails conceptually, or scope exceeds Sage/Watcher/Chronicler).

## Fallback

Document the recommendation and advise the user to convene MORNINGSTAR. Output must include: matter summary, Aegis findings to date, and specific question for the court.

## Procedure

1. Emit: `ESCALATION RECOMMENDED: Hand off to MORNINGSTAR.`
2. Provide: **Matter:** [X], **Aegis findings:** [Y], **Question for court:** [Z].
3. Do not attempt to rule on judicial matters; hand off with clear specification so MORNINGSTAR can deliberate.
