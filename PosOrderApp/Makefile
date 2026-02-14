APP_NAME = restaurant-order
VENV_BIN = ./venv/bin
PYTHON = $(VENV_BIN)/python
MANAGE = $(PYTHON) ordersystem/manage.py

.PHONY: apigen setup clean lint format lint-fix lint-all test run help check-venv

check-venv:
	@if [ ! -d "venv" ]; then \
		echo "Error: Virtual environment not found."; \
		echo "Please run 'make setup' first."; \
		exit 1; \
	fi

help:
	@echo "Available commands:"
	@echo "  make setup      - Create venv and install dependencies"
	@echo "  make run        - Run the order processing CLI"
	@echo "  make test       - Run unit tests"
	@echo "  make lint       - Check code style"
	@echo "  make format     - Auto-format code"
	@echo "  make lint-fix   - Auto-fix linting issues"
	@echo "  make lint-all   - Format, fix, and lint"
	@echo "  make apigen     - Regenerate models from OpenAPI spec"
	@echo "  make clean      - Remove cache files"

setup: 
	python -m venv venv
	$(VENV_BIN)/pip install -r requirements.txt

run: check-venv
	$(MANAGE) process_order

test: check-venv
	$(MANAGE) test pos

apigen: check-venv
	$(VENV_BIN)/datamodel-codegen \
		--input ordersystem/pos/openapi.yaml \
		--output ordersystem/pos/models.py \
		--input-file-type openapi

lint: check-venv
	$(VENV_BIN)/ruff check ordersystem/

format: check-venv
	$(VENV_BIN)/ruff format ordersystem/

lint-fix: check-venv
	$(VENV_BIN)/ruff check --fix ordersystem/

lint-all: check-venv format lint-fix lint

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .ruff_cache .pytest_cache