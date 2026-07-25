# HANDOFF: LIL_JEFF → MORNINGSTAR — Repo Audit Advancements

**Case:** Audit 2026-02-17  
**From:** LIL_JEFF  
**To:** MORNINGSTAR  
**Status:** COMPLETE

---

## Summary

LIL_JEFF performed a full repo audit for missing documentation, broken links, and silent errors. Below are the **advancements delivered** for the court’s awareness and any follow-on precedent or runbook updates.

---

## Advancements Delivered

### 1. Silent error fixed: MFAF not loaded on case-sensitive filesystems

- **Issue:** Litigation loader requested `core/mfaf.md`; the repo file is `core/MFAF.md`. On Linux (case-sensitive) the loader received empty content and the Feasibility Assessment Framework was omitted from the system prompt with no error.
- **Change:** `litigation/prompts/sources.py` now loads `core/MFAF.md` (SOURCES key `"mfaf"` → `core_path("MFAF")`).
- **Impact:** Deliberations via the litigation runner now consistently include MFAF content on all platforms.

### 2. Broken links and path consistency: Portal

- **Issue:** Root README and courtroom/portal/README instructed users to run `./portal/launch.sh` and linked to `portal/*`, but the portal lives at **`courtroom/portal/`**; there is no root-level `portal/` directory.
- **Change:** All references updated to **`courtroom/portal/`** in:
  - **README.md** (root): Quick Start, Navigation Index table, Project Structure tree, How to Use, Where to find what.
  - **courtroom/portal/README.md**: Quick Start, export/generate commands, directory structure, troubleshooting (generate_manifest, viewer paths).
- **Impact:** Users following the docs can run the launcher and open linked files without 404 or “no such file.”

### 3. Missing template: Prophet vindication

- **Issue:** `courtroom/COURT_PROTOCOL.md` references “Use template: `templates/prophet-vindication.md`”; the file did not exist.
- **Change:** Added **`templates/prophet-vindication.md`** with required updates (state/current.md → prophetVindications, CHANGELOG “Warned” entry, optional narrative) per COURT_PROTOCOL.
- **Impact:** Prophet vindication procedure has a valid, editable template.

### 4. Documentation and audit record

- **Added:** **`docs/LIL_JEFF_AUDIT_REPO_2026-02-17.md`** — full audit write-up: findings (broken links, MFAF path, missing template, error-handling notes), improvements executed, and recommendations for MORNINGSTAR (precedent, runbook, optional LITIGATION_DEBUG).
- **Updated:** Root README now mentions the **litigation transcript viewer** (`litigation/viewer.py` — list/show/serve) alongside the courtroom portal.

---

## Recommendations for the Court

1. **Precedent (optional):** Add a short “Documentation and paths” precedent: portal and transcript viewer live at `courtroom/portal/` and `litigation/viewer.py`; MFAF is loaded from `core/MFAF.md`.
2. **Runbook:** Consider an entry: “If MFAF or other framework sections are missing from litigation prompts, verify loader paths match actual filenames (e.g. core/MFAF.md).”
3. **Optional future work:** Env flag (e.g. `LITIGATION_DEBUG=1`) to log when framework files are missing or unreadable in the loader (documented in audit; not implemented).

---

## Files Touched

| Path | Change |
|------|--------|
| `litigation/prompts/sources.py` | MFAF source → `core_path("MFAF")` |
| `README.md` | Portal paths → courtroom/portal/; litigation viewer mention; structure tree merged courtroom/portal |
| `courtroom/portal/README.md` | All root-relative paths → courtroom/portal/; related doc links fixed |
| `templates/prophet-vindication.md` | **New** — Prophet vindication template |
| `docs/LIL_JEFF_AUDIT_REPO_2026-02-17.md` | **New** — Full audit analysis |
| `courtroom/transcripts/HANDOFF-2026-LIL-JEFF-AUDIT.md` | **New** — This handoff |

---

*LIL_JEFF — Audit complete. Advancements delivered to MORNINGSTAR.*
