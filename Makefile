VENV_DIR := $(shell poetry env info -p)

default: install

install: # Install dependencies
	poetry install

format: # Format code with black and yapf
	poetry run black src/ tests/
	poetry run yapf -i -r --style pep8 src/ tests/

test: # Run tests with pytest
	poetry run pytest

build: # Build the package
	poetry build

publish: build # Publish the package to PyPI
	poetry publish

clean: # Clean distribution files and Python bytecode
	rm -rf dist/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete

clean-all: clean # Clean all generated files including the virtual environment
	rm -rf $(VENV_DIR)
	poetry cache clear --all pypi

help: # Display this help message
	@printf "Usage: make \033[1;34m[target]\033[0m\n\nTargets:\n"
	@awk 'BEGIN {FS = ":.*#"} /^[a-zA-Z_-]+:.*?#/ { printf "  \033[1;34m%-15s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: install format test build publish clean clean-all help
