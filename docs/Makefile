# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
VERSIONDIR    = _versions
MODE          ?= html

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Build all tags of this repository.
versions:
	# Check if we have no dirty files
	if [ ! -z "$$(git status --porcelain)" ]; then \
	  echo "Error: There are changes in the working tree!" >&2; \
	  exit 1; \
	fi
	# Loop through all tags (except if current build) and execute versioned build for every one of them.
	CUR_DESCRIBE="$$(git describe --tags)"; \
	CUR_BRANCH="$$(git rev-parse --abbrev-ref HEAD)"; \
	for tag in $$(git tag); do \
	  git checkout "$$tag" || \
		(echo "Error: Could not checkout $$tag" >&2; exit 2); \
	  $(SPHINXBUILD) -M $(MODE) "$(SOURCEDIR)" "$(VERSIONDIR)/$$tag" -A is_version_build=True $(SPHINXOPTS) $(0); \
	done; \
	git checkout "$$CUR_BRANCH"

.PHONY: help versions Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)