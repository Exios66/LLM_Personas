# Litigation Prompts

Loads and assembles the full MORNINGSTAR framework for the courtroom litigation runner. All content is loaded from repository paths at runtime.

---

## Framework Components

| Component | Source | Purpose |
|-----------|--------|---------|
| **Agent** | `agents/morningstar.md` | MORNINGSTAR identity, court composition, procedure |
| **Procedures** | `core/procedures.md` | Deliberation flow, tie-breaking, SME, contempt, session lifecycle |
| **Personalities** | `core/personalities.md` | Detailed voice, bias, failure modes, invocation |
| **Rules** | `courtroom/RULES.md` | Jurisdiction, voting, transcripts, precedent |
| **Best Practices** | `courtroom/BEST_PRACTICES.md` | When to deliberate, efficient deliberations |
| **Checklist (Judge)** | `checklists/judge-morningstar.md` | Presiding, session flow |
| **Checklist (Scribe)** | `checklists/courtroom-scribe.md` | Transcript verification, certification |
| **Spectators** | `courtroom/spectators.md` | Optional live commentary |
| **Special Interest** | `templates/special-interest-hearing.md` | Investigative hearing template |
| **Contempt** | `templates/contempt-hearing.md` | Contempt/prosecution template |
| **State** | `state/current.md` | Session context (summary) |

---

## Usage

```python
from litigation.prompts import FrameworkLoader, build_deliberation_prompts

# Full system + user prompts (includes all framework components)
system_prompt, user_prompt = build_deliberation_prompts(
    matter="Should we adopt a new API naming convention?",
    feasibility="F3",
    state_summary=loader.state_summary(),
)

# Load individual components
loader = FrameworkLoader()
agent = loader.agent
procedures = loader.procedures
rules = loader.rules
```

---

## Source Paths

Content is loaded from the repository root. The loader prefers `agents/` over `.cursor/agents/` for the MORNINGSTAR agent. Paths are defined in `sources.py`.

---

## Assembly

The assembler combines components in order:

1. Agent definition
2. Deliberation procedures
3. Personality definitions
4. Courtroom rules
5. Judge checklist
6. Scribe checklist
7. Best practices
8. Spectators (optional)
9. Litigation runner instruction

Flags in `build_deliberation_prompts()` allow excluding components (e.g. `include_spectators=False`) for shorter prompts.
