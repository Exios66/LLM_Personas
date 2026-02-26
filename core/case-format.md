# MORNINGSTAR Case Naming & Case Numbering Format

> *"A case without a number is a case without a home."*  
> — MORNINGSTAR::ARCHITECT

**Authority:** Court ruling 2026-02-19 (Case Naming & Numbering deliberation). Vote: 4-1-0.  
**Canonical ref:** This document is the single source of truth for case identification. All references to transcript naming, Case No. format, precedent indexing, and session IDs point here.

---

## Formatted Conventions (Quick Reference)

| Convention | Format | Example |
|------------|--------|---------|
| **Case No.** (transcript header) | `YYYY-CATC-NNN-DDD` | `2026-DEL-004-001` |
| **Session ID** (state/current.md) | `YYYY-CATC-NNN` | `2026-DEL-004` |
| **Standard transcript** | `YYYY-MM-DD-[matter-slug].md` | `2026-02-19-case-naming-and-numbering-format.md` |
| **Special Interest transcript** | `YYYYMMDD_HHMMSS_special_interest_[subject].md` | `20260216_160000_special_interest_api_design.md` |
| **Handoff document** | `HANDOFF-YYYY-CATC-NNN.md` | `HANDOFF-2026-ARCH-002.md` |
| **Header label** | `Case No.:` | *(deprecate Matter ID)* |

**Category codes:** ARCH, INFRA, DEL, CONT, SEC, EXEC, FEAT, BUG, MAINT, DOC.

**Transcript storage:** `courtroom/transcripts/` or `litigation/transcripts/` (same naming in both).

---

## Case ID Format

```
YYYY-CATC-NNN-DDD
```

| Segment | Meaning | Values |
|---------|---------|--------|
| **YYYY** | Year | 4-digit (e.g., 2026) |
| **CATC** | Category code | See [Category Codes](#category-codes) |
| **NNN** | Matter sequence | 001-999 within category per year |
| **DDD** | Deliberation sequence | 001-999 within matter (first deliberation = 001) |

**Examples:**

- `2026-INFRA-001-001` — First deliberation of first infrastructure matter in 2026
- `2026-DEL-004-001` — First deliberation of fourth general deliberation matter in 2026
- `2026-CONT-001-001` — First contempt proceeding in 2026

---

## Session ID (Short Form)

For `state/current.md` and session context, use the short form **without DDD**:

```
YYYY-CATC-NNN
```

Example: `Session: 2026-DEL-004`. Full Case No. (with DDD) is used in transcripts and precedent citations.

---

## Category Codes

| Code | Meaning | Use |
|------|---------|-----|
| **ARCH** | Architectural decisions | Agent structure, protocols, framework design |
| **INFRA** | Infrastructure work | Enhancements, tooling, foundational changes |
| **DEL** | General deliberation | Full court proceedings not fitting other categories |
| **CONT** | Contempt proceedings | Contempt hearings, adversarial proceedings |
| **SEC** | Special inquiry / Security | Special Interest hearings, security posture |
| **EXEC** | Executive branch | Executive-orchestration matters |
| **FEAT** | Feature development | Feature adoption, capability addition |
| **BUG** | Bug investigation | Defect root cause, remediation |
| **MAINT** | Maintenance | Refactors, tech debt, cleanup |
| **DOC** | Documentation | Doc structure, glossary, onboarding |

---

## Transcript Header (Required)

Every F3+ transcript SHALL include:

```markdown
**Case No.:** YYYY-CATC-NNN-DDD
**Date:** YYYY-MM-DD
**Feasibility:** F[3-5]
**Presiding:** The Honorable Lucius J. Morningstar
```

**Additional fields for contempt hearings:** `**Hearing Type:**` (Contempt Proceeding / Prosecution / Investigative).

**Date matching:** The header **Date** MUST match the filename date: Standard transcripts use `YYYY-MM-DD` from the filename; Special Interest transcripts use the date parsed from the `YYYYMMDD` prefix.

**Deprecated:** `Matter ID` — use `Case No.:` only. The portal and `generate_manifest.py` prefer `Case No.:` but accept `Matter ID` for legacy transcripts.

---

## Case Title Format (Display)

For human-readable display and precedent indexing:

| Proceeding Type | Format | Example |
|-----------------|--------|---------|
| Standard / Expedited | `In Re: [Subject] — [Concise Action]` | In Re: Framework Enhancements — Ratification of Slate 1 |
| Special Interest | `Special Inquiry: [Subject] — [Focus]` | Special Inquiry: Bohemian Grove — Structure, Influence |
| Contempt | `In Re: [Respondent] — Alleged Contempt` or `DOJ vs. [Respondent]` | In Re: Xenon — Alleged Contempt of Court |
| Handoff | `Docket: [Case ID] — [Phase/Action]` | Docket: 2026-ARCH-002 — Implementation Handoff |

---

## Filename Formats

| Type | Format | Example |
|------|--------|---------|
| Standard / Expedited | `YYYY-MM-DD-[matter-slug].md` | 2026-02-17-full-session-skills-to-add-to-each-agent.md |
| Special Interest | `YYYYMMDD_HHMMSS_special_interest_[subject].md` | 20260216_160000_special_interest_xenon_fraud_elon_musk.md |
| Handoff | `HANDOFF-YYYY-CATC-NNN.md` | HANDOFF-2026-ARCH-002.md |

**Slug rules:** Lowercase, hyphens (not underscores), URL-safe, descriptive. Use `[matter-slug]` or `[subject_slug]` as appropriate.

**Storage locations:** Transcripts may be saved to `courtroom/transcripts/` or `litigation/transcripts/`. Same filename convention applies in both. The portal and Court Reporter scan both directories.

**Filename vs header:** The filename does not require the Case No. The Case No. resides in the transcript header.

---

## Legacy Filename Format (Grandfathered)

Older transcripts may use `YYYYMMDD_HHMMSS_topic.md` (no `special_interest_`). The portal and launch script support this for backward compatibility. **New transcripts** SHALL use the canonical Special Interest format: `YYYYMMDD_HHMMSS_special_interest_[subject].md`.

---

## Case Registry

**Location:** `courtroom/case-registry.yaml`

The registry holds the next available NNN per category per year. The Scribe (or Judge) assigns case IDs from it to prevent collisions.

**Assignment rule:** When convening a new matter, check the registry for the next NNN in the chosen category. Increment and record. If the matter continues (e.g., second deliberation on same matter), increment DDD only; NNN stays the same.

**Registry structure (YAML):** `year`, `last_updated`, and `categories: { ARCH: n, DEL: n, ... }` with next NNN per category.

---

## Precedent Indexing

When adding certified transcripts to `courtroom/precedents.md`, extract:

- **Case No.** — `YYYY-CATC-NNN-DDD` from header
- **Date** — from header or filename
- **Matter** — brief title or subject
- **Ruling** — decision summary
- **Vote** — tally (e.g., 4-1-0)

Add to the Master Index and to the appropriate category table. See `courtroom/precedents.md` for entry schema.

---

## Citation Format

- **In text:** `See Case 2026-DEL-004-001` or `Per 2026-INFRA-001-001`
- **In precedents:** Full Case ID in Master Index
- **In handoffs:** `Case: 2026-ARCH-002` (short form acceptable for handoff docs)

---

## Reconstructed Transcripts

When a transcript is recovered from CHANGELOG, state, or other sources, mark it in the header:

```markdown
**Case No.:** YYYY-CATC-NNN-DDD [RECONSTRUCTED]
```

Document sources used in reconstruction. Reconstructed transcripts have reduced precedential weight.

---

## Validation

The Court Reporter (`courtroom/reporter.py`) and `courtroom/portal/generate_manifest.py` SHALL:

1. **Check filename format** — Standard (`YYYY-MM-DD-*`) or Special Interest (`YYYYMMDD_HHMMSS_special_interest_*`). Legacy `YYYYMMDD_HHMMSS_*` grandfathered.
2. **Extract Case No.** — Prefer `**Case No.:**` in header; fall back to `**Matter ID:**` for legacy transcripts.
3. **Validate Case No. format** — Regex: `\d{4}-[A-Z]+-\d{3}(?:-\d+)?` (DDD optional for short form).
4. **Report collisions** — No duplicate Case No. across transcripts; flag for resolution.

---

## Legacy Transcripts

Transcripts created before this ruling may have non-canonical case numbers (e.g., multiple transcripts sharing 2026-DEL-001). **Grandfather rule:** Do not mass-rename or edit certified transcripts. When a legacy transcript is cited or updated, assign a canonical Case No. via addendum if needed. New transcripts SHALL use the canonical format from first line.

---

> *"The number persists. The case endures. The record is findable."*  
> — MORNINGSTAR::SCRIBE
