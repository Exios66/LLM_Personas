## Morningstar Courtroom Backend

Optional Node/Express backend that the Dracula-styled `index.html` can call instead of hitting OpenRouter directly from the browser.

### Features

- **OpenRouter proxy** at `POST /api/openrouter/chat`
  - Frontend sends: `{ sessionId, caseMeta, model, messages, options }`
  - Backend injects `OPENROUTER_API_KEY`, forwards to `https://openrouter.ai/api/v1/chat/completions`, and returns the raw JSON response.
- **Lightweight session logging**
  - In-memory store keyed by `sessionId`.
  - Each call logged with phase, model, token usage, and short prompt/response summaries.
- **Session utilities**
  - `GET /api/sessions/:sessionId/logs` – retrieve logs for a given session.
  - `POST /api/sessions/:sessionId/annotate` – attach notes to a session log.

### Configuration

Set these environment variables before starting the server:

- `OPENROUTER_API_KEY` – **required** for `/api/openrouter/chat`.
- `OPENROUTER_DEFAULT_MODEL` – optional, defaults to `arcee-ai/trinity-large-preview:free`.
- `ALLOWED_ORIGINS` – optional, comma-separated list of allowed browser origins (e.g. `https://yourname.github.io`).
- `PORT` – optional, defaults to `8787`.
- `HTTP_REFERER` – optional referer header to send to OpenRouter (defaults to `https://example.com`).
- `X_TITLE` – optional title header, defaults to `Morningstar Courtroom Backend`.

Node 18+ is required (for built-in `fetch`).

### Running locally

```bash
cd backend
npm install
OPENROUTER_API_KEY=sk-or-v1-... npm start
```

The service will listen on `http://localhost:8787` by default.

### Frontend integration

In the Dracula `index.html`:

- Select **“Via backend proxy”** in the “Model routing” dropdown.
- Set the backend URL field to your deployment base, e.g.:
  - `http://localhost:8787` for local development, or
  - `https://your-backend.example.com` in production.

The frontend will POST to:

- `POST {backendUrl}/api/openrouter/chat`

with a `sessionId` equal to the case number, plus `caseMeta` (title, feasibility, phase) and OpenRouter `messages`. The backend returns the OpenRouter response unchanged so the UI can continue to operate exactly as in direct mode, but without ever exposing your OpenRouter key in the browser.

