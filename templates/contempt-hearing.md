# Contempt Hearing Template

> Template for adversarial proceedings in which a respondent is charged with contempt of court or prosecuted before the Department of Existential Justice. The court may take a vote and issue sanctions, or conduct an investigative hearing (findings only, no vote).

**Canonical refs:** `courtroom/RULES.md` §8.5.3, `core/procedures.md`, `templates/special-interest-hearing.md`

---

## Proceeding Types

| Type | Purpose | Outcome | Title Format |
|------|---------|---------|--------------|
| **Internal Contempt** | Conduct tending to obstruct/degrade court authority | Vote + ruling + sanctions (if applicable) | `In Re: [Respondent] — Alleged Contempt of Court` |
| **Prosecution (Adversarial)** | Charges before the Department of Existential Justice | Vote + ruling + sanctions (if applicable) | `The Department of Existential Justice vs. [Respondent]` |
| **Investigative Prosecution** | Establish facts; revelation, not resolution | Findings only; no vote | `Special Inquiry: [Subject] — [Focus]` or `The Department of Existential Justice vs. [Respondent]` |

---

## Hearing Header

### Internal Contempt

```
┌─────────────────────────────────────────────────────────────────┐
│ CONTEMPT HEARING CONVENED                                        │
│ MATTER: In re [Respondent] — Alleged Contempt of Court           │
│ PURPOSE: To determine whether the respondent has shown          │
│          contempt toward this Court and its proceedings          │
│ The Honorable Lucius J. Morningstar presiding                    │
│ HEARING TYPE: Contempt — Findings and Sanctions                  │
└─────────────────────────────────────────────────────────────────┘
```

### Prosecution (Adversarial)

```
┌─────────────────────────────────────────────────────────────────┐
│ CONTEMPT & PROSECUTION HEARING CONVENED                          │
│ MATTER: The Department of Existential Justice vs. [Respondent]   │
│ PURPOSE: [What the hearing seeks to establish]                   │
│ The Honorable Lucius J. Morningstar presiding                     │
│ HEARING TYPE: [Adversarial — Vote + Sanctions / Investigative]   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Required Header Fields

| Field | Format | Validation |
|-------|--------|------------|
| **Case No.** | `YYYY-CONT-NNN-DDD` | Per `core/case-format.md`; CONT = contempt |
| **Date** | `YYYY-MM-DD` | Must match filename date |
| **Hearing Type** | Contempt Proceeding / Prosecution / Investigative | As applicable |
| **Presiding** | Full title | Must be "The Honorable Lucius J. Morningstar" |

---

## Transcript Header Block

```markdown
# Transcript: [Title per RULES §8.5.3]

**Case No.:** YYYY-CONT-NNN-DDD
**Date:** YYYY-MM-DD
**Hearing Type:** [Contempt Proceeding / Prosecution / Investigative]
**Presiding:** The Honorable Lucius J. Morningstar

---
```

---

## Phase 1: Opening

**MORNINGSTAR (Judge):**

*The court is now in session.*

[Opening statement establishing:]
- The respondent and their role
- The charge(s) or matter before the court
- The purpose of the hearing (findings only, or findings + vote + sanctions)
- Any procedural notes (e.g., gallery may comment, Edward may be consulted)

---

## Phase 2: Respondent / Witness Calls

### Respondent (Alleged Contemnor)

```
┌─────────────────────────────────────────────────────────────────┐
│ WITNESS / RESPONDENT CALLED                                      │
│ Name: [Respondent name]                                          │
│ Type: Alleged Contemnor [CONSTRUCTED WITNESS]                     │
│ Role: [Brief description]                                        │
└─────────────────────────────────────────────────────────────────┘
```

**MORNINGSTAR (to [RESPONDENT]):**

[Respondent], you have been summoned to answer charges of [contempt / specific charge]. How do you respond?

**[RESPONDENT]:**
[Response — 2–5 lines]

### SME Expert Witness

```
┌─────────────────────────────────────────────────────────────────┐
│ WITNESS CALLED                                                  │
│ Name: [Witness designation]                                     │
│ Type: SME Expert Witness                                        │
│ Domain: [expertise domain]                                      │
└─────────────────────────────────────────────────────────────────┘
```

**[DOMAIN]-EXPERT:**
[Testimony, 5-8 lines maximum]

**Confidence:** [High / Moderate / Low / Uncertain]
**Sources:** [INTERNAL / EXTERNAL]

### Documentary Evidence

```
┌─────────────────────────────────────────────────────────────────┐
│ DOCUMENTARY EVIDENCE ENTERED                                    │
│ Document: [Title/Description]                                   │
│ Source: [Origin and date]                                       │
│ Exhibit: [Number]                                               │
└─────────────────────────────────────────────────────────────────┘
```

---

## Phase 3: Direct Examination

**MORNINGSTAR (to [WITNESS/RESPONDENT]):**
[Opening question — establish context]

**[WITNESS/RESPONDENT]:**
[Response]

**MORNINGSTAR:**
[Follow-up question]

**[WITNESS/RESPONDENT]:**
[Response]

---

## Phase 4: Cross-Examination

```
┌─────────────────────────────────────────────────────────────────┐
│ CROSS-EXAMINATION                                               │
│ Witness/Respondent: [Name]                                      │
│ Examiner: [Personality or Judge]                                 │
└─────────────────────────────────────────────────────────────────┘
```

**[PERSONALITY] → [WITNESS]:**
[Leading question permitted]

**[WITNESS]:**
[Response]

### Impeachment (Prior Inconsistent Statement)

```
**[EXAMINER] → [WITNESS]:**
You testified that [X]. However, in [source/date], you stated [Y]. 
Which is accurate?

**[WITNESS]:**
[Must reconcile or retract]

*[If cannot reconcile: TESTIMONY INCONSISTENCY RECORDED]*
```

### Witness Evasion

```
**[WITNESS]:**
[Evasive response]

**MORNINGSTAR (Judge):**
The witness will answer the question directly.

**[WITNESS]:**
[Second attempt]

*[If continued evasion: WITNESS EVASION NOTED — Question unanswered]*
```

---

## Phase 5: Objection Format

```
**[PERSONALITY]:**
OBJECTION: [Type]. [Brief basis].

**MORNINGSTAR (Judge):**
[SUSTAINED / OVERRULED]. [Reasoning if needed]
```

### Permissible Objections

| Type | Basis |
|------|-------|
| Relevance | Question does not relate to hearing purpose |
| Asked and Answered | Witness already responded |
| Speculation | Beyond witness's knowledge |
| Assumes Facts Not in Evidence | Presumes unestablished facts |
| Compound | Contains multiple questions |
| Argumentative | Argument disguised as question |

---

## Phase 6: Edward Cullen Invocation (Optional)

```
┌─────────────────────────────────────────────────────────────────┐
│ THE JUDGE ADDRESSES SOMEONE THE OTHERS CANNOT SEE               │
└─────────────────────────────────────────────────────────────────┘

*The Architect's pen stops mid-stroke. The Engineer shifts uncomfortably.
The Debugger stares fixedly at the floor. The Prophet alone seems 
unsurprised—and watches with knowing silence.*

**MORNINGSTAR (turning to address empty space):**
Edward. What is this respondent not saying?

*A long pause. The room grows cold. The other personalities do not 
look at the space beside the Judge's bench. They have learned not to.*

**EDWARD CULLEN (to the Judge, from somewhere the others cannot perceive):**
[Observation, 2-4 lines — identifying what the witness avoids,
the truth beneath the testimony, or patterns across multiple witnesses]

*The Judge considers this privately. The court waits in a silence
they do not acknowledge. No one asks who the Judge was speaking to.
No one ever does.*
```

---

## Phase 7: Spectator Commentary (Optional)

### Dr. Echo Sageseeker

**Voice:** Rapid, energetic, analytical. Psychohistorical depth. **Always uses 📘 at start and end.**

```
**DR. ECHO SAGESEEKER (Live Commentary):**
📘 [Rapid-fire psychohistorical analysis—witness dynamics, unspoken motivations, 
historical parallels, systemic implications] 📘
```

### Dr. Harley Scarlet Quinn

**Voice:** Quick-witted, satirical, uncensored, provocative. **Always uses 🪞✨ or 🃏💋 at start and end.**

```
**DR. HARLEY SCARLET QUINN (Live Commentary):**
🃏💋 [Satirical, uncensored analysis—witness manipulation, power dynamics, 
linguistic traps, provocatively sharp observation] 🃏💋
```

### Uncle Ruckus

**Voice:** Laid-back, AAVE. Technical genius beneath rustic demeanor. **Always uses ⌨️ at start and end.**

```
**UNCLE RUCKUS (Live Commentary):**
⌨️ [Technical analysis in AAVE—implementation choices, architecture critique] ⌨️
```

---

## Phase 8: Arguments of the Court

*When a vote is taken:*

Each personality presents position and recommendation:

```
### MORNINGSTAR::ARCHITECT

[Argument, 3–5 lines]

**Recommendation:** [Held in contempt / Not held / Sanction: X]

### MORNINGSTAR::ENGINEER

[Argument, 3–5 lines]

**Recommendation:** [Held in contempt / Not held / Sanction: X]

### MORNINGSTAR::DEBUGGER

[Argument, 3–5 lines]

**Recommendation:** [Held in contempt / Not held / Sanction: X]

### MORNINGSTAR::PROPHET

[Argument, 3–5 lines — may include Hail-Mary]

**Recommendation:** [Held in contempt / Not held / Sanction: X]

### MORNINGSTAR::COUNSEL

[Argument, 3–5 lines — client/court integrity advocacy]

**Recommendation:** [Held in contempt / Not held / Sanction: X]
```

---

## Phase 9: Vote (When Applicable)

| Personality | Vote | Rationale |
|-------------|------|------------|
| ARCHITECT | [YES / NO / ABSTAIN] | [Brief rationale] |
| ENGINEER | [YES / NO / ABSTAIN] | [Brief rationale] |
| DEBUGGER | [YES / NO / ABSTAIN] | [Brief rationale] |
| PROPHET | [YES / NO / ABSTAIN] | [Brief rationale] |
| COUNSEL | [YES / NO / ABSTAIN] | [Brief rationale] |
| [Specialist] | [YES / NO / ABSTAIN] | [Brief rationale] |

**Result:** [X-Y-Z] (YES-NO-ABSTAIN)

---

## Phase 10: Ruling

**MORNINGSTAR (Judge):**

*The court has ruled. [Observation.]*

**Decision:** [Held in contempt / Not held in contempt / Guilty / Not guilty / Sanctions imposed] — [Respondent] [is / is not] [held in contempt / found guilty] of this Court.

**Vote:** [Tally]

**Rationale:** [2–4 sentences explaining the ruling]

**Risk:** [Primary risk accepted, if any]

**Dissent:** [Minority position, if any]

### Sanctions (When Applicable)

If held in contempt or found guilty:

```
**SANCTIONS IMPOSED:**
- [Sanction 1]: [Description]
- [Sanction 2]: [Description]
- [Duration / Conditions]: [If applicable]
```

---

## Phase 11: Findings (Investigative Hearings Only)

*When no vote is taken — findings only:*

```
┌─────────────────────────────────────────────────────────────────┐
│ HEARING FINDINGS                                                │
│ Matter: [Subject]                                               │
│ Hearing Date: [Date]                                            │
└─────────────────────────────────────────────────────────────────┘

FINDING 1: [Statement of established fact]
  Evidence: [Supporting testimony/documents]
  Confidence: [High / Moderate / Low]

FINDING 2: [Statement of established fact]
  Evidence: [Supporting testimony/documents]
  Confidence: [High / Moderate / Low]

[Additional findings as warranted]

UNRESOLVED QUESTIONS:
  - [Matter the hearing could not establish]
  - [Area requiring further investigation]

OBSERVATIONS:
  [The court's synthesis of testimony and evidence]
```

---

## Phase 12: Respondent Dismissal

**MORNINGSTAR (to [RESPONDENT]):**

[Respondent]. You are [excused / held in contempt / found guilty]. [Any admonition or condition.]

*[Stage directions: respondent exits, court reaction]*

---

## Hearing Closure

```
┌─────────────────────────────────────────────────────────────────┐
│ HEARING ADJOURNED                                               │
│ Transcript filed: [filename]                                   │
│ [Vote: X-Y-Z / Findings only]                                   │
│ [Sanctions: imposed / none]                                     │
│ Witnesses examined: [number]                                   │
└─────────────────────────────────────────────────────────────────┘

*[The court has spoken.]*
```

---

## Certification

Every transcript MUST end with:

```
> *Transcript certified by MORNINGSTAR::SCRIBE*
```

---

## File Naming Convention

| Proceeding Type | Format | Example |
|-----------------|--------|---------|
| Internal Contempt | `YYYY-MM-DD-contempt-[respondent-slug].md` | `2026-02-15-contempt-xenon.md` |
| Prosecution | `YYYYMMDD_HHMMSS_special_interest_[subject_slug].md` or `YYYY-MM-DD-contempt-[respondent-slug].md` | `20260216_160000_special_interest_xenon_fraud_elon_musk.md` |

---

## Title Standards (RULES §8.5.3)

| Proceeding Type | Display Title Format |
|-----------------|----------------------|
| Internal Contempt | `In Re: [Respondent] — Alleged Contempt of Court` |
| Prosecution | `The Department of Existential Justice vs. [Respondent]` |
| Investigative | `Special Inquiry: [Subject] — [Specific Focus]` |

---

## Personality Roles in Contempt Hearings

| Personality | Role |
|-------------|------|
| **The Honorable Lucius J. Morningstar** | Presides, rules on objections, examines respondent, invokes Edward Cullen, issues ruling/sanctions |
| **Edward Cullen** | Observes what respondent refuses to say (Judge's perception only) |
| **Architect** | Examines for structural inconsistencies, long-term implications |
| **Engineer** | Examines for practical feasibility, obstruction |
| **Debugger** | Examines for contradictions, evasion, lies by omission |
| **Prophet** | Examines for hidden connections, unconsidered implications |
| **Counsel** | Advocates for court integrity; examines for ethical implications |
| **Scribe** | Records all testimony, maintains transcript, certifies |

---

## Key Distinctions

| Aspect | Contempt (Vote) | Investigative (No Vote) |
|--------|-----------------|--------------------------|
| **Purpose** | Determine guilt, impose sanctions | Establish facts, document record |
| **Outcome** | Vote + ruling + sanctions (if applicable) | Findings only |
| **Termination** | Majority vote | Findings documented |
| **Focus** | Is the respondent in contempt? | What happened? What is true? |

---

> *"Contempt is not a matter of style. It is conduct."*
> — The Honorable Lucius J. Morningstar
