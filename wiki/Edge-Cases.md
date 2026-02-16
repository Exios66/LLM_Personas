# Edge Case Registry

Known limitations and expected behavior.

## Portal & Viewer

| Scenario | Behavior / limitation | Workaround |
|----------|------------------------|------------|
| Opening `portal/viewer.html` via `file://` | Browser may block fetch of local files. List may be empty or only hardcoded. | Serve over HTTP (e.g. `python3 -m http.server 8080`) and open `http://localhost:8080/portal/viewer.html`; or use `./portal/launch.sh`. |
| Transcript filename not in supported format | Launch script may show "Unknown" date or parse title incorrectly. | Use `YYYY-MM-DD-topic.md` or `YYYYMMDD_HHMMSS_topic.md`. |
| No `.html` for a given `.md` | Launch script exports on demand via Python. | Requires Python 3. If export fails, run export command manually (see [Runbook](Runbook)). |
| `portal/launch.sh` not executable | "Permission denied." | `chmod +x portal/launch.sh` once. |

## State & Session

| Scenario | Behavior / limitation | Workaround |
|----------|------------------------|------------|
| `state/current.md` missing | Court may assume empty context. | Create from template in repo (`templates/session-start.md`, `core/state-schema.md`). |
| State invalid (missing section) | Validation may fail; recovery procedures apply. | Backup state before major sessions; see [Error-Recovery](Error-Recovery). |
| Multiple editors of state | No locking; last writer wins. | Single-operator assumption. Backup before edits. |

## Agents & Handoff

| Scenario | Behavior / limitation | Workaround |
|----------|------------------------|------------|
| Task is mixed (e.g. decide + implement in R) | Deliberation with MORNINGSTAR; then hand off R part to OCTAVIUS. | Two-step handoff. |
| LIL_JEFF given R/Quarto task | OCTAVIUS is the designated R/Quarto agent. | Prefer invoking **octavius** for R/Quarto. |

## SME

| Scenario | Behavior / limitation | Workaround |
|----------|------------------------|------------|
| SME testimony wrong or misleading | No automatic correction. | Record in `state/sme-failures.md`. |
| Domain not in registry | `/summon` or `/seat` for unknown domain has no definition. | Add domain via `courtroom/domains/experts.yaml` and process in `courtroom/domains/README.md`. |

**See:** [Runbook](Runbook) · [Error-Recovery](Error-Recovery)
