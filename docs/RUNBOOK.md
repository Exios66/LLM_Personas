# Runbook — Troubleshooting Index

> *If X, then Y. Quick links to the right doc.*

---

## Portal & Transcripts

| Symptom | Action | Doc |
|---------|--------|-----|
| Portal won’t launch or "permission denied" | `chmod +x portal/launch.sh`; run from project root | [portal/README.md](../portal/README.md) |
| No transcripts found | Ensure `.md` files exist in `courtroom/transcripts/`; naming: `YYYY-MM-DD-topic.md` or `YYYYMMDD_HHMMSS_topic.md` | [portal/README.md](../portal/README.md) |
| Viewer doesn’t list my transcript | Add the filename to `KNOWN_TRANSCRIPTS` in `portal/viewer.html`, or use `./portal/launch.sh` (discovers from directory) | [portal/README.md](../portal/README.md) |
| Export to HTML fails | Run manually: `python3 portal/export_transcript.py courtroom/transcripts/<file>.md -o portal/exports/<file>.html` | [portal/README.md](../portal/README.md) |

---

## State & Session

| Symptom | Action | Doc |
|---------|--------|-----|
| State file missing or corrupted | Restore from backup if you have one; otherwise follow recovery levels 1–4 | [core/error-recovery.md](../core/error-recovery.md) |
| Need to roll back a bad decision | Follow rollback protocol: document, revert state, update changelog | [core/error-recovery.md](../core/error-recovery.md) |
| Not sure if state is valid | Check against required sections and fields | [core/state-schema.md](../core/state-schema.md) |
| Want to checkpoint before a big session | Copy `state/current.md` to e.g. `state/backups/YYYY-MM-DD-current.md` | [core/procedures.md](../core/procedures.md) (State backup) |

---

## Court & SME

| Symptom | Action | Doc |
|---------|--------|-----|
| When should I convene vs not? | Use Dissolution Protocol: F0, pure implementation, already decided → don’t convene | [core/procedures.md](../core/procedures.md#when-not-to-convene-dissolution-protocol) |
| How do I summon an expert? | `/summon <domain>-expert` (Witness) or `/seat <domain>-specialist` (Judge only, F3+) | [courtroom/domains/README.md](../courtroom/domains/README.md), [core/sme-framework.md](../core/sme-framework.md) |
| Which agent for R/Quarto? | Use **octavius** subagent. For general code, use **lil-jeff**. For decisions, use **morningstar**. | [core/inter-agent-protocol.md](../core/inter-agent-protocol.md) |
| How to cite a prior ruling? | Use Case ID, e.g. `Per 2026-INFRA-001-001` or `See Case 2026-INFRA-001-001` | [courtroom/precedents.md](../courtroom/precedents.md#citation-format) |

---

## Definitions & Navigation

| Need | Doc |
|------|-----|
| Glossary (F0–F5, SME, Witness, etc.) | [docs/glossary.md](glossary.md) |
| Full file/dir map | [README — Repository Map](../README.md#repository-map-complete) |
| How to use this repo (daily) | [README — How to Use This Repository](../README.md#how-to-use-this-repository) |
| Known edge cases and limitations | [docs/edge-cases.md](edge-cases.md) |

---

*When in doubt, start at [README.md](../README.md) and the [Navigation Index](../README.md#navigation-index).*
