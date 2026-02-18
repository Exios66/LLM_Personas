# Litigation Prompts

Loads and assembles the full MORNINGSTAR framework for the courtroom litigation runner. Framework content is loaded from repository paths at runtime; litigation-specific prompt fragments live in this subdirectory.

---

## Prompts in This Subdirectory

| File | Purpose |
|------|---------|
| **runner-instruction.md** | Final system-prompt tail: instructs the model to produce a full deliberation transcript in markdown with Scribe certification. |
| **user-prefix.md** | Opening line of the user prompt (e.g. "The court will now consider the following matter."). |
| **user/standard.md** | Standard Deliberation Flow instructions (Opening → Arguments → Hail-Mary → Cross-Examination → Consultant → Vote → Ruling, SME/recusal/tie-breaking/spectators). |
| **user/expedited.md** | Expedited format: Matter, Positions, Vote, Ruling (brief). |
| **user/special_inquiry.md** | Special Interest Hearing: Witness Calls, Direct/Cross-Examination, Objections, Edward Cullen, Findings, Adjournment. |
| **user/contempt.md** | Contempt Hearing: Opening, Charges, Arguments, Vote, Ruling/sanctions. |

The assembler uses these files when building prompts; if a file is missing, it falls back to built-in default text. Edit these files to change litigation runner behavior without changing Python code.

---

## Framework Components (Repository Paths)

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

- **Framework content:** Loaded from the repository root (`agents/`, `core/`, `courtroom/`, `checklists/`, `templates/`). Paths are defined in `sources.py`. The loader prefers `agents/` over `.cursor/agents/` for the MORNINGSTAR agent.
- **Litigation prompt fragments:** Loaded from this directory (`litigation/prompts/`) via `litigation_prompt_path()` in `sources.py`; see `loader.runner_instruction`, `loader.user_prefix`, and `loader.user_instructions(hearing_type)`.

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
