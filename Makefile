
.PHONY: docs test

help:
	cat Makefile

install:
	flatpak --user remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
	flatpak-builder --user --install build-dir org.darwin.blackfennec.yml --force-clean --install-deps-from flathub

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
