# Transcript: In Re: Case Naming & Case Numbering Format

**Case No.:** 2026-DOC-001-001
**Date:** 2026-02-19
**Feasibility:** F4
**Presiding:** The Honorable Lucius J. Morningstar

---

## Matter Before the Court

The court convenes to establish a formal CASE NAMING and CASE NUMBERING FORMAT for the MORNINGSTAR framework. Current state: inconsistent use of Case No. vs Matter ID; short form (2026-DEL-004) vs full form (2026-DEL-004-001); multiple transcripts sharing same case number (2026-DEL-001); undefined category codes; mixed filename conventions. Goal: smooth identification, recall, and searching for transcripts and precedents.

---

## Arguments

**MORNINGSTAR::ARCHITECT:** Canonical format `YYYY-CATC-NNN-DDD`. Define CATC explicitly. One Case ID per transcript. Filename include case for traceability. Single source of truth: core/case-format.md.

**MORNINGSTAR::ENGINEER:** Minimal change. Keep YYYY-MM-DD-slug filenames. Require `Case No.:` in header. Deprecate Matter ID. Define categories in RULES or procedures. Tools parse; content is authoritative.

**MORNINGSTAR::DEBUGGER:** Case registry to assign next NNN per category; prevents collision. Migration rule for legacy. Reporter validates for duplicate Case IDs.

**MORNINGSTAR::PROPHET:** Content-addressed or RFC-style numbering. Human IDs collide; hashes/UUIDs don't. Search by slug or path.

**MORNINGSTAR::COUNSEL:** Human-readable, citable IDs serve the user. YYYY-CATC-NNN-DDD is memorable. Add canonical case-title format for display.

---

## Hail-Mary

**MORNINGSTAR::PROPHET (Hail-Mary):** RFC-style: DRAFT-CASE-2026-01, 02, etc. One sequence. No per-category NNN. Simpler.

---

## Vote

| Personality | Vote | Rationale |
|-------------|------|-----------|
| ARCHITECT | YES | Canonical format, defined categories, single source of truth |
| ENGINEER | YES | Standardize header; keep filenames; implement via tooling |
| DEBUGGER | YES | Registry prevents collision; migration rule for legacy |
| PROPHET | NO | RFC-style or content-addressed better; per-category NNN is complexity |
| COUNSEL | YES | Human-readable, citable IDs serve user |

**Result:** 4-1-0 (YES-NO-ABSTAIN)

---

## Ruling

**Decision:** Adopt formal Case Naming & Case Numbering Format per core/case-format.md. Format: YYYY-CATC-NNN-DDD. Category codes: ARCH, INFRA, DEL, CONT, SEC, EXEC, FEAT, BUG, MAINT, DOC. Case registry at courtroom/case-registry.yaml. Deprecate Matter ID; use Case No. only. Legacy transcripts grandfathered.

**Vote:** 4-1-0
**Rationale:** Canonical format enables identification, recall, search. Registry prevents collision. Grandfather rule avoids mass migration.
**Risk:** Legacy migration deferred; some transcripts keep non-canonical IDs.
**Dissent:** Prophet preferred RFC-style or content-addressed numbering.

---

> *Transcript certified by MORNINGSTAR::SCRIBE*
