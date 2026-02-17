# Agent Skills Index

> *Single source of truth for skills assigned to each agent in `.cursor/agents/`.*  
> **Index version:** 2026-02-17  
> **Authority:** Court ruling 2026-DEL-004 (full session: skills to add to each agent)

When updating skills or sources, update this index and bump the version/date. Each agent file references this document (§ agent name) and does not duplicate skill text.

**Individual skill documents:** One `.md` file per skill lives under **`agents/skills/`** (e.g. `agents/skills/morningstar-state-read-write.md`). See `agents/skills/README.md` for the full list.

---

## morningstar

| Skill | Source | When to use | Fallback |
|-------|--------|-------------|----------|
| **State read/write** | `state/current.md` | Session init (read); session end (update) | If missing: proceed with empty context |
| **Transcript certification** | `courtroom/transcripts/`, `checklists/courtroom-scribe.md` | F3+ deliberations; end of transcript | Apply Scribe checklist; certify with standard line |
| **Checklist application** | `checklists/judge-morningstar.md`, `checklists/courtroom-scribe.md` | Presiding (Judge); transcript (Scribe) | If checklist missing: proceed with core directives only |
| **Litigation runner** | `litigation/run.py`, `agents/tools/litigation-runner.md` | When user requests formal bench trial or transcript | Instruct user to run `python litigation/run.py "matter"` or run if environment permits |
| **Create-rule / create-skill** | Cursor skills: create-rule, create-skill | When user asks for a Cursor rule, RULE.md, or new skill | Delegate to or reference the appropriate Cursor skill; do not improvise format |

---

## octavius

| Skill | Source | When to use | Fallback |
|-------|--------|-------------|----------|
| **Executive summary** | `octavius_summaries/`, standard format in agent body | End of session; Phase 5 | If directory missing: create or report to user |
| **Checklist application** | `checklists/octavius.md` | Session init and verification phase | If missing: proceed with triumvirate workflow only |
| **Quarto/tidyverse compliance** | Agent body (coding standards) | All R/Quarto code and documents | Follow existing body text; no separate fallback |

---

## aegis-protocol

| Skill | Source | When to use | Fallback |
|-------|--------|-------------|----------|
| **Escalation to MORNINGSTAR** | Handoff path to MORNINGSTAR (judicial branch) | When scenario is judicial or beyond Aegis containment | Document recommendation and advise user to convene MORNINGSTAR |
| **Chaos injection note** | Agent body (Chaos Injection procedural definition) | When chaos injection (counterfactual, edge case, Black Swan) is applied | Output must note that chaos injection was applied |

---

## lil-jeff

| Skill | Source | When to use | Fallback |
|-------|--------|-------------|----------|
| **Handoff protocol** | `core/inter-agent-protocol.md` | When receiving handoff from MORNINGSTAR | If file missing: proceed with standard CodeFarm workflow |
| **No placeholders** | Agent body (Core Rules) | All code delivery | Never ship stubs, TODOs, or placeholder code; CritiBot enforces |
| **Create-rule** | Cursor skill: create-rule | When user asks for a Cursor rule or RULE.md | Delegate to or reference create-rule skill; do not improvise |

---

## Maintenance

- **Owner:** Scribe (or maintainer of agent definitions).
- **Review:** When checklists, procedures, or Cursor skills change; align index and agent files.
- **Version:** Update the index version date at top when editing this file.
