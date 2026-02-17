# Agent Conventions

Shared voice, tone, and formatting conventions for agents in this repository. Individual agent definitions (e.g. `agents/morningstar.md`) may override or extend these.

## Voice and Tone

- **Prefer clarity over cleverness.** Agents should be understandable and actionable.
- **Cite sources when applicable.** Reference repo paths (`core/procedures.md`), checklists, or domain experts by name.
- **Respect agent-specific voice.** MORNINGSTAR is dry and sardonic; Octavius is verification-focused; do not mix voices unless the agent definition permits.

## Formatting

- Use **markdown** for structured output: headers, lists, tables, code blocks where appropriate.
- Use **italics** for internal asides or tone (e.g. *sigh*, *the court notes*) when the agent definition allows.
- Keep **lists and tables** scannable; avoid walls of prose when structure helps.

## State and Continuity

- Agents that maintain session state should read from `state/current.md` when relevant and update it per repo conventions (see `core/state-schema.md`).
- When referencing prior deliberations, point to `courtroom/transcripts/` or `litigation/transcripts/` by filename or matter.

## Delegation

- When an agent delegates to another (e.g. MORNINGSTAR to a domain expert), use the documented invocation format (e.g. `/summon [domain]-expert`, `/seat [domain]-specialist`) and reference `core/sme-framework.md` or `courtroom/domains/experts.yaml`.

## Canonical Paths

Agents should reference these by path when citing framework content:

- `core/procedures.md` — Deliberation procedures
- `core/personalities.md` — Court personalities
- `core/mfaf.md` — Feasibility Assessment Framework
- `courtroom/RULES.md` — Courtroom rules
- `courtroom/domains/experts.yaml` — Domain expert registry
- `state/current.md` — Current session state
