
ENV = env
PYTHON = $(ENV)/bin/python3
PIP = $(ENV)/bin/pip
PYLINT = $(ENV)/bin/pylint
PYTEST = $(ENV)/bin/pytest

default:
	@cat Makefile

env:
	python3 -m venv $(ENV)
	$(PIP) install --upgrade pip

update: env
	$(PIP) install -r requirements.txt

lint:
	$(PYLINT) bin/clean_ids.py

test: lint
	$(PYTEST) -vv tests

test_enrich:
	cat data/mock_transcript.jsonl | $(PYTHON) -u bin/enrich_transcripts.py	. env/bin/activate; pip install -r requirements.txt

lint:
	pylint clean_ids.py

test: lint
	pytest -vv tests

test_enrich:
	@. env/bin/activate && cat mock_transcripts.jsonl | python -u bin/enrich_transcripts. py | python bin/validate_schema.py
