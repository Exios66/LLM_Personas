# Handoff: Case 2026-INFRA-002 — Second Slate of 10 Enhancements

**From:** Court of MORNINGSTAR  
**To:** LIL_JEFF (primary), OCTAVIUS (where R/Quarto or data tooling applies)  
**Date:** 2026-02-15  
**Case:** 2026-INFRA-002  
**Vote:** 4-0-0 Unanimous

---

## Instructions for Implementers

1. **LIL_JEFF** is the primary implementer for all 10 items. Deliver complete, production-ready artifacts; no placeholders.
2. **OCTAVIUS** may be invoked for any item that involves R, Quarto, or data-science workflows (e.g. generating a transcript manifest with a script). Otherwise LIL_JEFF executes.
3. Implement in the order listed below where dependencies suggest it. Cross-reference existing docs (README, core/, courtroom/, portal/) and maintain the project’s formal tone.
4. When done, update CHANGELOG.md with an entry for “Second Enhancement Slate (2026-INFRA-002)” and reference this handoff.

---

## Enhancement Specifications

### 1. SME Failure Tracking File

- **File:** `state/sme-failures.md`
- **Purpose:** Record when SME (Witness or Specialist) input led to poor outcomes, for institutional learning.
- **Content:** Template and schema consistent with `core/sme-framework.md` “SME Failure Tracking” (domain, date, matter, what went wrong, lesson). Include a short header explaining purpose and how to add entries. Start with no entries; structure only.

### 2. Dissolution Protocol

- **Location:** Add a new section to `core/procedures.md` (or a subsection in `courtroom/BEST_PRACTICES.md`) titled “Dissolution Protocol” or “When Not to Convene.”
- **Purpose:** Formal criteria for when the court should *not* deliberate (e.g. F0 trivial, pure implementation with no tradeoff, matter already decided by precedent).
- **Content:** Bullet or numbered criteria; reference F0–F5 and “No Deliberation Needed” from README. Keep to one short page.

### 3. Glossary / Term Index

- **File:** `docs/glossary.md` (create `docs/` if missing), or a new “Glossary” section in README.
- **Purpose:** Single place to look up: MORNINGSTAR, F0–F5, SME, Expert Witness, Specialist, Prophet vindication, tie-breaking, key file names (state/current.md, RULES.md, etc.).
- **Content:** Alphabetical or categorized terms with one- or two-line definitions. Link to relevant docs where helpful.

### 4. Precedent Citation Shorthand

- **Location:** `courtroom/precedents.md` (add a “Citation format” or “How to cite” subsection if not already clear) and optionally a one-line note in `courtroom/RULES.md` or `courtroom/BEST_PRACTICES.md`.
- **Purpose:** Standard way to cite a case in transcripts and rulings (e.g. “See 2026-INFRA-001-001” or “Per Case 2026-INFRA-001-001”).
- **Content:** Define the canonical form (e.g. Case ID only, or “Case ID (Date)”) and one example. No need to change existing precedent entries unless clarifying.

### 5. OCTAVIUS Handoff in Inter-Agent Protocol

- **File:** `core/inter-agent-protocol.md`
- **Purpose:** Document when and how MORNINGSTAR or LIL_JEFF defers to OCTAVIUS (R/Quarto/tidyverse/tidymodels/statistical computing).
- **Content:** New subsection or short section: when to hand off to Octavius, what to pass (e.g. task description, paths to data or scripts), and any response format expectations. Cross-link to OCTAVIUS agent and `octavius_core/THE_RULES.md`.

### 6. Onboarding One-Pager

- **File:** `docs/ONBOARDING.md` (or equivalent “Start here” at top of README).
- **Purpose:** Single page for a new user: what this repo is, the three agents (MORNINGSTAR, LIL_JEFF, OCTAVIUS), how to run the portal, how to run a first deliberation, and where to find more (README, Navigation Index).
- **Content:** Short bullets or numbered steps; links to README, portal/README, and core docs. No long prose.

### 7. Portal Transcript Discovery

- **Location:** `portal/`
- **Purpose:** Viewer should not rely only on hardcoded `KNOWN_TRANSCRIPTS` in viewer.html. Prefer: a small manifest (e.g. JSON or text list) generated from `courtroom/transcripts/*.md`, or a script that updates a list used by the viewer.
- **Content:** Either (a) a script (e.g. Python or shell) that writes a manifest of transcript basenames (and optionally titles/dates) into a file the viewer can fetch, or (b) documentation that the launch script or generate step produces such a list and how the viewer consumes it. Viewer.html may be updated to read from that source when available; fallback to KNOWN_TRANSCRIPTS if not.

### 8. State Backup Recommendation

- **Location:** `core/procedures.md` and/or `core/error-recovery.md`
- **Purpose:** Recommend checkpointing/backing up state (e.g. `state/current.md`) before major or risky sessions.
- **Content:** One short subsection: “State backup” or “Pre-session checkpoint” with when to do it and how (e.g. copy state/current.md to state/backups/YYYY-MM-DD-current.md or similar). Link from error-recovery if appropriate.

### 9. Runbook / Troubleshooting Index

- **File:** `docs/RUNBOOK.md` (or a “Troubleshooting” / “Runbook” section in README).
- **Purpose:** One place to find: portal not launching, state corrupted, “no transcripts,” SME summoning fails, which agent to use, where error-recovery and portal README live.
- **Content:** Short scenarios with “If X, then do Y” and links to error-recovery.md, portal/README.md, sme-framework.md, inter-agent-protocol.md. One page or less.

### 10. Edge Case Registry

- **File:** `docs/edge-cases.md` (or `courtroom/edge-cases.md`).
- **Purpose:** Document known edge cases and limitations (e.g. viewer with file://, missing state file, transcript naming, etc.) so operators and future implementers know what to expect.
- **Content:** List of short entries: scenario, expected behavior or limitation, workaround or “by design.” Reference portal README and state-schema where relevant. Can be seeded from existing known issues (e.g. file:// fetch limits).

---

## Completion Checklist

- [ ] 1. `state/sme-failures.md` created with template and schema
- [ ] 2. Dissolution Protocol section added (procedures or BEST_PRACTICES)
- [ ] 3. `docs/glossary.md` (or README Glossary) created
- [ ] 4. Precedent citation shorthand documented (precedents.md and/or RULES/BEST_PRACTICES)
- [ ] 5. OCTAVIUS handoff added to `core/inter-agent-protocol.md`
- [ ] 6. `docs/ONBOARDING.md` (or README “Start here”) created
- [ ] 7. Portal transcript discovery implemented (manifest or script + viewer update or doc)
- [ ] 8. State backup recommendation added (procedures and/or error-recovery)
- [ ] 9. `docs/RUNBOOK.md` (or README Runbook section) created
- [ ] 10. `docs/edge-cases.md` (or courtroom equivalent) created
- [ ] CHANGELOG.md updated with Second Slate entry

---

*Handoff certified by MORNINGSTAR::SCRIBE. Implementation by LIL_JEFF and OCTAVIUS.*
