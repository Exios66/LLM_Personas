# MORNINGSTAR Court Reporter

Ensures all courtroom documentation sources are properly integrated and updated. Designed to run **every 3 hours** (or on demand).

---

## Components

| Component | Path | Purpose |
|-----------|------|---------|
| **Subagent** | `.cursor/agents/court-reporter.md` | AI role; performs full integration when invoked |
| **Skill** | `.cursor/skills/morningstar-court-reporter/SKILL.md` | Integration workflow and checklist |
| **Script** | `courtroom/reporter.py` | Mechanical sync: audit, manifest, report |
| **Cron launcher** | `scripts/run-court-reporter.sh` | Shell wrapper for crontab |

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
