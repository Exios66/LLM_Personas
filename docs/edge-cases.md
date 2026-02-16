# Edge Case Registry

> *Known limitations and expected behavior. By design or workaround.*

This document records edge cases and limitations so operators and implementers know what to expect. Add entries when new cases are discovered.

---

## Format

Each entry:

- **Scenario** — What situation or configuration.
- **Behavior / limitation** — What happens or what is not supported.
- **Workaround / note** — How to avoid or live with it; or "By design."

---

## Portal & Viewer

| Scenario | Behavior / limitation | Workaround / note |
|----------|------------------------|--------------------|
| Opening `portal/viewer.html` via `file://` | Browser may block `fetch()` of local transcript files (CORS). List may be empty or only show hardcoded `KNOWN_TRANSCRIPTS`. | Serve the project over HTTP (e.g. `python3 -m http.server 8080`) and open `http://localhost:8080/portal/viewer.html`; or use `./portal/launch.sh` to open exported HTML. |
| Transcript filename not `YYYY-MM-DD-*` or `YYYYMMDD_HHMMSS_*` | Launch script and generate.py may show "Unknown" date or parse title incorrectly. | Prefer the two supported naming conventions. See [portal/README.md](../portal/README.md). |
| No `.html` in `courtroom/transcripts/` for a given `.md` | Launch script will call `portal/export_transcript.py` to generate HTML on demand. | Requires Python 3. If export fails, run the export command manually (see RUNBOOK). |
| `portal/launch.sh` not executable | Shell reports "permission denied." | Run `chmod +x portal/launch.sh` once. |

---

## State & Session

| Scenario | Behavior / limitation | Workaround / note |
|----------|------------------------|--------------------|
| `state/current.md` missing | MORNINGSTAR may open with "no state" or assume empty context. | Create from template in [templates/session-start.md](../templates/session-start.md) or [core/state-schema.md](../core/state-schema.md). |
| State file invalid (e.g. missing required section) | Validation per state-schema may fail; recovery procedures apply. | Run validation checklist before major sessions; backup state (see procedures). |
| Multiple sessions / users editing state | No locking. Last writer wins; risk of overwrite. | By design: single-operator assumption. Backup before major edits. |

---

## Agents & Handoff

| Scenario | Behavior / limitation | Workaround / note |
|----------|------------------------|--------------------|
| Task is mixed (e.g. decide API shape + implement in R) | Deliberation stays with MORNINGSTAR; R implementation goes to OCTAVIUS. Hand off in two steps. | Specify in handoff: "Implement the agreed design in R per OCTAVIUS." |
| LIL_JEFF given R/Quarto task | LIL_JEFF may implement in R but OCTAVIUS is the designated R/Quarto agent with THE_RULES and summaries. | Prefer invoking octavius for R/Quarto work. See [core/inter-agent-protocol.md](../core/inter-agent-protocol.md). |

---

## SME & Domains

| Scenario | Behavior / limitation | Workaround / note |
|----------|------------------------|--------------------|
| SME testimony wrong or misleading | No automatic correction. Court may rely on bad input. | Record in [state/sme-failures.md](../state/sme-failures.md) for institutional learning. |
| Domain not in registry | `/summon` or `/seat` for unknown domain has no definition. | Add domain via [courtroom/domains/experts.yaml](../courtroom/domains/experts.yaml) and process in [courtroom/domains/README.md](../courtroom/domains/README.md). |

---

*Update this registry when new edge cases are discovered. See [courtroom/transcripts/HANDOFF-2026-INFRA-002.md](../courtroom/transcripts/HANDOFF-2026-INFRA-002.md) for enhancement context.*
