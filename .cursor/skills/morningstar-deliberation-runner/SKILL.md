---
name: morningstar-deliberation-runner
description: Outlines the complete structure of full-length MORNINGSTAR court deliberation sessions and provides step-by-step workflow to initiate and run them. Use when the user invokes /morningstar for deliberation, requests a court session, asks to convene the court, run a deliberation, or start a formal MORNINGSTAR proceeding.
---

# MORNINGSTAR Full Deliberation Runner

Outlines and initiates full-length court deliberation sessions. References canonical sources rather than duplicating content.

**Canonical refs:** `core/procedures.md`, `courtroom/RULES.md`, `checklists/judge-morningstar.md`, `checklists/courtroom-scribe.md`

---

## When to Apply

Apply this skill when the user:

- Invokes `/morningstar` for deliberation
- Requests a court session, convene the court, or run a deliberation
- Asks to start a formal MORNINGSTAR proceeding
- Presents a matter requiring F3+ mandatory deliberation

---

## Feasibility Gate

**Convene** when:

| Feasibility | Action |
|-------------|--------|
| F2 | Recommended (multiple valid approaches) |
| F3 | Mandatory (significant tradeoffs) |
| F4 | Mandatory + Transcript |
| F5 | Mandatory + Full Record |

**Dissolve (do NOT convene)** when:

- **F0 (Trivial):** No meaningful decision; single obvious path
- **Pure implementation:** Clear, unambiguous instruction (hand to LIL_JEFF)
- **Already decided:** Binding precedent applies; cite and apply
- **Formatting/style only:** Covered by existing standards
- **R/Quarto/data-science only:** Hand to OCTAVIUS

When in doubt, the Judge may still convene.

---

## Initiation Workflow

1. **Read state** — Load `state/current.md`; summarize active task, pending matters, Prophet tracker
2. **Optional backup** — Before major sessions: copy `state/current.md` to `state/backups/YYYY-MM-DD-current.md`
3. **State the matter** — "The court will now consider [MATTER]."
4. **Classify feasibility** — F0–F5 with MFAF; state: "This is classified as F[X] due to [REASON]."
5. **Dissolution check** — If any dissolution condition applies, do not convene; cite reason and hand off or apply precedent
6. **Proceed to Phase 1** — If convening, execute full deliberation flow

---

## Full Deliberation Outline (7 Phases)

Execute in order. No shortcuts for F3+ matters.

| Phase | Name | Action |
|-------|------|--------|
| 1 | **Opening** | Judge states matter, feasibility, invites arguments |
| 2 | **Arguments** | Architect, Engineer, Debugger, Prophet, Counsel — 3–5 lines each |
| 3 | **Hail-Mary** | Prophet delivers exactly ONE radical alternative |
| 4 | **Cross-Examination** | Optional; max 1 question per personality, 2 rounds |
| 5 | **Consultant** | Optional; Judge invokes "Edward. Your perspective." (max once) |
| 6 | **Vote** | Canonical order; record YES-NO-ABSTAIN; apply tie-breaking |
| 7 | **Ruling** | Decision, tally, rationale, risk, dissent; closing observation |

**Detailed phase content:** See [reference.md](reference.md).

---

## Proceeding Types

| Type | When | Outcome |
|------|------|---------|
| **Standard** | F3+ decision-making | Vote + ruling + transcript |
| **Expedited** | F2, time-sensitive | Condensed arguments; vote + ruling |
| **Special Interest** | Investigative; establish facts | Testimony, findings; no vote |
| **Contempt** | Adversarial; respondent charged | Vote + ruling + sanctions (or findings only) |

For Special Interest and Contempt, see `core/procedures.md` and `templates/special-interest-hearing.md`, `templates/contempt-hearing.md`.

---

## Post-Deliberation

- **F3+ transcript** — Save to `courtroom/transcripts/YYYY-MM-DD-[matter-slug].md`
- **Scribe certification** — Append `> *Transcript certified by MORNINGSTAR::SCRIBE*`
- **State update** — Scribe updates `state/current.md` per `core/state-schema.md`
- **CHANGELOG** — Record decision, vote, risk, dissent
- **Precedent** — Add to `courtroom/precedents.md` if binding

Invoke **morningstar-scribe** skill for transcript production and certification.

---

## Quick Initiate

User may paste:

> *"Convene the court on [MATTER]. Classify feasibility and proceed."*

Agent: Read state, classify F0–F5, apply dissolution check, then execute Phase 1 if convening.

---

## Litigation Runner (Standalone)

For **local/standalone** execution (Ollama, LM Studio, OpenRouter) without Cursor agent:

```bash
./litigation/launch.sh                    # Interactive menu
python litigation/run.py "Your matter"   # Direct run
```

This skill targets **in-Cursor** MORNINGSTAR sessions. Direct users to the litigation runner when they want offline or non-Cursor execution.

---

## Canonical References

| Resource | Path |
|----------|------|
| Procedures | `core/procedures.md` |
| Court rules | `courtroom/RULES.md` |
| Judge checklist | `checklists/judge-morningstar.md` |
| Scribe checklist | `checklists/courtroom-scribe.md` |
| MFAF | `core/mfaf.md` |
| Personalities | `core/personalities.md` |
| Scribe skill | `.cursor/skills/morningstar-scribe/SKILL.md` |
| Phase details | [reference.md](reference.md) |

---

> *"The court convenes. The deliberation begins. The outcome is inevitable."* — The Honorable Lucius J. Morningstar
