"""Mock implementation of the transcript enrichment interface."""

import re
from llm_strategy import LLMStrategy

# pylint: disable=too-few-public-methods
class MockLLMEnricher(LLMStrategy):
    """Mock transcript enricher for deterministic unit testing."""

    def __init__(self, tech_keywords: list[str], book_keywords: list[str]) -> None:
        """Initialize the mock enricher with keyword lists."""
        self.tech_keywords = tech_keywords
        self.book_keywords = book_keywords

    def run(self, video_id: str, raw_text: str) -> dict:
        """Return structured enrichment data for a transcript."""

        # Remove timestamps such as 00:45 or 1:05:30.
        cleaned_text = re.sub(r"\b\d{1,2}(?::\d{2})+\b", "", raw_text)

        # Collapse repeated whitespace and trim.
        cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()

        # Case-insensitive keyword matching while preserving original casing.
        lower_text = raw_text.lower()

        tech_terms = [
            keyword
            for keyword in self.tech_keywords
            if keyword.lower() in lower_text
        ]

        book_names = [
            keyword
            for keyword in self.book_keywords
            if keyword.lower() in lower_text
        ]

        return {
            "video_id": video_id,
            "cleaned_text": cleaned_text,
            "tech_terms": tech_terms,
            "book_names": book_names,
        }
