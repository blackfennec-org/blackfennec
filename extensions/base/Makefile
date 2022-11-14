.PHONY: test

help:
	cat Makefile

flatpak:
	flatpak --user remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
	flatpak-builder --user --install .flatpak-build/ org.blackfennec.extensions.base.yml --force-clean --install-deps-from flathub --repo=.flatpak-repo

lint:
	find . -name "*.py" | xargs pylint --output-format=text || true

test:
	pytest tests/;

install:
	python -m pip install -e .
