# Agent Skills (SKILL.md documents)

Individual skill documents for each capability assigned to agents. **Canonical index:** `docs/agent-skills.md`. These files are the referenceable skill definitions; agent files point to the index, which maps to these documents.

## Layout

| Agent | Skill documents |
|-------|-----------------|
| **morningstar** | `morningstar-state-read-write.md`, `morningstar-transcript-certification.md`, `morningstar-checklist-application.md`, `morningstar-litigation-runner.md`, `morningstar-create-rule-skill.md` |
| **octavius** | `octavius-executive-summary.md`, `octavius-checklist-application.md`, `octavius-quarto-tidyverse-compliance.md` |
| **aegis-protocol** | `aegis-escalation-to-morningstar.md`, `aegis-chaos-injection-note.md` |
| **lil-jeff** | `lil-jeff-handoff-protocol.md`, `lil-jeff-no-placeholders.md`, `lil-jeff-create-rule.md` |

## Naming

- `{agent}-{skill-slug}.md` (kebab-case).
- One file per skill; do not merge skills into one file.

## Maintenance

- When adding or changing a skill, update `docs/agent-skills.md` and create or edit the corresponding file here.
- Keep skill documents concise: name, source, when, fallback, brief procedure.
