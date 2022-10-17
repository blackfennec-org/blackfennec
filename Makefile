BLPS = $(shell find . -name "*.blp")
UIS = $(BLPS:.blp=.ui)

.PHONY: docs test

dependencies:
	python -m pip install -r requirements.txt
	python -m pip install -r docs/requirements.txt

docs:
	sphinx-apidoc -f -o docs/source/software_documentation/code/ .
	cd docs/; make html

compile-blueprint: $(UIS)
%.ui: %.blp
	blueprint-compiler compile "$<" --output "$@"

lint:
	find . -name "*.py" | xargs pylint --output-format=text || true

test:
	python -m pytest \
		--cov-config=.coveragerc \
		--cov=src \
		--cov-report=xml:cov.xml \
		--cov-report=term-missing \
		tests

run: compile-blueprint
	python black_fennec.py
