# Agents

Root folder for agent definitions and agent-related assets used by the LLM Personas project (Cursor, litigation runner, and other consumers).

## Layout

| Directory | Purpose |
|-----------|---------|
| **`tasks/`** | Task definitions, templates, and task specs that agents can invoke or follow. |
| **`tools/`** | Tool specifications and references for agent-invokable tools (APIs, scripts, MCP tools). |
| **`core/`** | Shared agent primitives: conventions, shared prompts, and cross-agent reference material. Distinct from repo root `core/` (MORNINGSTAR framework). |
| **`prompts/`** | Agent-specific prompt fragments, system-prompt building blocks, and reusable prompt templates. |

## Agent Definitions (root)

Agent definition files live at the root of `agents/`:

- **`morningstar.md`** — MORNINGSTAR deliberative court (Judge, Architect, Engineer, Debugger, Prophet, Counsel, Scribe).
- **`octavius.md`** — Octavius verification/spec-compliance agent.
- **`aegis-protocol.md`** — Aegis Protocol authority-assessment agent.
- **`lil-jeff.md`** — Lil Jeff code-review and improvement agent.

Consumers (e.g. litigation runner) resolve agent content via `agents/{name}.md` with fallback to `.cursor/agents/{name}.md` when applicable.

## Canonical References

- `core/` (repo root) — MORNINGSTAR procedures, personalities, MFAF.
- `courtroom/` — Court rules, domains, spectators, transcripts.
- `litigation/prompts/sources.py` — Source map for litigation runner (includes `agents_path()`).
