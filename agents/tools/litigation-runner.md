# Tool: Litigation Runner

**Implementation:** `litigation/run.py`  
**Purpose:** Run MORNINGSTAR courtroom deliberation via Ollama, LM Studio, or OpenRouter and produce a transcript.

## Invocation

From project root:

```bash
python litigation/run.py "Matter for the court to deliberate"
```

Or with options:

```bash
python litigation/run.py "Matter" --provider openrouter --hearing-type standard --save-to courtroom
```

## Inputs

| Input | Description |
|-------|--------------|
| **matter** | Free-text description of the matter before the court. |
| **--feasibility** | F0–F5 (default F3). |
| **--provider** | `ollama` \| `lm_studio` \| `openrouter`. |
| **--model** | Override config model. |
| **--hearing-type** | `standard` \| `expedited` \| `special_inquiry` \| `contempt`. |
| **--no-spectators** | Exclude spectators from system prompt. |
| **--save-to** | `litigation` \| `courtroom` (transcript destination). |

## Outputs

- Transcript written to `litigation/transcripts/` or `courtroom/transcripts/` (date + slug).
- Console: full deliberation text.

## Config

- `litigation/config.yaml` — provider, model list, max_tokens, temperature.
- `litigation/providers/.env` — e.g. `OPENROUTER_API_KEY`.

## When to Use

Agents (or operators) invoke the litigation runner when a formal court deliberation is required and the output should be a certified transcript rather than an inline chat deliberation.
