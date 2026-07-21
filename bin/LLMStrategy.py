"""Defines the abstract interface for LLM strategies."""

from abc import ABC, abstractmethod


# pylint: disable=too-few-public-methods
class LLMStrategy(ABC):
    """Abstract interface for executing LLM strategies."""

    @abstractmethod
    def run(self, video_id: str, raw_text: str) -> dict:
        """Run the LLM strategy and return structured output."""
