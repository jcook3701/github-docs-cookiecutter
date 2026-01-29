# {{ site.title }}

__Author:__ {{ site.author }}  
__Version:__ {{ site.version }}  

## Overview
{{ site.description }}  

Template cookiecutter project for Github Pages (Jekyll).  This project can utilize a variety of different documentation templates but is focused mainly on a clean implementation of [just the docs](https://github.com/just-the-docs/just-the-docs). Skip the boring boilerplate code and get to the work that matters.

***

[![License](https://img.shields.io/github/license/jcook3701/github-docs-cookiecutter)](LICENSE)

<!-- [![CLA assistant](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/cla.yml/badge.svg)]() -->
![dependency-check](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/dependency-check.yml/badge.svg)
![format-check](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/format-check.yml/badge.svg)
![lint-check](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/lint-check.yml/badge.svg)
![security-audit](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/security-audit.yml/badge.svg)
![spellcheck](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/spellcheck.yml/badge.svg)
![tests](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/tests.yml/badge.svg)
![typecheck](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/typecheck.yml/badge.svg)

***

## Usage Examples:
__Example:__ Pull from main branch.  
1. Pull Project with cookiecutter command:  
``` shell
$ cookiecutter git@github.com:jcook3701/github-docs-cookiecutter.git  
```
__Example:__ Pull from develop branch.  
1. Pull code from development branch while testing updates.  
``` shell
$ cookiecutter git@github.com:jcook3701/github-docs-cookiecutter.git --checkout develop  
```

## Advance Examples:
__Note:__ The real intention of this project is to call it as a hook within other cookiecutter projects as shown below.  
__Explanation:__ [ansible-galaxy-cookiecutter](https://github.com/jcook3701/ansible-galaxy-cookiecutter) template utilizes [nutri-matic](https://github.com/jcook3701/nutri-matic) hooks to pull both this documentation template along with [sphinx-cookiecutter](https://github.com/jcook3701/sphinx-cookiecutter) template into generated project ```$(PROJECT_ROOT)/docs/```.  

Utilization of [nutri-matic](https://github.com/jcook3701/nutri-matic) is the optimal way of integrating this template in projects.  

***

## Development Strategy:
__Note:__ All Makefile commands are used in ci/cd to ensure that if they pass locally they should also pass once pushed to github.  
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

***

### Authors Notes:  
1. This code currently works with cookiecutter 1.7 from Ubuntu's apt repositories.  
