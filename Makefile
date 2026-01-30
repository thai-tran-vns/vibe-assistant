.PHONY: all setup install test clean help

# Default target
all: install setup test

setup: ## Create necessary project directories and files
	mkdir -p core tests logs
	touch core/__init__.py
	@echo "Project structure created."

install: ## Install dependencies using uv
	uv sync
	@echo "Dependencies installed."

test: ## Run tests using pytest
	uv run pytest
	@echo "Tests completed."

clean: ## Clean up cache files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "Cleaned up cache files."

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'