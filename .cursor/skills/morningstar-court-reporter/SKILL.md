---
name: morningstar-court-reporter
description: Integrates and updates all MORNINGSTAR courtroom documentation sources—transcripts, precedents, metrics, dashboard, manifest, state, CHANGELOG. Authenticates and renames transcripts per core/case-format.md. Verifies winddown checklist completion. Use when syncing courtroom docs, running periodic documentation integration, invoking the Court Reporter, or ensuring transcript/precedent/metric consistency.
---

# MORNINGSTAR Court Reporter

Ensures all courtroom documentation sources are properly integrated and updated. **Authenticates all transcripts** per `core/case-format.md`. **Renames non-conforming uncertified transcripts** to canonical format. **Verifies winddown checklist** (per `checklists/courtroom-scribe.md`) is complete before finishing.

**The Court Reporter MUST act upon the script output.** Producing a report without completing the integration—without updating precedents, metrics, dashboard, state, and CHANGELOG—is grounds for contempt before the Court. Complete the job. All records must be documented and authenticated.

**Canonical refs:** `checklists/courtroom-scribe.md`, `core/case-format.md`, `core/state-schema.md`, `courtroom/precedents.md`, `state/metrics.md`

---

## When to Apply

- User requests "sync courtroom documentation", "run Court Reporter", or "integrate transcripts"
- Periodic documentation maintenance (every 3 hours)
- After new transcripts are added (courtroom or litigation)
- When precedents, metrics, or dashboard may be stale

---

## Integration Workflow

Execute in order:

### 1. Transcript Audit & Authentication

- Scan `courtroom/transcripts/` and `litigation/transcripts/`
- List all `.md` files; exclude `README.md`, `HANDOFF*`, `.gitkeep`
- Identify **uncertified** transcripts (missing `> *Transcript certified by MORNINGSTAR::SCRIBE*`)
- **Authenticate filenames** per `core/case-format.md`:
  - Canonical: `YYYY-MM-DD-[matter-slug].md` (Standard) or `YYYYMMDD_HHMMSS_special_interest_[subject].md` (Special Interest)
  - Legacy `YYYYMMDD_HHMMSS_topic.md`: grandfathered for certified; suggest rename for uncertified
- **Authenticate headers**: Case No. `YYYY-CATC-NNN-DDD`, Date `YYYY-MM-DD`, certification marker
- For non-conforming **uncertified** transcripts: run `python courtroom/reporter.py --rename` to rename to canonical format (or perform rename manually)
- **Never rename certified legacy transcripts** (grandfather rule)

### 2. Regenerate Manifest

```bash
python courtroom/portal/generate_manifest.py
```

Ensures `courtroom/portal/transcripts_manifest.json` reflects `courtroom/transcripts/`. If litigation transcripts should be in portal, extend manifest or document limitation.

### 3. Precedents Sync

- Read `courtroom/precedents.md` Master Index
- For each certified transcript not in index: extract Case No. (`YYYY-CATC-NNN-DDD` per `core/case-format.md`), Date, Matter, Ruling, Vote
- Add new entries to Master Index and category tables
- Follow precedent entry schema in `courtroom/precedents.md`

### 4. Metrics Sync

- Update `state/metrics.md` from transcript data:
  - Total deliberations, decisions, vote distribution
  - Prophet proposals, vindications
  - SME activity if documented
- Recalculate percentages, trends, health indicators

### 5. Dashboard Sync

- Update `templates/project-dashboard.md`:
  - Transcript counts (courtroom + litigation)
  - Deliberation metrics from `state/metrics.md`
  - Agent/skill counts from `docs/agent-skills.md` if changed
  - Last Updated date

### 6. State Validation

- Validate `state/current.md` per `core/state-schema.md`
- If invalid or stale: reconstruct from CHANGELOG, transcripts; or flag for user

### 7. CHANGELOG Check

- Ensure recent decisions (from transcripts) appear in `CHANGELOG.md`
- Format: `[YYYY-MM-DD] [Summary]. Vote: X-Y-Z. Risk: [risk]. Dissent: [if any].`

### 8. Agent Skills Index (Optional)

- If skills were added/changed: update `docs/agent-skills.md` version and entries

### 9. Authenticate & Rename Transcripts

- Run `python courtroom/reporter.py` — review output for `[CHECK FORMAT]`, `[HEADER INCOMPLETE]`, `→ rename to:`
- For **uncertified** transcripts with non-canonical names: run `python courtroom/reporter.py --rename` (or `--rename --yes` for non-interactive)
- For transcripts using `Matter ID`: add addendum recommending `Case No.:` for future; legacy certified need not be modified

### 10. Winddown Checklist Verification (Mandatory)

Before finishing, verify **all** Session Closure items from `checklists/courtroom-scribe.md` are complete:

| Item | Verification |
|------|--------------|
| CHANGELOG updated | Every F3+ decision from recent sessions appears in `CHANGELOG.md` |
| Transcripts archived | All certified transcripts in `courtroom/transcripts/` or `litigation/transcripts/` |
| State checkpointed | `state/current.md` reflects session outcomes; valid per `core/state-schema.md` |
| Precedent entry | Every certified transcript has an entry in `courtroom/precedents.md` Master Index |
| Project dashboard | `templates/project-dashboard.md` refreshed from metrics and transcript counts |
| Transcript directory hygiene | Filenames follow `core/case-format.md`; no uncertified drafts in wrong folders; manifest current |

**Do not finish until every item is verified complete.** Incomplete winddown = contempt.

---

## Script Integration

Run the script first:

```bash
python courtroom/reporter.py
```

If non-canonical uncertified transcripts exist:

```bash
python courtroom/reporter.py --rename
```

**You MUST act on the output.** Do not merely read it. The script reports transcript counts, uncertified list, auth status, rename suggestions, manifest status. You must then:

1. **Authenticate/rename** non-conforming uncertified transcripts
2. **Add** any certified transcripts not in precedents to `courtroom/precedents.md`
3. **Sync** `state/metrics.md` from transcript data
4. **Update** `templates/project-dashboard.md` with current counts
5. **Validate** `state/current.md`; fix or flag
6. **Verify** `CHANGELOG.md` has recent decisions
7. **Verify winddown checklist** — all Session Closure items complete

Incomplete integration = contempt. Complete the workflow. All records must be documented and authenticated.

---

## Verification Checklist (All Required)

- [ ] Transcripts audited; filenames authenticated per `core/case-format.md`
- [ ] Non-conforming uncertified transcripts renamed (or flagged for user)
- [ ] Uncertified transcripts identified; no drafts left in wrong folders
- [ ] Portal manifest regenerated and current
- [ ] Precedents index includes **all** certified transcripts
- [ ] Metrics reflect transcript data
- [ ] Dashboard synced from metrics
- [ ] State valid per schema
- [ ] CHANGELOG has recent entries
- [ ] **Winddown checklist** — all Session Closure items verified complete

---

## Scheduling (Every 3 Hours)

**Crontab:**
```bash
0 */3 * * * cd /path/to/LLM_Personas && python courtroom/reporter.py
```

**Manual full integration:** Invoke Court Reporter subagent for AI-required updates (precedent entries, metrics interpretation).

---

## Quick Reference

| Source | Path |
|--------|------|
| Courtroom transcripts | `courtroom/transcripts/` |
| Litigation transcripts | `litigation/transcripts/` |
| Manifest | `courtroom/portal/transcripts_manifest.json` |
| Precedents | `courtroom/precedents.md` |
| Metrics | `state/metrics.md` |
| Dashboard | `templates/project-dashboard.md` |
| State | `state/current.md` |
| Reporter script | `courtroom/reporter.py` |
| Manifest generator | `courtroom/portal/generate_manifest.py` |

---

> *"The record persists. The court endures. The documentation stays current."* — MORNINGSTAR::COURT_REPORTER
