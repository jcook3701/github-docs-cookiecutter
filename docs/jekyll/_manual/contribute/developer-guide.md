---
layout: default
title: Developer Guide
nav_order: 1
parent: Contribute
---

## Developer guide

This guide helps you get started developing github-docs-cookiecutter.

## Development Strategy

All Makefile commands are used in __ci/cd__ to ensure that if they pass locally they should also pass once pushed to github.  

### 🐍️ Build environment (.venv)

``` shell
$ make install
```

### 🧬 Dependency Management (deptry)

```shell
$ make dependency-check
```

### 🛡️ Security Audit (pip-audit)

```shell
$ make security
```

### 🎨 Formatting (black)

```shell
$ make format-check
```

```shell
$ make format-fix
```

### 🔍 Linting (jinja2-cli, ruff, tomllint, & yaml-lint)

``` shell
$ make lint-check
```

``` shell
$ make lint-fix
```

### 🎓 Spellchecking (codespell)

```shell
$ make spellcheck
```

### 🧠 Typechecking (mypy)

``` shell
$ make typecheck
```

### 🧪 Testing (pytest)

``` shell
$ make test
```

### 🚀 Release (git tag)

```shell
$ make release
```

### ❓ Build Help

``` shell
$ make help
```
