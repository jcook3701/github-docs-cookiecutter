# Makefile
# =========================================
# Project: github-docs-cookiecutter
# =========================================

# --------------------------------------------------
# ⚙️ Environment Settings
# --------------------------------------------------
SHELL := /bin/bash
.SHELLFLAGS := -O globstar -c

# If V is set to '1' or 'y' on the command line,
# AT will be empty (verbose).  Otherwise, AT will
# contain '@' (quiet by default).  The '?' is a
# conditional assignment operator: it only sets V
# if it hasn't been set externally.
V ?= 0
ifeq ($(V),0)
    AT = @
else
    AT =
endif

# Detect if we are running inside GitHub Actions CI.
# GitHub sets the environment variable GITHUB_ACTIONS=true in workflows.
# We set CI=1 if running in GitHub Actions, otherwise CI=0 for local runs.
ifeq ($(GITHUB_ACTIONS),true)
CI := 1
else
CI := 0
endif
# --------------------------------------------------
# ⚙️ Build Settings
# --------------------------------------------------
PACKAGE_NAME := "github-docs-cookiecutter"
AUTHOR := "Jared Cook"
VERSION := "0.1.1"
RELEASE := v$(VERSION)
# --------------------------------------------------
# 🐙 Github Build Settings
# --------------------------------------------------
GITHUB_USER := "jcook3701"
GITHUB_REPO := $(GITHUB_USER)/$(PACKAGE_NAME)
# --------------------------------------------------
# 📁 Build Directories
# --------------------------------------------------
PROJECT_ROOT := $(PWD)
COOKIE_DIR := $(PROJECT_ROOT)/{{ cookiecutter.project_name }}
HOOKS_DIR := $(PROJECT_ROOT)/hooks
SRC_DIR := $(HOOKS_DIR)
TESTS_DIR := $(PROJECT_ROOT)/tests
DOCS_DIR := $(PROJECT_ROOT)/docs
SPHINX_DIR := $(DOCS_DIR)/sphinx
JEKYLL_DIR := $(DOCS_DIR)/jekyll
JEKYLL_SPHINX_DIR := $(JEKYLL_DIR)/sphinx
CHANGELOG_DIR := $(PROJECT_ROOT)/changelogs
CHANGELOG_RELEASE_DIR := $(CHANGELOG_DIR)/releases
# --------------------------------------------------
# 📄 Build Files
# --------------------------------------------------
README_FILE := $(PROJECT_ROOT)/README.md
CHANGELOG_FILE := $(CHANGELOG_DIR)/CHANGELOG.md
# --------------------------------------------------
# 🐍 Python / Virtual Environment
# --------------------------------------------------
PYTHON_CMD := python3.11
VENV_DIR := .venv
# --------------------------------------------------
# 🐍 Python Dependencies
# --------------------------------------------------
DEPS := .
DEV_DEPS := .[dev]
DEV_DOCS := .[docs]
# --------------------------------------------------
# 🐍 Python Commands (venv, activate, pip)
# --------------------------------------------------
CREATE_VENV := $(PYTHON_CMD) -m venv $(VENV_DIR)
ACTIVATE := source $(VENV_DIR)/bin/activate
PYTHON := $(ACTIVATE) && $(PYTHON_CMD)
PIP := $(PYTHON) -m pip
# --------------------------------------------------
# 🧬 Dependency Management (deptry)
# --------------------------------------------------
DEPTRY := $(ACTIVATE) && deptry
# --------------------------------------------------
# 🛡️ Security Audit (pip-audit)
# --------------------------------------------------
PIPAUDIT :=	$(ACTIVATE) && pip-audit
# --------------------------------------------------
# 🎨 Formatting (black)
# --------------------------------------------------
BLACK := $(PYTHON) -m black
# --------------------------------------------------
# 🔍 Linting (ruff, toml, yaml, jinja2)
# --------------------------------------------------
RUFF := $(PYTHON) -m ruff
# NOTE: NOT AN ERROR!
TOMLLINT := tomllint
YAMLLINT := $(PYTHON) -m yamllint
JINJA := $(ACTIVATE) && jinja2 --strict
DJLINT := $(PYTHON) -m djlint
# --------------------------------------------------
# 🎓 Spellchecker (codespell)
# --------------------------------------------------
CODESPELL := $(ACTIVATE) && codespell
# --------------------------------------------------
# 🧠 Typing (mypy)
# --------------------------------------------------
MYPY := $(PYTHON) -m mypy
# --------------------------------------------------
# 🧪 Testing (pytest)
# --------------------------------------------------
PYTEST := $(PYTHON) -m pytest
# --------------------------------------------------
# 📚 Documentation (Sphinx + Jekyll)
# --------------------------------------------------
SPHINX := $(PYTHON) -m sphinx -b markdown
JEKYLL_BUILD := bundle exec jekyll build --quiet
JEKYLL_CLEAN := bundle exec jekyll clean
JEKYLL_SERVE := bundle exec jekyll serve
# --------------------------------------------------
# 🔖 Version Bumping (bumpy-my-version)
# --------------------------------------------------
BUMPVERSION := $(ACTIVATE) && bump-my-version bump --verbose
# Patch types:
MAJOR := major
MINOR := minor
PATCH := patch
# --------------------------------------------------
# 📜 Changelog generation (git-clif)
# --------------------------------------------------
GITCLIFF := git cliff
# --------------------------------------------------
# 🐙 Github Tools (git)
# --------------------------------------------------
GIT := git
# --------------------------------------------------
# 🚨 Pre-Commit (pre-commit)
# --------------------------------------------------
PRECOMMIT := $(ACTIVATE) && pre-commit
# --------------------------------------------------
# 🏃‍♂️ Nutri-Matic command
# --------------------------------------------------
NUTRIMATIC := $(PYTHON) -m nutrimatic
# --------------------------------------------------
# 🏗️ CI/CD Functions
# --------------------------------------------------
# Define a reusable CI-safe runner
define run_ci_safe =
( $1 || [ "$(CI)" != "1" ] )
endef

# Command to get the most recent previous version tag
# 'git describe --tags --abbrev=0' gets the latest tag, so we use HEAD~1 to get the one before that
# Use 'git describe --tags --abbrev=0' to get the latest tag for the current version
define get_version
$(shell $(GIT) describe --tags --abbrev=0 2> /dev/null || echo $(RELEASE))
endef

define get_previous_version
$(shell $(GIT) describe --tags --abbrev=0 HEAD~1 2> /dev/null || echo None)
endef
# Variables to store the versions
CURRENT_VERSION := $(call get_version)
PREVIOUS_VERSION := $(call get_previous_version)

define git_cliff_release_tag
$(if $(filter-out None,$(PREVIOUS_VERSION)),\
    $(GITCLIFF) $(PREPREVIOUS_VERSION)..$(CURRENT_VERSION) --tag $(CURRENT_VERSION), \
    $(GITCLIFF) --unreleased --tag $(CURRENT_VERSION) \
)
endef

CHANGELOG_RELEASE_FILE := $(CHANGELOG_RELEASE_DIR)/$(CURRENT_VERSION).md
GITCLIFF_RELEASE := $(call git_cliff_release_tag) --output $(CHANGELOG_RELEASE_FILE)
# --------------------------------------------------
.PHONY: all list-folders venv install ruff-lint-check ruff-lint-fix yaml-lint-check \
	jinja2-lint-check lint-check typecheck test build-docs jekyll-serve clean help
# --------------------------------------------------
# Default: run lint, typecheck, tests, and docs
# --------------------------------------------------
all: install lint-check typecheck spellcheck test build-docs
# --------------------------------------------------
# Make Internal Utilities
# --------------------------------------------------
list-folders:
	$(AT)printf "\
	🐍 src: $(SRC_DIR)\n\
	🧪 Test: $(TESTS_DIR)\n"
# --------------------------------------------------
# 🐍 Virtual Environment Setup
# --------------------------------------------------
venv:
	$(AT)echo "🐍 Creating virtual environment..."
	$(AT)$(CREATE_VENV)
	$(AT)echo "✅ Virtual environment created."

install: venv
	$(AT)echo "📦 Installing project dependencies..."
	$(AT)$(PIP) install --upgrade pip setuptools wheel
	# $(AT)$(PIP) install -e $(DEPS)
	$(AT)$(PIP) install -e $(DEV_DEPS)
	$(AT)$(PIP) install -e $(DEV_DOCS)
	$(AT)echo "✅ Dependencies installed."
# --------------------------------------------------
# 🚨 Pre-Commit (pre-commit)
# --------------------------------------------------
pre-commit-init:
	$(AT)echo "📦 Installing pre-commit hooks and hook-types..."
	$(AT)which $(GIT) >/dev/null || { $(AT)echo "Git is required"; exit 1; }
	$(AT)$(PRECOMMIT) install --install-hooks
	$(AT)$(PRECOMMIT) install --hook-type pre-commit --hook-type commit-msg
	$(AT)echo "✅ pre-commit dependencies installed!"
# --------------------------------------------------
# 🛡️ Security (pip-audit)
# --------------------------------------------------
security:
	$(AT)echo "🛡️ Running security audit..."
	$(AT)$(call run_ci_safe, $(PIPAUDIT))
	$(AT)echo "✅ Finished security audit!"
# --------------------------------------------------
# 🧬 Dependency Management (deptry)
# --------------------------------------------------
dependency-check:
	$(AT)echo "🧬 Checking dependency issues..."
	$(AT)$(DEPTRY) --pep621-dev-dependency-groups dev,docs \
		 $(SRC_DIR)
	$(AT)echo "✅ Finished checking for dependency issues!"
# --------------------------------------------------
# 🎨 Formatting (black)
# --------------------------------------------------
black-formatter-check:
	$(AT)echo "🔍 Running black formatter style check..."
	$(AT)$(call run_ci_safe, $(BLACK) --check $(SRC_DIR) $(TESTS_DIR))
	$(AT)echo "✅ Finished formatting check of Python code with Black!"

black-formatter-fix:
	$(AT)echo "🎨 Running black formatter fixes..."
	$(AT)$(BLACK) $(SRC_DIR) $(TESTS_DIR)
	$(AT)echo "✅ Finished formatting Python code with Black!"

format-check: black-formatter-check
format-fix: black-formatter-fix
# --------------------------------------------------
# 🔍 Linting (jinja2, ruff, toml, yaml)
# --------------------------------------------------
# TODO: Should use this eventually to replace jinja2-lint-check (github-workspace, lint-check)
# TODO: Look into djlint autofixes and update the pyproject.toml to include djlint.
djlint-check:
	$(AT)echo "🔍 Running DJLint..."
	$(AT)echo "$(DJLINT)"
	$(AT)echo "✅ Finished linting with DJLint!"

jinja2-lint-check:
	$(AT)echo "🔍 jinja2 linting all template files under $(COOKIE_DIR)..."
	$(AT)jq '{cookiecutter: .}' cookiecutter.json > /tmp/_cc_wrapped.json
	$(AT)find '$(COOKIE_DIR)' -type f \
		! -path "$(COOKIE_DIR)/.github/workflows/*" \
		! -name "*.md" \
		! -name "*.html" \
		! -name "*.png" \
		! -name "*.jpg" \
		! -name "*.ico" \
		! -name "*.gif" \
		-print0 | while IFS= read -r -d '' f; do \
			if file "$$f" | grep -q text; then \
				echo "Checking $$f"; \
				$(JINJA) "$$f" /tmp/_cc_wrapped.json || exit 1; \
			fi; \
		done
	$(AT)echo "✅ Finished linting check of jinja2 files with jinja2!"

ruff-lint-check: list-folders
	$(AT)echo "🔍 Running ruff linting..."
	$(AT)$(call run_ci_safe, $(RUFF) check $(SRC_DIR) $(TESTS_DIR))
	$(AT)echo "✅ Finished linting check of Python code with Ruff!"

ruff-lint-fix:
	$(AT)echo "🎨 Running ruff lint fixes..."
	$(AT)$(RUFF) check --show-files $(SRC_DIR) $(TESTS_DIR)
	$(AT)$(RUFF) check --fix $(SRC_DIR) $(TESTS_DIR)
	$(AT)echo "✅ Finished linting Python code with Ruff!"

toml-lint-check:
	$(AT)echo "🔍 Running Tomllint..."
	$(AT)$(ACTIVATE) && \
		find $(PROJECT_ROOT) -name "*.toml" \
			! -path "$(VENV_DIR)/*" \
			! -path "*{{*" \
			! -path "*}}*" \
			-print0 | xargs -0 -n 1 $(TOMLLINT)
	$(AT)echo "✅ Finished linting check of toml configuration files with Tomllint!"

yaml-lint-check:
	$(AT)echo "🔍 Running yamllint..."
	$(AT)$(call run_ci_safe, $(YAMLLINT) .)
	$(AT)echo "✅ Finished linting check of yaml files with yamllint!"

lint-check: jinja2-lint-check ruff-lint-check toml-lint-check yaml-lint-check
lint-fix: ruff-lint-fix
# --------------------------------------------------
# 🎓 Spellchecker (codespell)
# --------------------------------------------------
spellcheck:
	$(AT)echo "🎓 Checking Spelling (codespell)..."
	$(AT)$(CODESPELL) $(SRC_DIR) $(TESTS_DIR) $(DOCS_DIR)
	$(AT)echo "✅ Finished spellcheck!"
# --------------------------------------------------
# 🧠 Typechecking (MyPy)
# --------------------------------------------------
typecheck:
	$(AT)echo "🧠 Checking types (MyPy)..."
	$(AT)$(call run_ci_safe, $(MYPY) $(TESTS_DIR))
	$(AT)echo "✅ Python typecheck complete!"
# --------------------------------------------------
# 🧪 Testing (pytest)
# --------------------------------------------------
test:
	$(AT)echo "🧪 Running tests with pytest..."
	$(AT)$(call run_ci_safe,$(PYTEST) $(TESTS_DIR))
	$(AT)echo "✅ Python tests complete!"
# --------------------------------------------------
# 📚 Documentation (Sphinx + Jekyll)
# --------------------------------------------------
sphinx:
	$(AT)echo "🔨 Building Sphinx documentation 📘 as Markdown..."
	$(AT)$(SPHINX) $(SPHINX_DIR) $(JEKYLL_SPHINX_DIR)
	$(AT)echo "✅ Sphinx Markdown build complete!"

jekyll:
	$(AT)echo "🔨 Building Jekyll site..."
	$(AT)cd $(JEKYLL_DIR) && $(JEKYLL_BUILD)
	$(AT)echo "✅ Full documentation build complete!"

jekyll-serve: docs
	$(AT)echo "🚀 Starting Jekyll development server..."
	$(AT)cd $(JEKYLL_DIR) && $(JEKYLL_SERVE)

build-docs: sphinx jekyll
run-docs: jekyll-serve
# --------------------------------------------------
# 🔖 Version Bumping (bumpy-my-version)
# --------------------------------------------------
# TODO: Also create a git tag of current version.
bump-version-patch:
	$(AT)echo "🔖 Updating $(PACKAGE_NAME) version from $(VERSION)..."
	$(AT)$(BUMPVERSION) $(PATCH)
	$(AT)echo "✅ $(PACKAGE_NAME) version update complete!"
# --------------------------------------------------
# 📜 Changelog generation (git-cliff)
# --------------------------------------------------
# Note: Run as part of pre-commit.  No manual run needed.
changelog:
	$(AT)echo "📜 $(PACKAGE_NAME) Changelog Generation..."
	$(AT)$(GITCLIFF) \
	  --output $(CHANGELOG_FILE)
	$(AT)$(GITCLIFF_RELEASE)
	$(AT)$(GIT) add $(CHANGELOG_FILE)
	$(AT)$(GIT) add $(CHANGELOG_RELEASE_FILE)
	$(AT)echo "✅ Finished Changelog Update!"

changelog-test:
	$(AT)echo "current version: $(CURRENT_VERSION)"
	$(AT)echo "previous version: $(PREVIOUS_VERSION)"
	$(AT)echo $(GITCLIFF_RELEASE)
	$(AT)echo $(CHANGELOG_RELEASE_FILE)
# --------------------------------------------------
# 🐙 Github Commands (git)
# --------------------------------------------------
#NOTE: Not yet tested!!!
git-release:
	$(AT)echo "📦 $(PACKAGE_NAME) Release Tag - $(RELEASE)! 🎉"
	$(AT)$(GIT) tag -a $(RELEASE) -m "Release $(RELEASE)"
	$(AT)$(GIT) push origin $(RELEASE)
	$(AT)echo "✅ Finished uploading Release - $(RELEASE)!"
# --------------------------------------------------
# 📢 Release
# --------------------------------------------------
release: git-release bump-version-patch
# --------------------------------------------------
# 🧹 Clean artifacts
# --------------------------------------------------
clean:
	$(AT)echo "🧹 Clening build artifacts..."
	$(AT)rm -rf $(SPHINX_DIR)/_build $(JEKYLL_SPHINX_DIR)
	$(AT)$(call run_ci_safe,cd $(JEKYLL_DIR) && $(JEKYLL_CLEAN))
	$(AT)rm -rf build dist *.egg-info
	$(AT)find $(SRC_DIR) $(TESTS_DIR) -name "__pycache__" -type d -exec rm -rf {} +
	$(AT)-[ -d "$(VENV_DIR)" ] && rm -r $(VENV_DIR)
	$(AT)echo "🧹 Cleaned build artifacts."
# --------------------------------------------------
# Version
# --------------------------------------------------
version:
	$(AT)echo "$(PACKAGE_NAME)"
	$(AT)echo "author: $(AUTHOR)"
	$(AT)echo "version: $(RELEASE)"
# --------------------------------------------------
# ❓ Help
# --------------------------------------------------
help:
	$(AT)echo "📦 github-doc-cookiecutter Makefile"
	$(AT)echo ""
	$(AT)echo "Usage:"
	$(AT)echo "  make venv                   Create virtual environment."
	$(AT)echo "  make install                Install dependencies."
	$(AT)echo "  make security               Run security audit (pip-audit)."
	$(AT)echo "  make dependency-check       Run dependency check (deptry)."
	$(AT)echo "  make format-check           Run all project formatter checks (black)."
	$(AT)echo "  make format-fix             Run all project formatter autofixes (black)."
	$(AT)echo "  make jinja2-lint-check      Run jinja-cmd linter."
	$(AT)echo "  make ruff-lint-check        Run Ruff linter."
	$(AT)echo "  make ruff-lint-fix          Auto-fix lint issues with python ruff."
	$(AT)echo "  make toml-lint-check        Run toml linter (tomllint)."
	$(AT)echo "  make yaml-lint-check        Run YAML linter (yamllint)."
	$(AT)echo "  make lint-check             Run all project linters (ruff, yaml, & jinja2)."
	$(AT)echo "  make lint-fix               Run all project linter autofixes (ruff)."
	$(AT)echo "  make spellcheck             Run Spellchecker (codespell)."
	$(AT)echo "  make typecheck              Run Mypy type checking."
	$(AT)echo "  make test                   Run Pytest suite."
	$(AT)echo "  make build-docs             Build Sphinx + Jekyll documentation."
	$(AT)echo "  make run-docs               Serve Jekyll site locally."
	$(AT)echo "  make version                Displays project information."
	$(AT)echo "  make clean                  Clean build artifacts."
	$(AT)echo "  make all                    Run install, lint, typecheck, test, and docs."
	$(AT)echo "Options:"
	$(AT)echo "  V=1             Enable verbose output (show all commands being executed)"
	$(AT)echo "  make -s         Run completely silently (suppress make's own output AND command echo)"
