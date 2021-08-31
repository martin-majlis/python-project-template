OPEN=xdg-open

PROJECT_DIR=proj
TEST_DIR=tests

checks: mypy test

mypy:
	mypy $(PROJECT_DIR) $(TEST_DIR)

test: test-ci

test-ci:
	pytest --cov=$(PROJECT_DIR) -v

coverage:
	coverage html -d coverage_html
	$(OPEN) coverage_html/index.html

test-and-coverage: test coverage

pre-commit-all:
	pre-commit run -a -v

pre-commit-install:
	pre-commit install

install-all: dep-install pre-commit-install

dep-install: dep-install-run dep-install-dev

dep-install-run:
	pip install -r requirements.txt

dep-install-dev:
	pip install -r requirements-dev.txt
