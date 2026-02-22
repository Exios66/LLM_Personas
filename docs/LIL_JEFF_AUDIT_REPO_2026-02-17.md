# LIL_JEFF Repo Audit — 2026-02-17

**Scope:** Missing documentation, broken links, silent errors.  
**Delivered to:** MORNINGSTAR (advancements summary in handoff).

---

## 1. Executive Summary

| Category | Findings | Severity |
|----------|----------|----------|
| **Broken links** | Root README and others reference `portal/` but portal lives at `courtroom/portal/`; one template reference to non-existent file | High (user-facing), Medium |
| **Silent errors** | MFAF loaded via `core/mfaf.md` while repo has `core/MFAF.md` (case mismatch → empty MFAF on case-sensitive FS) | High |
| **Missing docs** | `templates/prophet-vindication.md` referenced in COURT_PROTOCOL.md but file absent | Medium |
| **Documentation gaps** | Litigation viewer not mentioned in root README; portal path inconsistency | Low |
| **Error handling** | Loader and some code use `except Exception: pass`; acceptable where fallback is documented; one path bug causes silent empty content | See below |

---

## 2. Broken Links & Paths

### 2.1 Portal path inconsistency (HIGH)

- **Fact:** The transcript portal lives at **`courtroom/portal/`** (launch.sh, export_transcript.py, viewer.html, README.md, generate.py, etc.).
- **Problem:** Root **README.md** and **courtroom/portal/README.md** instruct users to run `./portal/launch.sh` and link to `portal/README.md`, `portal/export_transcript.py`, `portal/viewer.html`. There is **no `portal/` directory at repo root**; only `courtroom/portal/` exists.
- **Impact:** Users following the docs get "No such file or directory" or 404s when opening linked files.
- **Fix applied:** Update root README and courtroom/portal/README to use **`courtroom/portal/`** consistently (paths and links). Add one-line note in root README that the portal lives under `courtroom/portal/`.

### 2.2 MFAF filename case (HIGH — silent failure)

- **Fact:** Repo has **`core/MFAF.md`** (uppercase). Litigation loader uses **`core_path("mfaf")`** → **`core/mfaf.md`**.
- **Impact:** On case-sensitive filesystems (e.g. Linux), `core/mfaf.md` does not exist. `_read()` returns `""`. MFAF section is omitted from the system prompt with **no error or warning** — deliberations run without Feasibility Assessment Framework content.
- **Fix applied:** In `litigation/prompts/sources.py`, load MFAF from the actual file: use key that resolves to `core/MFAF.md` (e.g. pass `"MFAF"` to a path helper that preserves case, or add explicit path for MFAF). Implemented as `core_path("MFAF")` in SOURCES.

### 2.3 Missing template: prophet-vindication.md (MEDIUM)

- **Reference:** `courtroom/COURT_PROTOCOL.md` line ~920: "Use template: `templates/prophet-vindication.md`".
- **Fact:** `templates/prophet-vindication.md` does not exist. Templates present: session-start, special-interest-hearing, contempt-hearing, module-template, project-dashboard.
- **Fix applied:** Add **`templates/prophet-vindication.md`** with minimal template content (Prophet vindication recording: state update, changelog note, optional narrative line) so the reference is valid and the court has a stub to expand.

---

## 3. Silent Errors & Error Handling

### 3.1 Intentional fallbacks (no change)

- **litigation/run.py:** `except ImportError: pass` for python-dotenv — documented; env used if available.
- **litigation/viewer.py:** `except ImportError` for markdown — falls back to `<pre>` escaped HTML; acceptable.
- **litigation/prompts/loader.py:** `_read()` returns `""` on missing file or read error — allows optional components; MFAF was the only critical component using a wrong path (fixed above).
- **litigation/providers:** ImportError/Exception in provider init re-raised or surfaced; no silent swallow.

### 3.2 Loader _read() (LOW)

- **Current:** `except Exception: pass` then return default. Any read error (permissions, encoding, etc.) is invisible.
- **Recommendation:** Optional debug logging (e.g. env `LITIGATION_DEBUG=1`) to log failed path and exception when a component is missing or unreadable. Not implemented in this audit to avoid behavioral change; documented here for future improvement.

---

## 4. Missing or Incomplete Documentation

### 4.1 Addressed in this audit

- **Portal path:** All portal references updated to `courtroom/portal/` in root README and portal README; Quick Start and tables corrected.
- **Litigation transcript viewer:** Root README already links `litigation/README.md`; litigation/README contains the viewer section. Optional: add one sentence in root README "Transcript viewer" section that litigation also provides a local viewer (`litigation/viewer.py`). Added as a brief bullet where litigation is mentioned.

### 4.2 Doc references verified (no breakage)

- Core docs: `core/procedures.md`, `core/personalities.md`, `core/mfaf.md` (doc ref; actual file MFAF.md), `core/sme-framework.md`, `core/state-schema.md`, `core/error-recovery.md`, `core/inter-agent-protocol.md` — all exist except doc convention `mfaf.md` vs file `MFAF.md` (loader fixed).
- Courtroom: RULES.md, BEST_PRACTICES.md, spectators.md, domains/README.md, domains/experts.yaml, precedents.md — exist.
- Checklists: judge-morningstar.md, courtroom-scribe.md, aegis-protocol.md — exist.
- Templates: session-start, special-interest-hearing, contempt-hearing, module-template, project-dashboard — exist; prophet-vindication added.
- Docs: ONBOARDING.md, agent-schema.md, glossary.md, RUNBOOK.md, edge-cases.md — exist.
- State: state/current.md, state/metrics.md — exist (or created on use).
- Agents: agents/morningstar.md and .cursor/agents/* — exist.

---

## 5. Improvements Executed

1. **sources.py:** MFAF source changed from `core_path("mfaf")` to `core_path("MFAF")` so `core/MFAF.md` is loaded.
2. **README.md (root):** Portal section and all portal links updated to `courtroom/portal/`; transcript viewer bullet added under litigation.
3. **courtroom/portal/README.md:** All internal references to `portal/` updated to `courtroom/portal/` where they denote repo paths; launch command set to `./courtroom/portal/launch.sh`.
4. **templates/prophet-vindication.md:** Created with minimal template (state update, changelog, narrative) per COURT_PROTOCOL.
5. **docs/LIL_JEFF_AUDIT_REPO_2026-02-17.md:** This audit document.
6. **Handoff to MORNINGSTAR:** `courtroom/transcripts/HANDOFF-2026-LIL-JEFF-AUDIT.md` (or equivalent) with short summary and pointer to this audit.

---

## 6. Recommendations for MORNINGSTAR

- **Precedents:** Consider a single "Documentation and Links" precedent: "Portal and transcript viewer live at `courtroom/portal/` and `litigation/viewer.py`; MFAF content from `core/MFAF.md`."
- **Runbook:** Add an entry: "If MFAF or other framework sections are missing from litigation prompts, check that filenames match loader paths (e.g. core/MFAF.md)."
- **Optional:** Add `LITIGATION_DEBUG=1` to log missing or unreadable framework files in the loader.

---

*Audit and fixes performed by LIL_JEFF. Advancements delivered to MORNINGSTAR via handoff document.*
