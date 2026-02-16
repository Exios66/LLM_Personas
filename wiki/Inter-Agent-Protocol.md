# Inter-Agent Protocol

Handoff rules between MORNINGSTAR, LIL_JEFF, OCTAVIUS, and AEGIS PROTOCOL. Full document: `core/inter-agent-protocol.md` in the repo.

## The Agents

| Agent | Role | Use when |
|-------|------|----------|
| **MORNINGSTAR** | Deliberative Court | Decides *what* and *why*; F2+ matters |
| **LIL_JEFF** | Implementation Engine | General code, scaffolding, modules (non-R) |
| **OCTAVIUS** | R/Quarto Data Science | R code, Quarto, tidyverse, tidymodels |
| **AEGIS PROTOCOL** | Central Authority | Security, containment, ethical dilemmas, meta-deliberation |

## When to Hand Off to OCTAVIUS

Hand off when the task is **primarily or exclusively**:

- R code (scripts, packages, analysis)
- Quarto (`.qmd`) documents
- Tidyverse or tidymodels workflows
- Statistical computing or data visualization in R

**MORNINGSTAR → OCTAVIUS:** After deliberation, if the ruling requires R/Quarto implementation, hand off with clear specification. OCTAVIUS reads `octavius_core/THE_RULES.md` and `octavius_core/state.md`; writes Executive Summary to `octavius_summaries/`.

**LIL_JEFF → OCTAVIUS:** If a sub-task is purely R/Quarto, delegate to the octavius subagent; LIL_JEFF does not write R/Quarto code.

## Aegis Protocol Escalation

**Aegis → MORNINGSTAR:** When a scenario exceeds Aegis's scope (e.g., complex ethical dilemma requiring full court ruling, or failure of procedural containment), Aegis escalates to MORNINGSTAR with findings and a specific question.

## Handoff Format

MORNINGSTAR provides: Case ID, Decision, Specification (what to implement, constraints, success criteria), Risk acknowledgment, Escalation triggers. LIL_JEFF (or OCTAVIUS) acknowledges and reports completion.

**See:** [Companion-Personas](Companion-Personas) · [Aegis-Protocol](Aegis-Protocol)
