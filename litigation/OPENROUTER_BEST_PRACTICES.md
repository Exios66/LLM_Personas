# OpenRouter Best Practices for MORNINGSTAR Courtroom

> *Core practices for effective, reliable deliberation execution via OpenRouter*

This document consolidates OpenRouter's recommended best practices and applies them to the MORNINGSTAR litigation runner and courtroom design. Reference: [OpenRouter Documentation](https://openrouter.ai/docs).

---

## 1. Authentication & Attribution

### API Key

- **Required:** `OPENROUTER_API_KEY` in environment or `litigation/providers/.env`
- **Format:** Bearer token; set `Authorization: Bearer <key>`
- **Security:** Never commit keys; use `.env` (gitignored) or system env

### App Attribution Headers

Optional headers improve discoverability and analytics on openrouter.ai:

| Header | Purpose |
|--------|---------|
| `HTTP-Referer` | Your app's URL (e.g. repo URL, deployment URL) |
| `X-Title` | Display name for rankings (e.g. "MORNINGSTAR Courtroom") |

**Config:** Set in `litigation/config.yaml` under `openrouter.app_attribution`:

```yaml
openrouter:
  app_attribution:
    http_referer: "https://github.com/Exios66/LLM_Personas"
    x_title: "MORNINGSTAR Courtroom"
```

---

## 2. Credits & Reliability

### Credit Balance

- **Recommended minimum:** $10–20 to avoid forced credit checks and latency spikes
- **Auto-topup:** Enable at [openrouter.ai/settings](https://openrouter.ai/settings) for uninterrupted deliberation
- **Free models:** Use `:free` suffix (e.g. `qwen/qwen3-next-80b-a3b-instruct:free`); configure [Privacy Settings](https://openrouter.ai/settings/privacy) if you see "No endpoints matching data policy"

### Latency Expectations

- **Cache warming:** First 1–2 minutes in new regions may have higher latency
- **Low credits:** Latency can increase when balance is low
- **Mitigation:** Maintain healthy balance; use `provider.sort: "throughput"` for time-sensitive deliberations

---

## 3. Provider Routing

OpenRouter routes requests across providers. Customize via the `provider` object in the request body.

### Default Behavior

- **Load balancing:** By price (inverse square); fallback on 5xx or rate limit
- **Fallbacks:** `allow_fallbacks: true` (default) — backup providers when primary unavailable

### Routing Options for Courtroom Use

| Option | Use Case | Example |
|--------|----------|---------|
| `sort` | Prioritize latency, throughput, or price | `sort: "latency"` for expedited hearings |
| `order` | Try providers in sequence | `order: ["anthropic", "openai"]` |
| `allow_fallbacks` | Enable/disable backup providers | `allow_fallbacks: true` (recommended) |
| `max_price` | Cap cost per request | `max_price: { prompt: 0.001, completion: 0.002 }` |
| `preferred_max_latency` | Prefer providers under N seconds | `preferred_max_latency: 30` |
| `preferred_min_throughput` | Prefer providers above N tokens/sec | `preferred_min_throughput: 50` |
| `data_collection` | Restrict to providers that don't store data | `data_collection: "deny"` for sensitive matters |
| `zdr` | Zero Data Retention only | `zdr: true` for confidential deliberations |

### Nitro Shortcut

Append `:nitro` to model slug for throughput priority:  
`meta-llama/llama-3.3-70b-instruct:nitro` ≈ `provider.sort: "throughput"`

---

## 4. Model Selection

### Model List

- **Organization prefix required:** e.g. `openai/gpt-4`, `anthropic/claude-3`
- **Free tier:** Use `:free` suffix to avoid billing
- **Slot machine:** When no model set, litigation runner picks randomly from `openrouter.models` for load distribution
- **Interactive:** Use `--model-select` to choose from list

### Fallback on Failure

OpenRouter automatically retries with other providers on 5xx or rate limit. No extra code needed when `allow_fallbacks: true`.

---

## 5. Request Parameters

### Generation Parameters

| Parameter | Courtroom Default | Notes |
|-----------|-------------------|-------|
| `max_tokens` | 8192 (capped 32k) | Sufficient for full deliberation; increase for long transcripts |
| `temperature` | 0.7 | Balances creativity (Prophet) and consistency (Architect) |
| `top_p` | — | Optional; some models support |
| `frequency_penalty` | — | Reduces repetition in long outputs |

### Structured Outputs (Optional)

For machine-parseable rulings, use `response_format`:

```json
{ "type": "json_object" }
```

Or strict schema via `json_schema`. Check [models page](https://openrouter.ai/models?supported_parameters=structured_outputs) for support.

### Assistant Prefill

Guide the model by including a partial assistant message at the end of `messages`:

```json
[
  { "role": "user", "content": "Deliberate on REST vs GraphQL." },
  { "role": "assistant", "content": "RULING: " }
]
```

Useful for enforcing output format (e.g. "RULING: ...").

---

## 6. Plugins (Optional)

OpenRouter plugins extend model capabilities:

| Plugin | Use Case |
|--------|----------|
| `web` | Real-time web search during deliberation (e.g. precedent lookup) |
| `file-parser` | PDF/attachment parsing |
| `response-healing` | Automatic JSON repair for structured outputs |

Enable via `plugins` array in request. See [Plugins docs](https://openrouter.ai/docs/guides/features/plugins).

---

## 7. Usage & Auditing

### Response Usage

OpenRouter returns `usage` with:

- `prompt_tokens`, `completion_tokens`, `total_tokens`
- `cost` (credits)
- `prompt_tokens_details.cached_tokens` (cache hits)
- `completion_tokens_details.reasoning_tokens` (for reasoning models)

### Generation Stats API

Query `/api/v1/generation?id=<generation_id>` for historical token counts and cost. Useful for auditing deliberation costs.

---

## 8. User Identifier (Abuse Prevention)

Set `user` in the request body to a stable identifier for your end-users. Helps OpenRouter detect and prevent abuse:

```json
{ "user": "morningstar-session-2026-02-19" }
```

---

## 9. Courtroom-Specific Recommendations

### By Hearing Type

| Hearing Type | Recommendation |
|--------------|----------------|
| **Standard** | Default routing; `sort: "price"` for cost efficiency |
| **Expedited** | `sort: "latency"` or `:nitro` model; `preferred_max_latency: 30` |
| **Special Inquiry** | Consider `web` plugin for external fact-checking |
| **Contempt** | `data_collection: "deny"` or `zdr: true` if matter is sensitive |

### For Long Deliberations

- Increase `max_tokens` in config (up to 32k)
- Use `--no-spectators` to reduce prompt size
- Prefer models with large context (128k+ when available)

### For Cost Control

- Use free models (`:free`) when quality suffices
- Set `max_price` in provider preferences
- Monitor usage via OpenRouter dashboard

---

## 10. Config Integration

Best practices are applied via `litigation/config.yaml`:

```yaml
openrouter:
  base_url: https://openrouter.ai/api/v1
  app_attribution:
    http_referer: "https://github.com/Exios66/LLM_Personas"
    x_title: "MORNINGSTAR Courtroom"
  provider:
    allow_fallbacks: true
    sort: "price"          # or "latency" | "throughput"
    # data_collection: "deny"   # Uncomment for sensitive matters
    # zdr: true                 # Zero Data Retention
  models:
    - qwen/qwen3-next-80b-a3b-instruct:free
    # ...
```

See `litigation/config.example.yaml` for full template.

---

## References

- [OpenRouter API Reference](https://openrouter.ai/docs/api/reference/overview)
- [Provider Routing](https://openrouter.ai/docs/guides/routing/provider-selection)
- [Latency & Performance](https://openrouter.ai/docs/guides/best-practices/latency-and-performance)
- [App Attribution](https://openrouter.ai/docs/app-attribution)
- [Privacy Settings](https://openrouter.ai/settings/privacy)

---

> *"The court demands reliability. The router delivers."*  
> — MORNINGSTAR::ENGINEER
