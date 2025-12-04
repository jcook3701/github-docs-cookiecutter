# Github Docs Cookiecutter

__Author:__ Jared Cook  
__Version:__ 0.1.0  

## Overview
Template cookiecutter project for Github Pages (Jekyll).  

![black-format](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/black-format.yml/badge.svg)
![dependency-check](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/dependency-check.yml/badge.svg)
![jinja2-lint](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/jinja2-lint.yml/badge.svg)
![ruff-lint](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/ruff-lint.yml/badge.svg)
![security-audit](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/security-audit.yml/badge.svg)
![spellcheck](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/spellcheck.yml/badge.svg)
![tests](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/tests.yml/badge.svg)
![typecheck](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/typecheck.yml/badge.svg)
![yaml-lint](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/yaml-lint.yml/badge.svg)

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

***

## Development Strategy
__Note:__ All Makefile commands are used in ci/cd to ensure that if they pass locally they should also pass once pushed to github.  
### 🐍️ Build environment (.venv)
``` shell
$ make install
```
### 🔍 Linting (ruff & yaml-lint)
``` shell
$ make lint-check
```
``` shell
$ make lint-fix
```
### 🎨 Formatting (black)
```shell
$ make format-check
```
```shell
$ make format-fix
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

## Commit Help:
__Note:__ Commits are required to be conventional git commit message.
__example:__
```shell
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```
* ```<type>```: A required noun that describes the nature of the change.  
* ```[optional scope]```: An optional phrase within parentheses that specifies the part of the codebase being affected (e.g., fix(parser):).  
* ```<description>```: A required short, imperative-mood summary of the changes.  
* ```[optional body]```: A longer description providing additional context and "what and why" details.  
* ```[optional footer(s)]```: Used for adding meta-information, such as issue references (Fixes #123) or indicating breaking changes.  

***

### Authors Notes:  
1. This code currently works with cookiecutter 1.7 from Ubuntu's apt repositories.  

<!--

### TODO's
1. ~~[markdown](https://github.com/jackdewinter/pymarkdown) linter.~~  
      * ~~[docs](https://pymarkdown.readthedocs.io/en/latest/getting-started/)~~  
2. [djlint](https://djlint.com/)  
      * Swap jinja2 for djlint...


-->
