# Agents

Root folder for agent definitions and agent-related assets used by the LLM Personas project (Cursor, litigation runner, and other consumers).

## Layout

| Directory | Purpose |
|-----------|---------|
| **`skills/`** | Individual SKILL.md documents per agent capability (state read/write, transcript certification, handoff, etc.). Index: `docs/agent-skills.md`. |
| **`protocols/`** | Interaction and task protocols: inter-agent handoff, invocation and delegation, Aegis escalation, task deliberation. |
| **`templates/`** | Reusable output templates: session state init, transcript certification, handoff blocks, escalation blocks, Octavius executive summary. |
| **`tasks/`** | Task definitions and task specs that agents can invoke or follow (e.g. standard deliberation). |
| **`tools/`** | Tool specifications and references for agent-invokable tools (APIs, scripts, MCP tools). |
| **`workflows/`** | Executable multi-agent workflows (e.g. Research Report: research → fact-check → write → format → Gmail). |
| **`reports/`** | Output directory for workflow reports (e.g. `RPT_XXXX_YYYYMMDD_HHMMSS.html`). |
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
