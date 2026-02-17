# Agent Tasks

Task definitions, templates, and specs that agents can invoke or follow. Use these to standardize how agents execute common workflows (e.g. deliberation, review, verification).

## Purpose

- **Task definitions** describe what an agent should do, in what order, and with what outputs.
- **Templates** provide fill-in-the-blank flows (e.g. standard deliberation, expedited ruling).
- **Specs** can be consumed by runners or other tooling to drive agent behavior.

## Naming

- Use kebab-case for filenames: `standard-deliberation.md`, `expedited-ruling.md`.
- One logical task per file; split by agent if the same task has agent-specific variants.

## Relation to Repo

- Repo **`core/procedures.md`** defines MORNINGSTAR deliberation procedures; tasks here can reference or mirror those flows for agent-invocation contexts.
- Repo **`templates/`** holds courtroom/hearing templates; `agents/tasks/` holds agent-oriented task flows.
