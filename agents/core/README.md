# Agents Core

Shared primitives, conventions, and cross-agent reference material for all agents defined under `agents/`. This directory is **distinct** from the repo root **`core/`**, which holds the MORNINGSTAR framework (procedures, personalities, MFAF).

## Purpose

- **Conventions** — Voice, formatting, and behavioral norms that apply across agents.
- **Shared prompts** — Reusable fragments (e.g. state-reading, citation rules) that multiple agents can include.
- **Cross-agent references** — Pointers to canonical docs (courtroom rules, checklists) so agent definitions stay DRY.

## Contents

| File | Description |
|------|-------------|
| `conventions.md` | Voice, tone, and formatting conventions for agent output. |
| `shared-prompts.md` | Reusable prompt fragments for state, citations, and session init. |

## Relation to Repo

- **`core/`** (repo root) — MORNINGSTAR-specific: procedures, personalities, mfaf, state-schema. Do not duplicate here; reference by path.
- **`agents/core/`** — Agent-agnostic or multi-agent shared content only.
