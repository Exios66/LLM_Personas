"""Web search client for Research Report workflow.

Primary: Tavily API (TAVILY_API_KEY). Fallback: DuckDuckGo (no key required).
"""

import os
from dataclasses import dataclass


@dataclass
class SearchResult:
    """Single search result with source attribution."""

    title: str
    url: str
    snippet: str
    source: str


def search_web(query: str, max_results: int = 10) -> tuple[list[SearchResult], str]:
    """
    Search the web for a query. Uses Tavily if TAVILY_API_KEY is set,
    otherwise falls back to DuckDuckGo (no API key required).

    Returns:
        Tuple of (list of SearchResult, search_backend_name)
    """
    api_key = os.environ.get("TAVILY_API_KEY", "").strip()
    if api_key:
        return _search_tavily(query, max_results, api_key), "tavily"
    return _search_duckduckgo(query, max_results), "duckduckgo"


def _search_tavily(query: str, max_results: int, api_key: str) -> list[SearchResult]:
    """Search using Tavily API (optimized for AI/RAG)."""
    try:
        from tavily import TavilyClient

        client = TavilyClient(api_key=api_key)
        response = client.search(query, max_results=min(max_results, 10))
        results = []
        for r in response.get("results", []):
            url = r.get("url", "")
            results.append(
                SearchResult(
                    title=r.get("title", ""),
                    url=url,
                    snippet=r.get("content", r.get("snippet", "")),
                    source=_domain_from_url(url),
                )
            )
        return results
    except Exception as e:
        raise RuntimeError(f"Tavily search failed: {e}") from e


def _search_duckduckgo(query: str, max_results: int) -> list[SearchResult]:
    """Fallback: DuckDuckGo text search (no API key required)."""
    try:
        from duckduckgo_search import DDGS

        ddgs = DDGS()
        raw = list(ddgs.text(query, max_results=max_results))
        return [
            SearchResult(
                title=r.get("title", ""),
                url=r.get("href", r.get("url", "")),
                snippet=r.get("body", r.get("snippet", "")),
                source=_domain_from_url(r.get("href", r.get("url", ""))),
            )
            for r in raw
        ]
    except Exception as e:
        raise RuntimeError(f"DuckDuckGo search failed: {e}") from e


def _domain_from_url(url: str) -> str:
    """Extract domain from URL for source attribution."""
    if not url:
        return "unknown"
    try:
        from urllib.parse import urlparse

        netloc = urlparse(url).netloc
        return netloc.replace("www.", "") if netloc else "unknown"
    except Exception:
        return "unknown"
