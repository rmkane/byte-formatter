VENV_DIR := .venv

default: install

.venv: # Create virtual environment
	poetry config virtualenvs.in-project true
	poetry env use python3

install: .venv # Install dependencies
	poetry install

format: # Format code with black and yapf
	poetry run black src/ tests/
	poetry run yapf -i -r --style pep8 src/ tests/

test: # Run tests with pytest
	poetry run pytest

build: # Build the package
	poetry build

publish: build # Publish the package to PyPI
	poetry publish --dry-run # Remove --dry-run to actually publish

clean: # Clean distribution files
	rm -rf dist/

clean-all: clean # Clean all generated files
	find . -type d -name __pycache__ -exec rm -rf {} +
	rm -rf $(VENV_DIR)
	poetry cache clear --all pypi

help: # Display this help message
	@printf "Usage: make \033[1;34m[target]\033[0m\n\nTargets:\n"
	@awk 'BEGIN {FS = ":.*#"} /^[a-zA-Z_-]+:.*?#/ { printf "  \033[1;34m%-15s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: .venv build clean clean-all format help install publish test
