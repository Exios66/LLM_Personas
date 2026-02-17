// Morningstar Courtroom backend
// Node/Express proxy for OpenRouter + lightweight session logging

require('dotenv').config();

const express = require('express');
const cors = require('cors');
const morgan = require('morgan');
const rateLimit = require('express-rate-limit');

const app = express();
const PORT = process.env.PORT || 8787;

// --- Configuration helpers ---
const OPENROUTER_API_KEY = process.env.OPENROUTER_API_KEY;
const OPENROUTER_DEFAULT_MODEL = process.env.OPENROUTER_DEFAULT_MODEL || 'arcee-ai/trinity-large-preview:free';
const ALLOWED_ORIGINS = (process.env.ALLOWED_ORIGINS || '').split(',').map(s => s.trim()).filter(Boolean);

if (!OPENROUTER_API_KEY) {
  // Warn but do not crash; some environments may set it later
  console.warn('[morningstar-backend] OPENROUTER_API_KEY not set – /api/openrouter/chat will reject requests until configured.');
}

// Simple in-memory session store: { [sessionId]: { caseMeta, calls: [] } }
const sessions = Object.create(null);

// --- Middleware ---

app.use(express.json({ limit: '1mb' }));
app.use(morgan('tiny'));

app.use(
  cors({
    origin: function (origin, callback) {
      if (!origin) return callback(null, true); // non-browser / curl
      if (!ALLOWED_ORIGINS.length || ALLOWED_ORIGINS.includes(origin)) {
        return callback(null, true);
      }
      return callback(new Error('Origin not allowed by CORS'), false);
    }
  })
);

const limiter = rateLimit({
  windowMs: 60 * 1000, // 1 minute
  max: 60, // 60 requests per minute per IP
  standardHeaders: true,
  legacyHeaders: false
});

app.use('/api/', limiter);

// Ensure fetch is available (Node >= 18 recommended)
async function httpPostJson(url, options) {
  if (typeof fetch !== 'function') {
    throw new Error('Global fetch is not available – run on Node 18+ or add a fetch polyfill.');
  }
  const res = await fetch(url, options);
  return res;
}

// --- Routes ---

app.get('/api/health', (_req, res) => {
  res.json({
    ok: true,
    service: 'morningstar-courtroom-backend',
    node: process.version
  });
});

app.post('/api/openrouter/chat', async (req, res) => {
  try {
    if (!OPENROUTER_API_KEY) {
      return res.status(500).json({ error: 'Backend is not configured with OPENROUTER_API_KEY.' });
    }

    const {
      sessionId = 'anonymous',
      caseMeta = {},
      model,
      messages,
      options = {}
    } = req.body || {};

    if (!Array.isArray(messages) || messages.length === 0) {
      return res.status(400).json({ error: 'messages array is required.' });
    }

    const effectiveModel = model || OPENROUTER_DEFAULT_MODEL;

    const payload = {
      model: effectiveModel,
      messages,
      max_tokens: options.maxTokens || 2048,
      temperature: options.temperature ?? 0.7,
      stream: false
    };

    const response = await httpPostJson('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${OPENROUTER_API_KEY}`,
        'Content-Type': 'application/json',
        'HTTP-Referer': process.env.HTTP_REFERER || 'https://example.com',
        'X-Title': process.env.X_TITLE || 'Morningstar Courtroom Backend'
      },
      body: JSON.stringify(payload)
    });

    const text = await response.text();

    if (!response.ok) {
      console.warn('[openrouter] non-2xx response', response.status, text);
      return res.status(response.status).json({ error: 'OpenRouter error', details: text });
    }

    let data;
    try {
      data = JSON.parse(text);
    } catch (e) {
      console.error('[openrouter] failed to parse JSON', e);
      return res.status(502).json({ error: 'Invalid JSON from OpenRouter' });
    }

    // Minimal logging into in-memory session store
    const now = new Date().toISOString();
    if (!sessions[sessionId]) {
      sessions[sessionId] = {
        id: sessionId,
        caseMeta,
        createdAt: now,
        lastUpdatedAt: now,
        calls: []
      };
    }
    const session = sessions[sessionId];
    session.caseMeta = { ...session.caseMeta, ...caseMeta };
    session.lastUpdatedAt = now;

    const usage = data.usage || {};
    session.calls.push({
      at: now,
      phase: caseMeta.phase || null,
      model: effectiveModel,
      promptTokens: usage.prompt_tokens || null,
      completionTokens: usage.completion_tokens || null,
      totalTokens: usage.total_tokens || null,
      promptSummary: JSON.stringify(messages[messages.length - 1] || {}).slice(0, 200),
      responseSummary: JSON.stringify(data.choices?.[0]?.message || {}).slice(0, 200)
    });

    res.json(data);
  } catch (err) {
    console.error('[openrouter-chat] unexpected error', err);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/sessions/:sessionId/logs', (req, res) => {
  const { sessionId } = req.params;
  const session = sessions[sessionId];
  if (!session) {
    return res.status(404).json({ error: 'Session not found' });
  }
  res.json(session);
});

app.post('/api/sessions/:sessionId/annotate', (req, res) => {
  const { sessionId } = req.params;
  const { note, tag } = req.body || {};
  if (!note) {
    return res.status(400).json({ error: 'note is required' });
  }
  const now = new Date().toISOString();
  if (!sessions[sessionId]) {
    sessions[sessionId] = {
      id: sessionId,
      caseMeta: {},
      createdAt: now,
      lastUpdatedAt: now,
      calls: []
    };
  }
  const session = sessions[sessionId];
  session.lastUpdatedAt = now;
  session.calls.push({
    at: now,
    phase: 'annotation',
    model: null,
    promptTokens: null,
    completionTokens: null,
    totalTokens: null,
    promptSummary: `NOTE[${tag || 'info'}]: ${note.slice(0, 200)}`,
    responseSummary: null
  });
  res.json({ ok: true });
});

// Fallback 404
app.use((_req, res) => {
  res.status(404).json({ error: 'Not found' });
});

app.listen(PORT, () => {
  console.log(`[morningstar-backend] listening on port ${PORT}`);
});

