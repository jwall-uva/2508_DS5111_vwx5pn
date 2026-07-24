"""Engine for streaming transcript enrichment."""

import json
import sys

from llm_strategy import LLMStrategy


# pylint: disable=too-few-public-methods
# This class intentionally exposes only run_stream as its public interface.
class TranscriptEnricher:
    """Streams transcript records through a transcript enrichment strategy."""

    def __init__(self, strategy: LLMStrategy):
        """Initialize the engine with an enrichment strategy."""
        self.strategy = strategy

    def run_stream(self):
        """Read transcript records and write enriched records to stdout."""
        for line in sys.stdin:
            line = line.strip()

            if not line:
                continue

            try:
                payload = json.loads(line)
                video_id = payload["video_id"]
                raw_text = payload["raw_text"]
            except json.JSONDecodeError:
                print("Invalid JSON input.", file=sys.stderr)
                continue
            except KeyError as error:
                print(f"Missing required field: {error}", file=sys.stderr)
                continue

            try:
                enriched = self.strategy.run(
                    video_id,
                    raw_text,
                )
            except Exception as error:  # pylint: disable=broad-exception-caught
                print(
                    f"Failed to enrich transcript '{video_id}': {error}",
                    file=sys.stderr,
                )
                continue

            print(json.dumps(enriched))
