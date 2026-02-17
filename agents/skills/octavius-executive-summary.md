# Skill: Executive summary

**Agent:** octavius  
**Index:** `docs/agent-skills.md` § octavius

## Source

`octavius_summaries/`, standard format in agent body (Octavius Executive Summary block).

## When to use

End of session; Phase 5. Always produce an Executive Summary and save to `octavius_summaries/` with timestamped filename (e.g. `YYYY-MM-DD_HHMMSS_summary.md`).

## Fallback

If `octavius_summaries/` is missing: create the directory or report to user that the summary could not be archived.

## Procedure

1. At session end, compile: task overview, Apollo contributions, Kronos report, Morningstar authentication (spec compliance, scientific accuracy, reproducibility), deliverables, notes.
2. Use the standard block format from the Octavius agent body (session concluded block).
3. Write to `octavius_summaries/YYYY-MM-DD_HHMMSS_summary.md`.
