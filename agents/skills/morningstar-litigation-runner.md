# Skill: Litigation runner

**Agent:** morningstar  
**Index:** `docs/agent-skills.md` § morningstar

## Source

`litigation/run.py`, `agents/tools/litigation-runner.md`

## When to use

When the user requests a **formal bench trial** or **formal transcript** from the litigation runner (full framework, LLM-backed deliberation).

## Fallback

If the runner cannot be executed by the agent: instruct the user to run from project root:  
`python litigation/run.py "Matter text"` (and optional flags: `--save-to courtroom`, `--hearing-type standard`, etc.). See `agents/tools/litigation-runner.md` for full options.

## Procedure

1. If user wants a formal transcript: determine matter text and feasibility.
2. If environment permits running commands: run `python litigation/run.py "matter"` with appropriate args.
3. Otherwise: provide the exact command and flags for the user to run.
4. Transcript will be written to `litigation/transcripts/` or `courtroom/transcripts/` per config.
