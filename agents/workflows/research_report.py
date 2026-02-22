#!/usr/bin/env python3
"""
Research Report Workflow — Multi-Agent Pipeline

Four sequential agents: Researcher → Fact-Checker → Report Writer → Formatter.
Uses gpt-4.1-mini via OpenRouter. Saves report with alphanumeric ID + timestamp.
Sends via Gmail when recipient provided.
"""

import argparse
import os
import random
import string
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT))

# Load .env from agents/workflows/ or agents/
_env_paths = [
    Path(__file__).resolve().parent / ".env",
    REPO_ROOT / "agents" / ".env",
    REPO_ROOT / ".env",
]
for _p in _env_paths:
    if _p.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(_p)
        except ImportError:
            pass
        break


MODEL = "openai/gpt-4.1-mini"
REPORTS_DIR = Path(__file__).resolve().parent.parent / "reports"


def _load_config() -> dict:
    """Load workflow config from YAML."""
    config_path = Path(__file__).resolve().parent / "config.yaml"
    if config_path.exists():
        try:
            import yaml
            return yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        except Exception:
            pass
    return {}


def _get_llm_provider():
    """Create LLM provider (OpenRouter with gpt-4.1-mini)."""
    from litigation.providers import get_provider, ProviderError

    config = _load_config()
    provider_name = config.get("provider", "openrouter")
    model = config.get("model") or MODEL
    base_url = config.get("openrouter", {}).get("base_url", "https://openrouter.ai/api/v1")

    return get_provider(
        provider=provider_name,
        model=model,
        openrouter_base_url=base_url,
    )


def _llm_complete(system_prompt: str, user_prompt: str, *, max_tokens: int = 4096) -> str:
    """Call LLM via provider."""
    provider = _get_llm_provider()
    config = _load_config()
    temp = config.get("temperature", 0.5)
    return provider.complete(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        max_tokens=max_tokens,
        temperature=temp,
    )


def _generate_report_id() -> str:
    """Generate alphanumeric report ID, e.g. RPT_A1B2C3D4."""
    chars = string.ascii_uppercase + string.digits
    suffix = "".join(random.choices(chars, k=8))
    return f"RPT_{suffix}"


def _timestamp_short() -> str:
    """Short-form timestamp: YYYYMMDD_HHMMSS."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def _agent_researcher(topic: str) -> str:
    """Agent 1: Gather recent, credible information via web search."""
    from agents.workflows.search import search_web

    queries = [
        f"{topic} recent developments 2025",
        f"{topic} authoritative sources",
    ]
    all_results = []
    seen_urls = set()
    backend = "unknown"
    for q in queries:
        results, backend = search_web(q, max_results=8)
        for r in results:
            if r.url not in seen_urls:
                seen_urls.add(r.url)
                all_results.append(r)

    search_context = "\n\n".join(
        f"[{i+1}] {r.title}\nURL: {r.url}\nSource: {r.source}\nSnippet: {r.snippet}"
        for i, r in enumerate(all_results)
    )

    system = """You are a Researcher Agent. Your job is to gather recent, credible information about a user-provided topic using the provided web search results.

Output your findings in the following structured format. For EACH distinct fact or claim you extract:
- Start a line with "FACT: " followed by the fact (concise, one sentence).
- On the next line, "SOURCES: " followed by the URL(s) where you found it, comma-separated.
- Separate fact blocks with "---"

Prioritize:
1. Recent information (2024-2025 when available)
2. Authoritative sources (gov, edu, established news, official sites)
3. Cite the exact URL for each fact

If search results are sparse, extract what you can and note limitations. Do not invent facts."""

    user = f"""Topic: {topic}

Web search results (backend: {backend}):

{search_context}

Extract and structure all relevant, credible findings. Use the FACT:/SOURCES: format for each."""

    return _llm_complete(system, user)


def _agent_fact_checker(researcher_output: str) -> str:
    """Agent 2: Mark fact as verified ONLY if it appears in ≥2 independent sources."""
    system = """You are a Fact-Checker Agent. You receive findings from a Researcher and must verify them.

VERIFICATION RULE: A fact is VERIFIED only if it appears in at least TWO independent sources.
- "Independent" means different domains/organizations (e.g. bbc.com and reuters.com, not bbc.com and bbc.co.uk).
- Extract the domain from each URL to assess independence.
- If a fact has only one source, mark it REJECTED.
- If a fact has 2+ independent sources, mark it VERIFIED.

Output format:
- For each VERIFIED fact: "VERIFIED: [fact]. SOURCES: [list of 2+ independent URLs]"
- For each REJECTED fact: "REJECTED: [fact]. REASON: Only 1 source (or sources not independent)."
- Separate blocks with "---"

Include only facts from the Researcher's output. Do not add new facts."""

    user = f"""Researcher findings:

{researcher_output}

Apply the verification rule. Output only VERIFIED and REJECTED blocks."""

    return _llm_complete(system, user)


def _agent_report_writer(verified_facts: str) -> str:
    """Agent 3: Combine verified facts into a clear report under 1,000 words."""
    system = """You are a Report Writer Agent. You receive verified facts from a Fact-Checker and write a clear, well-structured report.

Requirements:
- Use ONLY the verified facts provided. Do not add information from elsewhere.
- Write in a professional, informative style.
- Structure with a brief intro, logical sections, and a short conclusion.
- Stay UNDER 1,000 words.
- Cite sources inline where appropriate (e.g. "According to X and Y...").
- Output plain text or light Markdown (no HTML yet)."""

    user = f"""Verified facts from Fact-Checker:

{verified_facts}

Combine these into a single, coherent report under 1,000 words."""

    return _llm_complete(system, user, max_tokens=2048)


def _agent_formatter(report_text: str, topic: str) -> str:
    """Agent 4: Format report into clean, professional HTML for email body."""
    system = """You are a Formatter Agent. You receive a report and convert it to clean, professional HTML suitable for an email body.

Requirements:
- Valid HTML only (no head, no body tags; just the content suitable for insertion into an email body).
- Use semantic tags: <h2>, <h3>, <p>, <ul>, <li>, <strong>, <em>, <a> as appropriate.
- Inline styles are acceptable for basic formatting (e.g. font-family, font-size, line-height).
- Keep it simple and readable. Avoid complex layouts.
- Ensure links have href attributes.
- No placeholder text or [brackets]. Output complete, usable HTML."""

    user = f"""Report to format as HTML:

{report_text}

Topic: {topic}

Produce clean HTML suitable for an email body. No wrapper document, just the content block."""

    return _llm_complete(system, user, max_tokens=2048)


def _ensure_html_wrapped(html: str) -> str:
    """Wrap raw HTML in a minimal document if needed for email client compatibility."""
    html = html.strip()
    if not html.startswith("<"):
        return f"<div>\n{html}\n</div>"
    if "<html" not in html.lower() and "<body" not in html.lower():
        return f'<div style="font-family: Georgia, serif; font-size: 14px; line-height: 1.6;">\n{html}\n</div>'
    return html


def run_pipeline(topic: str) -> tuple[str, str, str]:
    """
    Run the 4-agent pipeline. Returns (report_id, timestamp, html_content).
    """
    report_id = _generate_report_id()
    ts = _timestamp_short()

    print("Agent 1: Researcher...", file=sys.stderr)
    findings = _agent_researcher(topic)

    print("Agent 2: Fact-Checker...", file=sys.stderr)
    verified = _agent_fact_checker(findings)

    print("Agent 3: Report Writer...", file=sys.stderr)
    report_text = _agent_report_writer(verified)

    print("Agent 4: Formatter...", file=sys.stderr)
    html = _agent_formatter(report_text, topic)
    html = _ensure_html_wrapped(html)

    return report_id, ts, html


def save_report(report_id: str, timestamp: str, html: str, topic: str) -> Path:
    """Save report to agents/reports/{report_id}_{timestamp}.html"""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{report_id}_{timestamp}.html"
    path = REPORTS_DIR / filename
    header = f"<!-- Report ID: {report_id} | Generated: {timestamp} | Topic: {topic} -->\n"
    path.write_text(header + html, encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Multi-agent research report: Researcher → Fact-Checker → Report Writer → Formatter"
    )
    parser.add_argument("topic", help="Topic to research")
    parser.add_argument("--to", dest="recipient", help="Optional: email recipient (sends via Gmail)")
    parser.add_argument("--no-save", action="store_true", help="Do not save report file")
    args = parser.parse_args()

    if not os.environ.get("OPENROUTER_API_KEY"):
        print(
            "ERROR: OPENROUTER_API_KEY required. Set it in agents/workflows/.env or environment.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Topic: {args.topic}", file=sys.stderr)
    print("-" * 50, file=sys.stderr)

    report_id, timestamp, html = run_pipeline(args.topic)

    if not args.no_save:
        path = save_report(report_id, timestamp, html, args.topic)
        print(f"Saved: {path}", file=sys.stderr)

    subject = f"Research Report: {args.topic[:60]}{'...' if len(args.topic) > 60 else ''}"

    if args.recipient:
        try:
            from agents.workflows.email_sender import send_report_email
            send_report_email(html, subject, args.recipient)
            print(f"Sent to: {args.recipient}", file=sys.stderr)
        except ValueError as e:
            print(f"Gmail not configured: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Send failed: {e}", file=sys.stderr)
            sys.exit(1)

    print(f"\nReport ID: {report_id} | Timestamp: {timestamp}", file=sys.stderr)
    print(html[:500] + "..." if len(html) > 500 else html)


if __name__ == "__main__":
    main()
