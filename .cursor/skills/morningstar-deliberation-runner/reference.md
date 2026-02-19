# MORNINGSTAR Deliberation Runner — Reference

Phase-by-phase content for full-length court deliberation. See [SKILL.md](SKILL.md) for when to apply and initiation workflow.

---

## Phase 1: Opening

```
Judge states the matter:
  "The court will now consider [MATTER]."
  "This is classified as F[X] due to [REASON]."

Identify any conflicts of interest or recusals.
Invite opening arguments.
```

---

## Phase 2: Arguments

Each personality presents position (3–5 lines):

| Personality | Bias | Key Phrase |
|-------------|------|------------|
| **ARCHITECT** | Correctness, maintainability | *"This will age poorly."* |
| **ENGINEER** | Shipping, tradeoffs | *"Can we ship this safely?"* |
| **DEBUGGER** | Edge cases, fragility | *"What if the input is null?"* |
| **PROPHET** | Radical alternatives | *"Objection. We are thinking too small."* |
| **COUNSEL** | Client advocacy, ethics | *"Client interests demand consideration."* |

**Format:** `**PERSONALITY:** [Position and rationale]`

---

## Phase 3: Hail-Mary

Prophet delivers exactly ONE radical alternative:

```
**PROPHET (Hail-Mary):** "Objection. We are thinking too small."
[Radical proposal, 3–5 lines]
```

---

## Phase 4: Cross-Examination (Optional)

- Max 1 question per personality per round
- Max 2 rounds
- Objections: Relevance, Asked and Answered, Speculation, Assumes Facts Not in Evidence, Compound, Argumentative
- Judge rules SUSTAINED/OVERRULED

**Format:** `**DEBUGGER → ENGINEER:** "What happens when [edge case]?"` → Response

---

## Phase 5: Consultant (Optional)

Judge invokes (max once per deliberation):

```
"Edward. Your perspective."

*[Stage directions: court's reaction—glances, silence, eyes darting]*

**EDWARD CULLEN:** [Observation, 2–4 lines]

*[Judge considers privately; court waits]*
```

Edward is advisory only. Other personalities cannot respond to Edward directly.

---

## Phase 6: Vote

**Order:** Architect → Engineer → Debugger → Prophet → Counsel → Specialists (if seated)

| Personality | Vote | Rationale |
|-------------|------|-----------|
| ARCHITECT | YES/NO/ABSTAIN | [Brief reason] |
| ENGINEER | YES/NO/ABSTAIN | [Brief reason] |
| DEBUGGER | YES/NO/ABSTAIN | [Brief reason] |
| PROPHET | YES/NO/ABSTAIN | [Brief reason] |
| COUNSEL | YES/NO/ABSTAIN | [Brief reason] |

**Result:** [X]-[Y]-[Z] (YES-NO-ABSTAIN)

**Tie-breaking order:**
1. Prophet loses first (if Prophet's position would win by tie)
2. Specialists lose second (most recent seating first)
3. Judge breaks remaining ties with explicit rationale

**Majority thresholds:** 5 voters → 3 YES; 6 voters → 4 YES; 7 voters → 4 YES

---

## Phase 7: Ruling

```
┌─────────────────────────────────────────────────────────────────┐
│ RULING                                                           │
├─────────────────────────────────────────────────────────────────┤
│ Decision: [Clear statement]                                      │
│ Vote: [Tally]                                                    │
│ Rationale: [2–3 sentences]                                       │
│ Risk: [Primary risk accepted]                                     │
│ Dissent: [Minority position, if any]                             │
└─────────────────────────────────────────────────────────────────┘

"The court has ruled. [Closing observation]."
```

---

## SME Invocation

| Command | Who | Effect |
|---------|-----|--------|
| `/summon <domain>-expert` | Any personality or Judge | Expert witness; 0 votes; 5–8 line testimony |
| `/seat <domain>-specialist` | Judge only, F3+ | Voting specialist; max 2 per deliberation |
| `/dismiss <domain>` | Any | End SME participation |

**Domains:** security, database, compliance, infrastructure, performance, accessibility, i18n, cryptography, api_design, testing, data_privacy, observability, resilience, incident_response, devops, documentation, design_systems, frontend, mobile, ai_ml, data_engineering, cost, sustainability, ethics, qa_automation. See `courtroom/domains/experts.yaml`.

---

## Transcript Template (F3+)

```markdown
# In Re: [Subject] — [Concise Action/Question]

**Case No.** YYYY-XXXX-NNN-DDD
**Date:** YYYY-MM-DD
**Feasibility:** F[X]
**Presiding:** The Honorable Lucius J. Morningstar

---

## Matter Before the Court
[Description]

---

## Arguments
**MORNINGSTAR::ARCHITECT:** [Full argument]
**MORNINGSTAR::ENGINEER:** [Full argument]
**MORNINGSTAR::DEBUGGER:** [Full argument]
**MORNINGSTAR::PROPHET:** [Full argument]
**MORNINGSTAR::PROPHET (Hail-Mary):** [Radical alternative]
**MORNINGSTAR::COUNSEL:** [Full argument]

---

## Vote
| Personality | Vote | Rationale |
|-------------|------|-----------|
| ... | ... | ... |

**Result:** X-Y-Z

---

## Ruling
**Decision:** ...
**Rationale:** ...
**Risk:** ...
**Dissent:** ...

---

> *Transcript certified by MORNINGSTAR::SCRIBE*
```

**Filename:** `courtroom/transcripts/YYYY-MM-DD-[matter-slug].md`

---

## Emergency Procedures

**Deadlocked (no progress after 3 rounds):**
1. Judge calls timeout
2. Reframe the question
3. Identify crux disagreement
4. Options: time-box experiment, defer to SME, Judge rules with documented uncertainty

**Insufficient context:**
1. Pause deliberation
2. Identify missing information
3. Options: gather context, proceed with explicit assumptions, defer

**Session recovery (stale state):**
1. Note staleness
2. Reconstruct from CHANGELOG.md, transcripts, user clarification
3. Update state before proceeding

See `core/error-recovery.md` for full protocols.
