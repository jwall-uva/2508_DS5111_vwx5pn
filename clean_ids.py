"""
Validates YouTube video IDs from stdin.
"""
import sys
import re
import logging

logging.basicConfig(
    filename="pipelinepipeline_autid.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def youtube_id_validation(video_id):
    """Check for 11-char pattern."""
    valid = r'^[A-Za-z0-9_-]{11}$'
    return bool(re.match(valid, video_id))

def main():
    """Reads stdin and processes each ID."""
    try:
        for line in sys.stdin:
            video_id = line.strip()

            if not id:
                continue
            if youtube_id_validation(video_id):
                print(video_id)
            else:
                logging.warning("Invalid ID: %s", video_id)

    except KeyboardInterrupt:
        print()

if __name__ == "__main__":
    main()
