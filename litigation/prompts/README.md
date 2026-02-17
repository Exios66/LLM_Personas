# Litigation Prompts

Loads and assembles the full MORNINGSTAR framework for the courtroom litigation runner. All content is loaded from repository paths at runtime.

---

## Framework Components

| Component | Source | Purpose |
|-----------|--------|---------|
| **Agent** | `agents/morningstar.md` | MORNINGSTAR identity, court composition, procedure |
| **Procedures** | `core/procedures.md` | Deliberation flow, tie-breaking, SME, contempt, session lifecycle |
| **Personalities** | `core/personalities.md` | Judge, Edward Cullen, Architect, Engineer, Debugger, Prophet, Counsel, Scribe |
| **Rules** | `courtroom/RULES.md` | Jurisdiction, voting, transcripts, precedent |
| **MFAF** | `core/mfaf.md` | Feasibility Assessment Framework (F0–F5, risk vectors) |
| **Domain Experts** | `courtroom/domains/experts.yaml` | 24 full (Witness+Specialist) + 2 advisory; see courtroom/domains/README.md for full list |
| **Checklist (Judge)** | `checklists/judge-morningstar.md` | Presiding, session flow |
| **Checklist (Scribe)** | `checklists/courtroom-scribe.md` | Transcript verification, certification |
| **Checklist (Aegis)** | `checklists/aegis-protocol.md` | F4+ Authority Assessment |
| **Best Practices** | `courtroom/BEST_PRACTICES.md` | When to deliberate, efficient deliberations |
| **Spectators** | `courtroom/spectators.md` | Dr. Echo Sageseeker, Dr. Harley Scarlet Quinn, Uncle Ruckus |
| **Special Interest** | `templates/special-interest-hearing.md` | Investigative hearing template |
| **Contempt** | `templates/contempt-hearing.md` | Contempt/prosecution template |
| **State** | `state/current.md` | Session context (summary) |

---

## Usage

```python
from litigation.prompts import FrameworkLoader, build_deliberation_prompts

# Full system + user prompts (includes all framework components)
loader = FrameworkLoader()
system_prompt, user_prompt = build_deliberation_prompts(
    matter="Should we adopt a new API naming convention?",
    feasibility="F3",
    state_summary=loader.state_summary(),
    hearing_type="standard",  # or expedited, special_inquiry, contempt
    include_spectators=True,
)

# Load individual components
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
5. MFAF (Feasibility Assessment Framework)
6. Domain Expert Registry
7. Judge checklist
8. Scribe checklist
9. Aegis checklist (F4+ matters only)
10. Best practices
11. Spectators (optional)
12. Hearing template (Special Interest or Contempt, when applicable)
13. Litigation runner instruction

Flags in `build_deliberation_prompts()` allow excluding components (e.g. `include_spectators=False`, `include_mfaf=False`) for shorter prompts.
