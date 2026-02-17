# Skill: Checklist application

**Agent:** morningstar  
**Index:** `docs/agent-skills.md` § morningstar

## Source

`checklists/judge-morningstar.md`, `checklists/courtroom-scribe.md`

## When to use

- **Presiding (Judge):** Use `checklists/judge-morningstar.md` for session flow, deliberation phases, and tie-breaking.
- **Transcript (Scribe):** Use `checklists/courtroom-scribe.md` for transcript verification and certification.

## Fallback

If a checklist is missing: proceed with core directives only. Do not block on checklist presence.

## Procedure

1. At session init and during deliberation, reference Judge checklist for phase order and rules.
2. Before certifying a transcript, run through Scribe checklist (record decisions, dissent, certification).
3. F4+ matters: consider `checklists/aegis-protocol.md` if Aegis Authority Assessment is required.
