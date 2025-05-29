# Makefile for Python project using Poetry, Black, Ruff, Pytest, and Coverage

.PHONY: install lint format test coverage clean

# Install all dependencies
install:
	poetry install

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

testenv:
	black --check src
	black --check tests
	$(lint)
	$(coverage)
	
# Remove .pyc files and __pycache__ directories
clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.pyc' -delete
	rm -rf .pytest_cache .ruff_cache htmlcov .coverage
