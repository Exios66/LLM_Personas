# MORNINGSTAR Court Reporter

Ensures all courtroom documentation sources are properly integrated and updated. **Authenticates transcripts** per [core/case-format.md](../core/case-format.md). **Renames non-conforming uncertified transcripts** to canonical format. **Verifies winddown checklist** completion. Designed to run **every 3 hours** (or on demand).

---

## Components

| Component | Path | Purpose |
|-----------|------|---------|
| **Subagent** | `.cursor/agents/court-reporter.md` | AI role; performs full integration when invoked |
| **Skill** | `.cursor/skills/morningstar-court-reporter/SKILL.md` | Integration workflow and checklist |
| **Script** | `courtroom/reporter.py` | Audit, authenticate, manifest, report; optional `--rename` |
| **Cron launcher** | `scripts/run-court-reporter.sh` | Shell wrapper for crontab |

---

## Script Usage

```bash
python courtroom/reporter.py              # Audit; output ACTION REQUIRED
python courtroom/reporter.py --rename     # Also rename non-conforming uncertified transcripts (interactive)
python courtroom/reporter.py --rename -y  # Non-interactive rename
```

The script authenticates filenames per `core/case-format.md`, validates headers (Case No., Date), and flags `[CHECK FORMAT]`, `[HEADER INCOMPLETE]`, `[Matter ID—prefer Case No.]`, or `→ rename to:` for non-conforming files. **Certified legacy transcripts are never renamed** (grandfather rule).

---

## Winddown Checklist Verification

Before finishing, the Court Reporter **must verify** all Session Closure items from [checklists/courtroom-scribe.md](../checklists/courtroom-scribe.md):

- CHANGELOG updated with decisions
- All transcripts archived in correct location
- State checkpointed
- Precedents index complete (every certified transcript)
- Project dashboard refreshed
- Transcript directory hygiene (correct filenames, no uncertified drafts misplaced)

---

## Scheduling (Every 3 Hours)

### Crontab

```bash
crontab -e
# Add (adjust path):
0 */3 * * * cd /path/to/LLM_Personas && python3 courtroom/reporter.py

# With logging:
0 */3 * * * /path/to/LLM_Personas/scripts/run-court-reporter.sh >> /tmp/court-reporter.log 2>&1
```

### launchd (macOS)

Create `~/Library/LaunchAgents/com.morningstar.court-reporter.plist` with `StartInterval` 10800 (3 hours). See `scripts/run-court-reporter.sh` for pattern.

### Manual

- **Script:** `python courtroom/reporter.py`
- **Full integration:** Invoke Court Reporter subagent: "Run the Court Reporter"

---

## Transcript & Case Format

Transcript filenames and Case No. format are defined in [core/case-format.md](../core/case-format.md): Standard `YYYY-MM-DD-[matter-slug].md`; Special Interest `YYYYMMDD_HHMMSS_special_interest_[subject].md`; Case No. `YYYY-CATC-NNN-DDD` in header. The reporter checks filename format (Standard, Special Interest); Case No. is extracted by `generate_manifest.py` for display.

---

## Integration Sources

| Source | Script | Subagent |
|--------|--------|----------|
| courtroom/transcripts/ | Audit | — |
| litigation/transcripts/ | Audit | — |
| portal manifest | Regenerate | — |
| precedents.md | — | Add entries |
| state/metrics.md | — | Sync |
| project-dashboard.md | — | Refresh |
| state/current.md | — | Validate |
| CHANGELOG.md | — | Verify |

---

> *"The record persists. The court endures. The documentation stays current."* — MORNINGSTAR::COURT_REPORTER
