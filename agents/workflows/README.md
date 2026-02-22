# Research Report Workflow

Production-ready multi-agent pipeline that researches a topic, fact-checks findings, writes a report, formats it as HTML, and optionally sends it via Gmail.

## Overview

| Agent | Role | Input | Output |
|-------|-----|------|--------|
| **Researcher** | Gathers recent, credible info via web search | Topic | Structured findings (fact + sources) |
| **Fact-Checker** | Verifies facts | Findings | Only facts in ≥2 independent sources |
| **Report Writer** | Composes report | Verified facts | Report < 1,000 words |
| **Formatter** | Produces HTML | Report text | Clean HTML for email body |

**Model:** `gpt-4.1-mini` (OpenRouter)

**Output:** `agents/reports/{report_id}_{timestamp}.html`  
Example: `RPT_A1B2C3D4_20250219_143022.html`

---

## Quick Start

```bash
# From repo root
cd /path/to/LLM_Personas
python agents/workflows/research_report.py "Climate policy updates 2025"

# With email delivery
python agents/workflows/research_report.py "Quantum computing advances" --to recipient@example.com
```

---

## Required Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENROUTER_API_KEY` | **Yes** | OpenRouter API key for LLM calls |
| `TAVILY_API_KEY` | No | Web search (primary). Fallback: DuckDuckGo (no key) |
| `GMAIL_USER` | For `--to` | Gmail address |
| `GMAIL_APP_PASSWORD` | For `--to` | [App Password](https://support.google.com/accounts/answer/185833), not regular password |

**Setup:**

1. Copy `agents/workflows/.env.example` → `agents/workflows/.env`
2. Fill in `OPENROUTER_API_KEY` (get key at [openrouter.ai](https://openrouter.ai))
3. Optional: `TAVILY_API_KEY` from [app.tavily.com](https://app.tavily.com) (1,000 free credits/mo)
4. Optional: `GMAIL_USER` and `GMAIL_APP_PASSWORD` for `--to`

---

## CLI Options

```
usage: research_report.py [-h] [--to RECIPIENT] [--no-save] topic

positional arguments:
  topic         Topic to research

optional arguments:
  --to RECIPIENT   Email recipient (sends via Gmail)
  --no-save        Do not save report file
```

---

## Workflow Steps

1. **Researcher**  
   Uses Tavily (or DuckDuckGo fallback) to search for recent, authoritative content. Outputs facts with source URLs.

2. **Fact-Checker**  
   Marks a fact **verified** only if it appears in at least two independent sources. Rejects single-source claims.

3. **Report Writer**  
   Combines verified facts into a coherent report under 1,000 words. Cites sources inline.

4. **Formatter**  
   Converts the report to clean HTML suitable for email body (semantic tags, inline styles).

5. **Save**  
   Writes to `agents/reports/{report_id}_{timestamp}.html` with report metadata in a comment.

6. **Send** (optional)  
   If `--to` is given and Gmail credentials are set, sends the HTML report as the email body.

---

## File Layout

```
agents/
├── workflows/
│   ├── research_report.py   # Main script
│   ├── search.py            # Tavily + DuckDuckGo search
│   ├── email_sender.py      # Gmail SMTP
│   ├── config.yaml          # Optional overrides
│   ├── .env.example         # Env template
│   └── README.md            # This file
└── reports/                 # Output directory
    └── RPT_XXXX_YYYYMMDD_HHMMSS.html
```

---

## Fallback Behavior

| Service | Primary | Fallback |
|---------|---------|----------|
| LLM | OpenRouter + gpt-4.1-mini | (required; no fallback) |
| Web search | Tavily | DuckDuckGo (no API key) |
| Email | Gmail SMTP | Skip if `--to` not used or credentials missing |

If `TAVILY_API_KEY` is not set, the Researcher uses DuckDuckGo. Results may be less curated but the workflow still runs.
