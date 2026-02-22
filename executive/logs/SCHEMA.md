# Judicial Decisions Log Schema

**File:** `judicial_decisions.log`  
**Format:** NDJSON (one JSON object per line)

## Entry Schema

| Field       | Type   | Required | Description                                      |
|-------------|--------|----------|--------------------------------------------------|
| timestamp   | string | yes      | ISO 8601 UTC                                     |
| matter      | string | yes      | Short description of the matter                  |
| ruling_hash | string | yes      | Content hash of ruling (e.g. `sha256:abc123...`) |
| source      | string | yes      | Transcript path or ruling ID                     |
| entry_hash  | string | yes      | SHA-256 of canonical entry (content-addressing)  |
| prev_hash   | string | yes      | entry_hash of previous entry (chain integrity)  |

## Example

```json
{"timestamp": "2026-02-19T12:00:00.000000+00:00", "matter": "2026-DEL-001: Executive branch addition", "ruling_hash": "sha256:b85887fe...", "source": "litigation/transcripts/2026-02-19-the-addition-of-an-executive-branch-into-the-larger-architec.md", "entry_hash": "a1b2c3...", "prev_hash": ""}
```

First entry has `prev_hash: ""`. Subsequent entries chain via `prev_hash` = previous `entry_hash`.
