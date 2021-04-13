
.PHONY: docs

docs:
	sphinx-apidoc -f -o docs/source/documentation/code/ .
	cd docs/; make html