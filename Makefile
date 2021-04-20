
.PHONY: docs

docs:
	sphinx-apidoc -f -o docs/source/documentation/code/ .
	cd docs/; make html

lint:
	find . -name "*.py" | xargs pylint --output-format=text || true
