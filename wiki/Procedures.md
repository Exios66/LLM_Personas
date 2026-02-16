# Procedures

High-level session and deliberation flow. Full detail is in the repo: `core/procedures.md`.

## Session Lifecycle

1. **Session start (`/morningstar`):** Read state, summarize context, predict likely failures, await matter.
2. **State backup (recommended):** Before major sessions, copy `state/current.md` to `state/backups/YYYY-MM-DD-current.md`. See [Error-Recovery](Error-Recovery).
3. **Checkpoint (`/update`):** Update state with progress, decisions, pending matters.
4. **Session close (`/end`):** Finalize deliberations, update CHANGELOG and transcripts, checkpoint state.

## Deliberation Flow

1. **Opening** — Judge states the matter and feasibility.
2. **Arguments** — Each personality presents position (3–5 lines).
3. **Hail-Mary** — Prophet offers one radical alternative.
4. **Vote** — YES/NO/ABSTAIN; tally and ruling.
5. **Ruling** — Decision, Rationale, Risk, (optional) Dissent.

Optional: cross-examination, Consultant (Edward) invocation.

## Dissolution Protocol

When **not** to convene: F0 trivial, pure implementation, already decided by precedent, formatting-only, or R/Quarto-only (hand to OCTAVIUS). See [When-to-Convene](When-to-Convene).

**See also:** [The-Court](The-Court) · [State-and-Metrics](State-and-Metrics)
