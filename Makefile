EXTS = $(shell find extensions/ -maxdepth 1 -mindepth 1 -type d | tac)
EXTS_FLATPAK = $(addsuffix .flatpak, $(EXTS))
EXTS_TEST = $(addsuffix .test, $(EXTS))
BLPS = $(shell find . -name "*.blp")
UIS = $(BLPS:.blp=.ui)

.PHONY: docs test

help:
	cat Makefile

flatpak_remoate_flathub:
	flatpak --user remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

install_flatpak: compile-blueprint flatpak_remoate_flathub
	flatpak-builder --user --install .flatpak-build/ org.blackfennec.app.yml --force-clean --install-deps-from flathub --repo=.flatpak-repo

install_flatpak_extensions: compile-blueprint $(EXTS_FLATPAK)

%.flatpak:
	# remove the trailing .flatpak
	$(eval EXT := $(subst .flatpak,,$@))
	cd "$(EXT)" && make flatpak

run_flatpak:
	flatpak run org.blackfennec.app

docs:
	sphinx-apidoc -f -q -o docs/source/development/code/ . setup.py
	cd docs/; make html

compile-blueprint: $(UIS)
%.ui: %.blp
	blueprint-compiler compile "$<" --output "$@"

lint:
	find . -name "*.py" | xargs pylint --output-format=text || true

test_all: test test_extensions

test:
	pytest tests/;

test_extensions: $(EXTS_TEST)

%.test:
	# remove the trailing .test
	$(eval EXT := $(subst .test,,$@))
	cd "$(EXT)" && make test

install_all: isntall install_extensions

install:
	python -m pip install -e .

install_extensions: $(EXTS_PIP)

%.pip:
	# remove the trailing .pip
	$(eval EXT := $(subst .pip,,$@))
	cd "$(EXT)" && make install

run: compile-blueprint install
	python blackfennec.py
