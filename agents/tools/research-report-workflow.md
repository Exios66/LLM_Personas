# Tool: Research Report Workflow

**Implementation:** `agents/workflows/research_report.py`  
**Purpose:** Multi-agent pipeline that researches a topic, fact-checks findings, writes a report under 1,000 words, formats it as HTML, and optionally sends via Gmail. Reports are saved with an alphanumeric ID and short-form timestamp.

## Invocation

From project root:

```bash
python agents/workflows/research_report.py "Topic to research"
```

With email delivery:

```bash
python agents/workflows/research_report.py "Quantum computing 2025" --to recipient@example.com
```

Without saving to file:

```bash
python agents/workflows/research_report.py "Topic" --no-save
```

## Inputs

| Input | Description |
|-------|-------------|
| **topic** | Free-text topic to research. |
| **--to** | Optional: email recipient (sends via Gmail SMTP). |
| **--no-save** | Skip saving the report file. |

## Outputs

- **File:** `agents/reports/{report_id}_{timestamp}.html`  
  Example: `RPT_A1B2C3D4_20250219_143022.html`
- **Console:** Report ID, timestamp, and HTML preview.
- **Email:** If `--to` and Gmail credentials are set, HTML report sent as email body.

## Agents (Sequential Pipeline)

1. **Researcher** — Web search (Tavily or DuckDuckGo); extracts facts with source URLs.
2. **Fact-Checker** — Keeps only facts appearing in ≥2 independent sources.
3. **Report Writer** — Coherent report under 1,000 words.
4. **Formatter** — Clean HTML for email body.

## Config & Env

- `agents/workflows/config.yaml` — provider, model (gpt-4.1-mini), temperature.
- `agents/workflows/.env` — `OPENROUTER_API_KEY`, `TAVILY_API_KEY`, `GMAIL_USER`, `GMAIL_APP_PASSWORD`.

See `agents/workflows/README.md` for full setup.

## When to Use

Invoke when a researched, fact-checked report is needed on a topic and delivery as HTML (file or email) is required. Use litigation runner for formal courtroom deliberation instead.
