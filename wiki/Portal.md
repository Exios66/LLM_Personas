# Portal (Transcript Viewer)

View and export deliberation transcripts.

## Primary: Launch Script

From the project root:

```bash
./portal/launch.sh
```

- Lists all `.md` transcripts in `courtroom/transcripts/`
- You pick one by number
- Opens in browser (uses existing `.html` if present, otherwise exports via `portal/export_transcript.py`)

If you get "permission denied," run `chmod +x portal/launch.sh` once. Python 3 is used for on-demand export.

## Transcript Discovery

- Run `python3 portal/generate_manifest.py` to generate `portal/transcripts_manifest.json`.
- When the viewer is served over HTTP, it loads this manifest and lists transcripts automatically.
- Otherwise the viewer falls back to a hardcoded list in `portal/viewer.html`.

## Standalone Viewer

- **`portal/viewer.html`** — Browse transcripts (best when served over HTTP, e.g. `python3 -m http.server 8080` then open `http://localhost:8080/portal/viewer.html`).
- **`portal/export_transcript.py`** — Export a single `.md` transcript to styled HTML (no external deps). Used by the launch script when no pre-built HTML exists.

## Transcript Naming

Supported formats: `YYYY-MM-DD-topic.md` or `YYYYMMDD_HHMMSS_topic.md`.

Full details: `portal/README.md` in the repo.

**See:** [Runbook](Runbook) (troubleshooting) · [Edge-Cases](Edge-Cases)
