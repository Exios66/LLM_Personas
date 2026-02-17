# Courtroom Litigation Runner

Run the MORNINGSTAR courtroom litigation protocol using local or free-tier LLMs. Supports **Ollama**, **LM Studio** (or LLM Studio), and **OpenRouter** (free models).

---

## Overview

This directory orchestrates the deliberation flow defined in `core/procedures.md` and agent documentation. It:

1. Loads session state from `state/current.md`
2. Presents a matter for deliberation
3. Invokes the court personalities (Judge, Architect, Engineer, Debugger, Prophet, Counsel) via LLM calls
4. Records arguments, vote, and ruling
5. Saves transcripts to `courtroom/transcripts/` and updates state

---

## Supported Providers

| Provider | Type | Cost | Setup |
|----------|------|------|-------|
| **Ollama** | Local | Free | Install Ollama, pull a model |
| **LM Studio** | Local | Free | Install LM Studio, load model, start server |
| **OpenRouter** | API | Free tier available | API key, use free models |

### Ollama

- **URL:** `http://localhost:11434`
- **Models:** `llama3.2`, `mistral`, `qwen2`, etc.
- **Setup:** [ollama.com](https://ollama.com) → install → `ollama pull llama3.2`

### LM Studio / LLM Studio

- **URL:** `http://localhost:1234` (OpenAI-compatible API)
- **Models:** Any model you load in LM Studio
- **Setup:** [lmstudio.ai](https://lmstudio.ai) → download → load model → Start Server (Developer tab)

### OpenRouter

- **URL:** `https://openrouter.ai/api/v1`
- **Models:** Filter for "free" at [openrouter.ai/models](https://openrouter.ai/models?q=free) (e.g. `meta-llama/llama-3.2-3b-instruct:free`, `google/gemma-2-9b-it:free`)
- **Setup:** Create API key at [openrouter.ai/keys](https://openrouter.ai/keys) → set `OPENROUTER_API_KEY`

---

## Quick Start

### 1. Install Dependencies

```bash
cd /path/to/LLM_Personas
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r litigation/requirements.txt
```

### 2. Configure Provider

Copy the example config and edit:

```bash
cp litigation/config.example.yaml litigation/config.yaml
```

Edit `litigation/config.yaml`:

```yaml
provider: ollama   # ollama | lm_studio | openrouter
model: llama3.2    # model name for your provider
```

For OpenRouter, set your API key:

```bash
export OPENROUTER_API_KEY=sk-or-v1-...
```

### 3. Run a Deliberation

From project root:

```bash
python litigation/run.py "Should we adopt a new naming convention for API endpoints?"
```

Or use the launch script:

```bash
./litigation/launch.sh "Should we adopt a new naming convention for API endpoints?"
```

Interactive mode (enter matter when prompted):

```bash
python litigation/run.py
```

---

## Configuration Reference

| Key | Description | Example |
|-----|--------------|---------|
| `provider` | `ollama`, `lm_studio`, or `openrouter` | `ollama` |
| `model` | Model identifier for the provider | `llama3.2` |
| `ollama.base_url` | Ollama API URL | `http://localhost:11434` |
| `lm_studio.base_url` | LM Studio OpenAI-compat URL | `http://localhost:1234/v1` |
| `openrouter.base_url` | OpenRouter API URL | `https://openrouter.ai/api/v1` |
| `max_tokens` | Max tokens per response | `2048` |
| `temperature` | Sampling temperature (0–1) | `0.7` |

---

## Environment Variables

| Variable | Provider | Purpose |
|----------|----------|---------|
| `OPENROUTER_API_KEY` | OpenRouter | API authentication |
| `LITIGATION_CONFIG` | All | Path to config file (default: `litigation/config.yaml`) |

---

## Output

- **Transcripts:** `courtroom/transcripts/YYYY-MM-DD-[matter-slug].md`
- **State:** `state/current.md` updated with session outcome
- **CHANGELOG:** Updated if decisions were made (F3+)

---

## Canonical References

- `core/procedures.md` — Deliberation flow, session lifecycle
- `courtroom/RULES.md` — Transcript rules, titling
- `checklists/judge-morningstar.md` — Presiding checklist
- `.cursor/agents/morningstar.md` — MORNINGSTAR agent definition

---

> *"The court runs on silicon now. The rulings remain regrettably sensible."*
> — The Honorable Lucius J. Morningstar
