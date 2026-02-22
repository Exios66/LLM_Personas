---
name: morningstar-court-reporter
description: Integrates and updates all MORNINGSTAR courtroom documentation sources—transcripts, precedents, metrics, dashboard, manifest, state, CHANGELOG. Use when syncing courtroom docs, running periodic documentation integration, invoking the Court Reporter, or ensuring transcript/precedent/metric consistency.
---

# MORNINGSTAR Court Reporter

Ensures all courtroom documentation sources are properly integrated and updated. Run periodically (every 3 hours recommended) or when invoked.

**The Court Reporter MUST act upon the script output.** Producing a report without completing the integration—without updating precedents, metrics, dashboard, state, and CHANGELOG—is grounds for contempt before the Court. Complete the job.

**Canonical refs:** `checklists/courtroom-scribe.md`, `core/state-schema.md`, `courtroom/precedents.md`, `state/metrics.md`

---

## When to Apply

- User requests "sync courtroom documentation", "run Court Reporter", or "integrate transcripts"
- Periodic documentation maintenance (every 3 hours)
- After new transcripts are added (courtroom or litigation)
- When precedents, metrics, or dashboard may be stale

---

## Integration Workflow

Execute in order:

### 1. Transcript Audit

- Scan `courtroom/transcripts/` and `litigation/transcripts/`
- List all `.md` files; exclude `README.md`, `HANDOFF*`, `.gitkeep`
- Identify **uncertified** transcripts (missing `> *Transcript certified by MORNINGSTAR::SCRIBE*`)
- Verify filenames: `YYYY-MM-DD-[slug].md` or `YYYYMMDD_HHMMSS_special_interest_[subject].md`
- Report: total count, uncertified count, any mis-filed files

### 2. Regenerate Manifest

```bash
python courtroom/portal/generate_manifest.py
```

Ensures `courtroom/portal/transcripts_manifest.json` reflects `courtroom/transcripts/`. If litigation transcripts should be in portal, extend manifest or document limitation.

### 3. Precedents Sync

- Read `courtroom/precedents.md` Master Index
- For each certified transcript not in index: extract Case No., Date, Matter, Ruling, Vote
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

---

## Script Integration

Run the script first:

```bash
python courtroom/reporter.py
```

**You MUST act on the output.** Do not merely read it. The script reports transcript counts, uncertified list, manifest status. You must then:

1. **Add** any certified transcripts not in precedents to `courtroom/precedents.md`
2. **Sync** `state/metrics.md` from transcript data
3. **Update** `templates/project-dashboard.md` with current counts
4. **Validate** `state/current.md`; fix or flag
5. **Verify** `CHANGELOG.md` has recent decisions

Incomplete integration = contempt. Complete the workflow.

---

## Verification Checklist

- [ ] Transcripts audited; uncertified identified
- [ ] Manifest regenerated
- [ ] Precedents index current
- [ ] Metrics reflect transcript data
- [ ] Dashboard synced
- [ ] State valid
- [ ] CHANGELOG current

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
