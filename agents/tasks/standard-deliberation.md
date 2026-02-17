# Task: Standard Deliberation

**Agent:** MORNINGSTAR (or compatible deliberative agent)  
**Source:** `core/procedures.md` (Standard Deliberation Flow)

## Objective

Convene the court and produce a complete deliberation transcript for a given matter, including opening, arguments, Hail-Mary, optional cross-examination, optional Consultant, vote, and ruling.

## Steps

1. **Opening** — Judge states the matter, feasibility level, and invites arguments.
2. **Arguments** — Architect, Engineer, Debugger, Prophet, Counsel (3–5 lines each).
3. **Hail-Mary** — Prophet delivers exactly ONE radical alternative.
4. **Cross-Examination (Optional)** — Max 1 question per personality per round, max 2 rounds.
5. **Consultant (Optional)** — Judge may invoke: "Edward. Your perspective." (max once).
6. **Vote** — Each personality votes YES/NO/ABSTAIN in canonical order (Architect, Engineer, Debugger, Prophet, Counsel, Specialists).
7. **Ruling** — Decision, vote tally, rationale, risk, dissent.

## Outputs

- Full deliberation transcript in markdown.
- End with Scribe certification: `> *Transcript certified by MORNINGSTAR::SCRIBE*`

## SME Invocation

- **Expert Witness:** `/summon [domain]-expert` (any personality or Judge).
- **Specialist:** `/seat [domain]-specialist` (Judge only, F3+ matters; max 2 per deliberation).

## References

- `core/procedures.md` — Full procedure text.
- `core/personalities.md` — Personality definitions and voting order.
- `courtroom/domains/experts.yaml` — Available domains for summon/seat.
