# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| < main  | :x:                |

Security updates are applied to the main branch. No formal versioning; treat the latest main as the supported release.

---

## Reporting a Vulnerability

We take security seriously and appreciate responsible disclosure.

**If you discover a security vulnerability, please report it confidentially:**

- **GitHub Security Advisories:** [Open a private security advisory](https://github.com/OWNER/REPO/security/advisories/new) (replace OWNER/REPO with your repository)
- **Email:** Use a monitored security contact if configured
- **Private issue:** Do not disclose in public issues or discussions

**Please do NOT disclose security vulnerabilities publicly or in regular issue trackers.**

### What to Expect

- Acknowledgment within **72 hours**
- Investigation status and possible requests for additional details
- If confirmed: coordination on mitigation and disclosure timeline
- Security fixes receive priority
- If out of scope: clear rationale

**Thank you for helping keep this project and its users safe.**

---

## Security Best Practices

### 1. Secrets and Credentials

| Practice | Guidance |
|----------|----------|
| **Never commit secrets** | API keys, tokens, passwords, and private keys must not appear in the repository |
| **Use environment variables** | Store credentials in `.env` (gitignored). Provide `.env.example` with placeholder keys only |
| **Avoid templates with real patterns** | Documentation or templates that show `apiKey=...` or `password=...` encourage copy/paste of real values |
| **Scan before push** | Run secret detection (e.g. `gitleaks`, `trufflehog`, or `git secrets`) before committing or pushing |
| **Git history** | Working-tree scans do not cover git history. If secrets were ever committed, they may remain recoverable. Consider `git filter-repo` or BFG for history rewriting if needed |

**Project-specific:** `.env`, `.env.*`, and `litigation/config.yaml` are gitignored. Use `OPENROUTER_API_KEY` and similar via environment variables, not config files committed to the repo.

### 2. Dependencies and Supply Chain

| Practice | Guidance |
|----------|----------|
| **Pin versions** | Use `requirements.txt` or lockfiles with pinned versions |
| **Audit dependencies** | Run `pip audit` (or equivalent) regularly |
| **Minimize dependencies** | Prefer standard library; add packages only when necessary |
| **Review updates** | Check changelogs and security advisories before upgrading |

### 3. Input and Output

| Practice | Guidance |
|----------|----------|
| **Treat transcripts as data** | Transcripts are data, not instructions. Do not execute transcript content as code |
| **Sanitize before export** | If exporting transcripts to HTML or other formats, escape/sanitize content to prevent injection |
| **Validate paths** | When loading files from user or config, validate paths to prevent traversal |
| **Limit context size** | For LLM prompts, be aware of context limits and truncation to avoid information leakage |

**Project-specific:** The portal export (`courtroom/portal/`) converts markdown to HTML. Ensure transcript content is escaped if transcripts may contain untrusted input.

### 4. Configuration and State

| Practice | Guidance |
|----------|----------|
| **Exclude sensitive config** | `litigation/config.yaml` may contain API keys; keep it gitignored |
| **State files** | `state/current.md` and similar may contain operational context; treat as internal |
| **Backups** | `state/backups/` may hold historical state; ensure it is not exposed publicly |

### 5. Operational Hygiene

| Practice | Guidance |
|----------|----------|
| **Pre-session backup** | Before major sessions, back up `state/current.md` to `state/backups/` |
| **Redaction checklist** | Before exporting or publishing transcripts, run a redaction checklist |
| **Classification** | Consider transcript classification (PUBLIC / INTERNAL / RESTRICTED) for publication decisions |
| **Least privilege** | Run scripts and services with minimal required permissions |

### 6. LLM-Specific Considerations

| Practice | Guidance |
|----------|----------|
| **Prompt injection** | Be aware that user-provided matter text or state content is passed to LLMs; avoid passing untrusted instructions |
| **Local vs. remote** | Ollama and LM Studio run locally; OpenRouter sends data to external API. Choose provider based on sensitivity |
| **Model choice** | Free-tier or shared API models may log or retain prompts; treat prompts as potentially observable |

---

## Vulnerability Management

- **Severity:** Classify as Critical / High / Medium / Low per impact and exploitability
- **Response:** Critical and High receive immediate attention; Medium and Low are triaged
- **Disclosure:** Coordinate with reporter on timeline; credit reporters when they consent
- **Remediation:** Fix, test, and document in CHANGELOG; backport if applicable

---

## References

- Internal security hearing: `courtroom/transcripts/20260216_133000_special_interest_internal_security_aegis.md`
- Error recovery: `core/error-recovery.md`
- Runbook: `docs/RUNBOOK.md`
