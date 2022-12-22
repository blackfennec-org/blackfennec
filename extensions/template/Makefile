.PHONY: test

install:
	pip install -e .

flatpak:
	flatpak-builder --user --install .flatpak-build/ org.blackfennec.app.extensions.template.yml --force-clean --repo=.flatpak-repo

test: