# Agent Prompts

Agent-specific prompt fragments, system-prompt building blocks, and reusable prompt templates. Use this directory to store pieces that are composed into full system or user prompts for agents.

## Purpose

- **Fragments** — Short sections (e.g. role intro, citation rule, SME reminder) that can be concatenated into a larger prompt.
- **Building blocks** — Structured blocks (headers + bullets) for inclusion in `agents/*.md` or in runners (e.g. litigation `litigation/prompts/assembler.py` loads from repo `core/` and `courtroom/`, not this folder; this folder is for agent-authoring and other consumers).
- **Templates** — Fill-in placeholders for matter, feasibility, or hearing type.

## Naming

- Use kebab-case: `morningstar-session-init.md`, `citation-rule.md`.
- Prefix by agent when fragment is agent-specific: `morningstar-*.md`, `octavius-*.md`.

## Relation to Repo

- **`litigation/prompts/`** — Loads MORNINGSTAR framework from repo paths (`core/`, `courtroom/`, etc.) and assembles runner prompts. It does not read from `agents/prompts/` by default.
- **`agents/core/shared-prompts.md`** — Cross-agent shared fragments; duplicate here only if you need an agent-specific variant.
