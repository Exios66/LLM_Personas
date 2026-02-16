# State and Metrics

## State

- **`state/current.md`** — Active session state. Read at session start; updated at checkpoint and session end. Contains: active task, working files, recent decisions, pending matters, Prophet tracker, SME activity, session metrics.
- **Schema:** Validation rules and required sections are in `core/state-schema.md` in the repo.
- **Backup:** Before major sessions, copy `state/current.md` to `state/backups/YYYY-MM-DD-current.md`. See [Error-Recovery](Error-Recovery) and [Procedures](Procedures).

## Metrics

- **`state/metrics.md`** — Cumulative statistics: deliberations, vote patterns, Prophet vindications, SME activity, trends. Used for tracking and retrospectives.

## SME Failures

- **`state/sme-failures.md`** — Log when SME (Witness or Specialist) input led to poor outcomes. Template and schema in repo.

**See:** [Error-Recovery](Error-Recovery) · [Procedures](Procedures)
