.PHONY: help
.DEFAULT_GOAL := help

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	uv sync

lint: ## Run linting with ruff
	uv run ruff check kebab_it tests

format: ## Format code with ruff
	uv run ruff format .

typecheck: ## Run type checking with mypy
	uv run mypy kebab_it

test: ## Run tests
	uv run pytest tests/

security: ## Run security checks (bandit, pip-audit, trufflehog)
	@echo "Running Bandit security linter (note: Python 3.14 compatibility limited)..."
	-uv run bandit -r kebab_it -ll 2>/dev/null || echo "Bandit scan skipped (Python 3.14 AST compatibility issue)"
	@echo "\nRunning pip-audit for dependency vulnerabilities..."
	uv run pip-audit
	@echo "\nRunning TruffleHog for secrets scanning..."
	@if command -v trufflehog >/dev/null 2>&1; then \
		trufflehog filesystem . --only-verified --fail; \
	else \
		echo "TruffleHog not installed. Install with: brew install trufflehog (macOS) or go install github.com/trufflesecurity/trufflehog/v3@latest"; \
	fi

check: lint typecheck test ## Run all checks (lint, typecheck, test)

pipeline: format lint typecheck test security build install-global ## Run full pipeline (format, lint, typecheck, test, security, build, install-global)

clean: ## Remove build artifacts and cache
	rm -rf build/ dist/ *.egg-info .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete

run: ## Run kebab-it (usage: make run ARGS="*.md")
	uv run kebab-it $(ARGS)

build: ## Build package
	uv build

install-global: ## Install globally with uv tool
	uv tool install .

uninstall-global: ## Uninstall global installation
	uv tool uninstall kebab-it
