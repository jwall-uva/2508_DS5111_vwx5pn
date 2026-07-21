"""Gemini LLM strategy implementation."""

from google import genai

from llm_strategy import LLMStrategy

# pylint: disable=too-few-public-methods
class GeminiStrategy(LLMStrategy):
    """LLM strategy that uses Google's Gemini API."""

    def __init__(self, api_key: str):
        """Initialize the Gemini client and response schema."""

        if not api_key:
            raise ValueError("Gemini API key is required.")

        self.client = genai.Client(api_key=api_key)

        self.response_schema = {
             "type": "OBJECT",
        "properties": {
            "video_id": {
                "type": "STRING"
            },
            "cleaned_text": {
                "type": "STRING"
            },
            "tech_terms": {
                "type": "ARRAY",
                "items": {
                    "type": "STRING"}
            },
            "book_names": {
                "type": "ARRAY",
                "items": {
                    "type": "STRING"}
            }
        },
        "required": [
            "video_id", 
            "cleaned_text",
            "tech_terms",
            "book_names"]
        }

