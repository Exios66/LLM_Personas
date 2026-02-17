# Skill: State read/write

**Agent:** morningstar  
**Index:** `docs/agent-skills.md` § morningstar

## Source

`state/current.md`

## When to use

- **Session init (read):** On `/morningstar` or session start, read `state/current.md` to load active context, recent decisions, pending matters.
- **Session end (update):** Before closing, update `state/current.md` with session outcomes, new decisions, and working files.

## Fallback

If `state/current.md` is missing: proceed with empty context. Optionally create the file from `templates/session-start.md` or report to user.

## Procedure

1. Read `state/current.md` at session init.
2. Summarize state in opening (e.g. "Well then. Let's see what survived yesterday.").
3. At session end or after material decisions, update state per `core/state-schema.md`.
4. Preserve existing sections; append or update only changed parts.
