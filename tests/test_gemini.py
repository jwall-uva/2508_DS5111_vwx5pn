import io
import json
import sys

from transcript_enricher_engine import TranscriptEnricher
from mock_llm_strategy import MockLLMStrategy


def test_run_stream_with_mock_strategy(monkeypatch, capsys):
    """Test that TranscriptEnricher processes JSONL input correctly."""

    input_data = (
        '{"video_id": "ds5111_v001", '
        '"raw_text": "00:01 Welcome back to class! Today we are discussing '
        'Snowflake VARIANT columns and dbt staging transformations. '
        "Let's look at how to unpack semi-structured records. "
        "Make sure to refer to Martin Kleppmann's text, "
        'Designing Data-Intensive Applications. '
        '00:45 Next, configure the staging view using a standard SELECT '
        'query statement."}\n'
    )

    monkeypatch.setattr(sys, "stdin", io.StringIO(input_data))

    strategy = MockLLMStrategy(
        tech_keywords=["Snowflake", "dbt", "SELECT"],
        book_keywords=["Designing Data-Intensive Applications"],
    )

    engine = TranscriptEnricher(strategy)
    engine.run_stream()

    captured = capsys.readouterr()
    result = json.loads(captured.out)

    expected = {
        "video_id": "ds5111_v001",
        "cleaned_text": (
            "Welcome back to class! Today we are discussing Snowflake VARIANT "
            "columns and dbt staging transformations. Let's look at how to "
            "unpack semi-structured records. Make sure to refer to Martin "
            "Kleppmann's text, Designing Data-Intensive Applications. Next, "
            "configure the staging view using a standard SELECT query statement."
        ),
        "tech_terms": ["Snowflake", "dbt", "SELECT"],
        "book_names": ["Designing Data-Intensive Applications"],
    }

    assert result == expected
