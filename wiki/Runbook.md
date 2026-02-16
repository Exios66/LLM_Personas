# Runbook — Troubleshooting

| Symptom | Action |
|---------|--------|
| Portal won't launch / "permission denied" | `chmod +x portal/launch.sh`; run from project root. |
| No transcripts found | Ensure `.md` files exist in `courtroom/transcripts/` with supported naming (`YYYY-MM-DD-topic.md` or `YYYYMMDD_HHMMSS_topic.md`). |
| Viewer doesn't list my transcript | Add filename to `KNOWN_TRANSCRIPTS` in `portal/viewer.html`, or run `./portal/launch.sh` (discovers from directory). Or run `python3 portal/generate_manifest.py` and serve over HTTP. |
| Export to HTML fails | Run manually: `python3 portal/export_transcript.py courtroom/transcripts/<file>.md -o portal/exports/<file>.html`. |
| State missing or corrupted | Restore from backup if available; otherwise follow recovery levels in [Error-Recovery](Error-Recovery). |
| Need to roll back a bad decision | Follow rollback protocol in [Error-Recovery](Error-Recovery). |
| When should I convene vs not? | Use [When-to-Convene](When-to-Convene) (Dissolution Protocol). |
| How do I summon an expert? | `/summon <domain>-expert` (Witness) or `/seat <domain>-specialist` (Judge only, F3+). See [Domains-and-Experts](Domains-and-Experts). |
| Which agent for R/Quarto? | **octavius** subagent. General code → **lil-jeff**. Decisions → **morningstar**. See [Inter-Agent-Protocol](Inter-Agent-Protocol). |
| How to cite a prior ruling? | Use Case ID: e.g. `Per 2026-INFRA-001-001` or `See Case 2026-INFRA-001-001`. See [Precedents](Precedents). |

**See also:** [Edge-Cases](Edge-Cases) · [Error-Recovery](Error-Recovery)
