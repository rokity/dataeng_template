# Makefile for Python project using Poetry, Black, Ruff, Pytest, and Coverage

.PHONY: install lint format test coverage clean

# Install all dependencies
install:
	poetry install
	poetry run pre-commit install

# Run Ruff linter
lint:
	poetry run ruff check .

# Auto-format code with Black
format:
	poetry run black .

# Run tests with pytest
test:
	poetry run pytest

# Run tests with coverage and generate report
coverage:
	poetry run coverage run -m unittest discover -v
	poetry run coverage report -m
	@echo "Coverage report generated at .coverage"

validate:
	poetry run black --check src
	poetry run black --check tests
	$(lint)

testenv:
	$(validate)
	$(coverage)
