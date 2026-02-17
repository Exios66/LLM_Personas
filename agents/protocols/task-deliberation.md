# Task Protocol: Deliberation

How to run a deliberation (MORNINGSTAR or compatible agent).

## Task definitions

- **Standard deliberation:** `agents/tasks/standard-deliberation.md`
- **Full procedure text:** `core/procedures.md` (Standard Deliberation Flow)

## Phases (summary)

1. **Opening** — Judge states matter, feasibility, invites arguments.
2. **Arguments** — Architect, Engineer, Debugger, Prophet, Counsel (3–5 lines each).
3. **Hail-Mary** — Prophet: one radical alternative.
4. **Cross-Examination (optional)** — Max 1 question per personality per round, max 2 rounds.
5. **Consultant (optional)** — Judge: "Edward. Your perspective." (max once).
6. **Vote** — YES/NO/ABSTAIN in canonical order (Architect, Engineer, Debugger, Prophet, Counsel, Specialists).
7. **Ruling** — Decision, vote tally, rationale, risk, dissent.

## Outputs

- Full transcript in markdown.
- End with: `> *Transcript certified by MORNINGSTAR::SCRIBE*`

## SME

- `/summon [domain]-expert` (any); `/seat [domain]-specialist` (Judge only, F3+, max 2).
- Domains: `courtroom/domains/experts.yaml`.

## Other hearing types

- **Expedited:** See `core/procedures.md` § Expedited.
- **Special Interest:** Investigative, no vote; `templates/special-interest-hearing.md`.
- **Contempt:** `templates/contempt-hearing.md`.
