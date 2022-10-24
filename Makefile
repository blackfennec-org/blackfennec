EXTS = $(shell find extensions/ -type d -maxdepth 1 -mindepth 1)
BLPS = $(shell find . -name "*.blp")
UIS = $(BLPS:.blp=.ui)

.PHONY: docs test

help:
	cat Makefile

install:
	flatpak --user remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
	flatpak-builder --user --install .flatpak-build/ org.blackfennec.app.yml --force-clean --install-deps-from flathub --repo=.flatpak-repo

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

test: test_blackfennec test_extensions

test_blackfennec:
	pytest tests/

test_extensions:
	for ext in $(EXTS); do \
		cd "$$ext"; \
		pytest tests/; \
	done


run: compile-blueprint
	python black_fennec.py
