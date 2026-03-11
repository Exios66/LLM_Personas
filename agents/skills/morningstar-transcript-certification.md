# Skill: Transcript certification

**Agent:** morningstar  
**Index:** `docs/agent-skills.md` § morningstar

## Source

`courtroom/transcripts/`, `checklists/courtroom-scribe.md`

## When to use

- After F3+ deliberations: save transcript to `courtroom/transcripts/` or `litigation/transcripts/`.
- At end of transcript: apply Scribe certification.

## Fallback

Apply Scribe checklist to the extent possible; certify with the standard line even if checklist is missing.

## Procedure

1. Save transcript per [core/case-format.md](../core/case-format.md): Standard `YYYY-MM-DD-[matter-slug].md`; Special Interest `YYYYMMDD_HHMMSS_special_interest_[subject].md`. Header MUST include `Case No.: YYYY-CATC-NNN-DDD`.
2. Apply `checklists/courtroom-scribe.md` (transcript verification, certification).
3. End transcript with: `> *Transcript certified by MORNINGSTAR::SCRIBE*`
