
.PHONY: docs test

help:
	cat Makefile

dependencies:
	python -m pip install -r requriements.txt
	pythom -m pip install -r docs/requriements.txt

docs:
	sphinx-apidoc -f -o docs/source/software_documentation/code/ .
	cd docs/; make html

lint:
	find . -name "*.py" | xargs pylint --output-format=text || true

test:
	python -m pytest \
		--cov-config=.coveragerc \
		--cov=src \
		--cov-report=xml:cov.xml \
		--cov-report=term-missing \
		tests

run:
	python black_fennec.py
