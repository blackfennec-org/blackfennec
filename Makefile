EXTS = $(shell find extensions/ -maxdepth 1 -mindepth 1 -type d | tac)
BLPS = $(shell find . -name "*.blp")
UIS = $(BLPS:.blp=.ui)

.PHONY: docs test

help:
	cat Makefile

flatpak:
	flatpak --user remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
	flatpak-builder --user --install .flatpak-build/ org.blackfennec.app.yml --force-clean --install-deps-from flathub --repo=.flatpak-repo

flatpak_run: flatpak
	flatpak run org.blackfennec.app

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

test_all: test $(EXTS)

test:
	pytest tests/;

.PHONY: $(EXTS)
$(EXTS):
	cd "$@"; \
	xvfb-run -a pytest tests/;

install: install_extensions
	python -m pip install -e .

install_extensions:
	rm ~/.config/blackfennec/extensions.json || true
	python -m pip install -e $(EXTS)

run: compile-blueprint install
	python blackfennec.py
