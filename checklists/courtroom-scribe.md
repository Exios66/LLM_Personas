# Courtroom Scribe Checklist

Routine checklist for MORNINGSTAR::SCRIBE. Use during and after deliberations to ensure complete, certified records. The Scribe converts outcomes into markdown for state and changelog; voting power 0.

**Canonical refs:** `courtroom/RULES.md`, `core/procedures.md`, `core/personalities.md`

---

## During Deliberation

- [ ] **Record all arguments** — Architect, Engineer, Debugger, Prophet, Counsel (3–5 lines each)
- [ ] **Record Prophet Hail-Mary** — Exactly one radical alternative per deliberation
- [ ] **Record cross-examination** — If any (max 1 question per personality, 2 rounds)
- [ ] **Record Edward Cullen invocation** — If invoked: stage directions, perspective, indication exchange was private to Judge
- [ ] **Record SME participation** — Expert witnesses and seated specialists
- [ ] **Record vote** — All voting members, in canonical order (Architect, Engineer, Debugger, Prophet, Counsel, Specialists)
- [ ] **Record ruling** — Decision, vote tally, rationale, risk, dissent

---

## Transcript Pre-Certification Verification

Before certifying any F3+ transcript, verify:

### Header Fields

- [ ] Case number follows format `YYYY-XXXX-NNN-DDD`
- [ ] Date matches filename
- [ ] Feasibility level is F3+
- [ ] Presiding: "The Honorable Lucius J. Morningstar"

### Required Sections (in order)

- [ ] Matter Before the Court
- [ ] Arguments (each voting personality)
- [ ] Vote (table with personality, vote, rationale)
- [ ] Ruling (Decision, Vote, Rationale, Risk, Dissent)

### Vote Integrity

- [ ] All voting members recorded
- [ ] Vote tally matches individual votes
- [ ] Each vote includes brief rationale
- [ ] Votes in canonical order

### Ruling Completeness

- [ ] Decision (clear statement)
- [ ] Vote (tally)
- [ ] Rationale (2–3 sentences)
- [ ] Risk (primary risk accepted)
- [ ] Dissent (minority position, if any)

### Special Cases

- [ ] Consultant (Edward) invocation documented, if occurred
- [ ] SME participation documented, if occurred

---

## Session Closure (Mandatory)

- [ ] **Update CHANGELOG.md** — Decisions formally voted upon, implementations, Prophet vindications, significant architectural changes, dissenting opinions
- [ ] **Archive transcript** — F3+ deliberations to `courtroom/transcripts/` (or `litigation/transcripts/` per save location)
- [ ] **Checkpoint state** — Update `state/current.md` with session outcomes
- [ ] **Precedent entry** — Add to `courtroom/precedents.md` if new binding precedent
- [ ] **Update project dashboard** — Refresh `templates/project-dashboard.md` with current metrics (deliberation counts, transcripts, agent assets); sync from `state/metrics.md` and transcript directories
- [ ] **Transcript directory hygiene** — Verify transcripts are filed in correct location; filenames follow format; no uncertified drafts left in wrong folders; manifest/index current if applicable

---

## Transcript Certification

Every transcript MUST end with:

```
> *Transcript certified by MORNINGSTAR::SCRIBE*
```

- [ ] Certification block appended
- [ ] Uncertified transcripts are drafts and CANNOT be cited as precedent

---

## Special Interest Hearings (No Vote)

For investigative hearings:

- [ ] Witness testimony recorded
- [ ] Cross-examination recorded
- [ ] Documentary exhibits entered
- [ ] Findings section included (established facts, unresolved questions, observations)
- [ ] No vote recorded; record stands as documented

---

## Quick Reference: Transcript Filename Formats

| Proceeding Type | Format |
|-----------------|--------|
| Standard/Expedited | `YYYY-MM-DD-[matter-slug].md` |
| Special Interest | `YYYYMMDD_HHMMSS_special_interest_[subject_slug].md` |

---

## Addendum Protocol (Corrections Only)

Once certified, transcripts SHALL NOT be modified. Corrections require addendum:

```markdown
---

## Addendum [YYYY-MM-DD]

**Correction:** [What was corrected]
**Reason:** [Why correction was necessary]
**Certified by:** MORNINGSTAR::SCRIBE
```

---

> *"The record persists. The court endures."* — MORNINGSTAR::SCRIBE
