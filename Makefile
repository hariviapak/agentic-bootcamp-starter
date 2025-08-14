.PHONY: setup run test format

setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

run:
	python -m src.agentic_bootcamp.app

test:
	pytest -q

format:
	python -m pip install ruff black
	ruff check --fix src tests
	black src tests
