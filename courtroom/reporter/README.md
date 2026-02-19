# MORNINGSTAR Court Reporter

Ensures all courtroom documentation sources are properly integrated and updated. Designed to run **every 3 hours** (or on demand).

---

## Components

| Component | Path | Purpose |
|-----------|------|---------|
| **Subagent** | `.cursor/agents/court-reporter.md` | AI role; performs full integration when invoked |
| **Skill** | `.cursor/skills/morningstar-court-reporter/SKILL.md` | Integration workflow and checklist |
| **Script** | `courtroom/reporter.py` | Mechanical sync: audit, manifest, report |

---

## Scheduling (Every 3 Hours)

### Option 1: Crontab

```bash
# Edit crontab
crontab -e

# Add line (adjust path to your repo):
0 */3 * * * cd /path/to/LLM_Personas && python3 courtroom/reporter.py

# With logging:
0 */3 * * * /path/to/LLM_Personas/scripts/run-court-reporter.sh >> /tmp/court-reporter.log 2>&1
```

### Option 2: launchd (macOS)

Create `~/Library/LaunchAgents/com.morningstar.court-reporter.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.morningstar.court-reporter</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/python3</string>
    <string>/path/to/LLM_Personas/courtroom/reporter.py</string>
  </array>
  <key>WorkingDirectory</key>
  <string>/path/to/LLM_Personas</string>
  <key>StartInterval</key>
  <integer>10800</integer>
  <key>StandardOutPath</key>
  <string>/tmp/court-reporter.log</string>
  <key>StandardErrorPath</key>
  <string>/tmp/court-reporter.err</string>
</dict>
</plist>
```

Load: `launchctl load ~/Library/LaunchAgents/com.morningstar.court-reporter.plist`

### Option 3: Manual Invocation

- **Script only:** `python courtroom/reporter.py` — mechanical sync
- **Full integration:** Invoke Court Reporter subagent: "Run the Court Reporter" or "Sync courtroom documentation"

---

## Integration Sources

| Source | Action |
|--------|--------|
| `courtroom/transcripts/` | Audit; list uncertified |
| `litigation/transcripts/` | Audit; list uncertified |
| `courtroom/portal/transcripts_manifest.json` | Regenerate |
| `courtroom/precedents.md` | Add new entries (subagent) |
| `state/metrics.md` | Sync from transcripts (subagent) |
| `templates/project-dashboard.md` | Refresh (subagent) |
| `state/current.md` | Validate (subagent) |
| `CHANGELOG.md` | Verify (subagent) |

---

## Quick Reference

```bash
# Run script
python courtroom/reporter.py

# Via launcher
./scripts/run-court-reporter.sh
```

---

> *"The record persists. The court endures. The documentation stays current."* — MORNINGSTAR::COURT_REPORTER
