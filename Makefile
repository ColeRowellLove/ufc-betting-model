.PHONY: install lint format typecheck test check up down

install:
	uv sync && uv run pre-commit install

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run mypy

test:
	uv run pytest

check: lint typecheck test
	uv run ruff format --check .

up:
	docker compose up -d

down:
	docker compose down
