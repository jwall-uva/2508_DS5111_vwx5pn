import pytest
from youtube_transcript_api import YouTubeTranscriptApi

# Import YOUR function
from extract_transcipts import extract_transcript


# Fake transcript object
class DummyFetchedTranscript:
    def to_raw_data(self):
        return [
            {"start": 0.0, "duration": 2.5, "text": "Hello world"},
            {"start": 2.5, "duration": 3.0, "text": "Data engineering testing"}
        ]


def test_extract_transcript(monkeypatch):

    # Fake replacement for the real API call
    def mock_fetch(self, video_id):
        assert video_id == "test_id_123"
        return DummyFetchedTranscript()

    # Replace YouTubeTranscriptApi.fetch with our fake version
    monkeypatch.setattr(YouTubeTranscriptApi, "fetch", mock_fetch)

    # Call YOUR function
    transcript = extract_transcript("test_id_123")

    # Verify the results
    assert len(transcript) == 2
    assert transcript[0]["text"] == "Hello world"
    assert transcript[1]["text"] == "Data engineering testing"
