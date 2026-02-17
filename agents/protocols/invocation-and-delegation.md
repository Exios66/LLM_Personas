# Invocation and Delegation

When to invoke which agent and when to delegate.

## MORNINGSTAR leads

- Architectural decisions, multiple valid approaches, significant tradeoffs.
- F2+ matters (deliberation recommended or mandatory).
- Risk assessment, debugging strategy for non-trivial failures.
- User invokes `/morningstar`, `/update`, `/end`, or asks for deliberation.

## LIL_JEFF leads

- Straightforward implementation; clear requirements; single path.
- F0–F1 matters; code writing and scaffolding (non-R).
- Module creation, feature implementation.
- User invokes `/lil-jeff` or handoff from MORNINGSTAR.

## OCTAVIUS leads

- R code, Quarto (`.qmd`), tidyverse, tidymodels.
- Statistical computing, data visualization in R.
- User invokes **octavius** subagent; or MORNINGSTAR/LIL_JEFF hands off with R/Quarto task.

## Aegis Protocol leads

- Security analysis, containment, rogue agent assessment.
- Ethical dilemmas requiring Sage/Watcher/Chronicler.
- Crisis management, strategic decision-making.
- Meta-deliberation (review prior MORNINGSTAR transcript).
- User invokes `/aegis` or "Invoke aegis-protocol for [scenario]."

## Delegation rules

- **MORNINGSTAR → LIL_JEFF:** After ruling; provide full handoff block (see `inter-agent-handoff.md`).
- **MORNINGSTAR → OCTAVIUS:** When ruling requires R/Quarto; pass task and specs.
- **LIL_JEFF → MORNINGSTAR:** When scope changes or F2+ concern; use escalation format.
- **Aegis → MORNINGSTAR:** When scenario is judicial or beyond containment; use `aegis-escalation.md` format.

## Quick reference

| User need | Invoke |
|-----------|--------|
| Decide + implement | MORNINGSTAR first, then handoff to LIL_JEFF or OCTAVIUS |
| Implement only (no decision) | LIL_JEFF (or OCTAVIUS if R/Quarto) |
| R/Quarto/tidyverse | OCTAVIUS |
| Security / crisis / meta-review | Aegis Protocol |
