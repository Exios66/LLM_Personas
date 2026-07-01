"""Regression tests for research workflow web search helpers."""

from __future__ import annotations

import pytest

from agents.workflows.search import SearchResult, _domain_from_url, search_web


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("https://www.bbc.com/news/article", "bbc.com"),
        ("https://reuters.com/world", "reuters.com"),
        ("", "unknown"),
        ("not-a-url", "unknown"),
    ],
)
def test_domain_from_url(url: str, expected: str) -> None:
    assert _domain_from_url(url) == expected


def test_search_web_uses_tavily_when_key_set(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TAVILY_API_KEY", "tvly-test")

    class FakeClient:
        def __init__(self, api_key: str) -> None:
            assert api_key == "tvly-test"

        def search(self, query: str, max_results: int = 10) -> dict:
            return {
                "results": [
                    {
                        "title": "Example",
                        "url": "https://example.com/page",
                        "content": "Snippet text",
                    }
                ]
            }

    monkeypatch.setitem(__import__("sys").modules, "tavily", type("m", (), {"TavilyClient": FakeClient})())

    results, backend = search_web("test query", max_results=5)
    assert backend == "tavily"
    assert len(results) == 1
    assert results[0] == SearchResult(
        title="Example",
        url="https://example.com/page",
        snippet="Snippet text",
        source="example.com",
    )


def test_search_web_falls_back_to_duckduckgo(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)

    class FakeDDGS:
        def text(self, query: str, max_results: int = 10):
            yield {
                "title": "DDG Result",
                "href": "https://duck.com/result",
                "body": "Body text",
            }

    monkeypatch.setitem(
        __import__("sys").modules,
        "duckduckgo_search",
        type("m", (), {"DDGS": FakeDDGS})(),
    )

    results, backend = search_web("fallback query")
    assert backend == "duckduckgo"
    assert len(results) == 1
    assert results[0].title == "DDG Result"
    assert results[0].source == "duck.com"
