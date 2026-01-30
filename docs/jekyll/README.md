# {{ site.title }}

[![License](https://img.shields.io/github/license/{{ site.github_username }}{{ site.baseurl }})](LICENSE.md)

**Author:** {{ site.author }}  
**Version:** {{ site.version }}  

## Overview
{{ site.description }}  

Template cookiecutter project for Github Pages (Jekyll).  This project can utilize a variety of different documentation templates but is focused mainly on a clean implementation of [just the docs](https://github.com/just-the-docs/just-the-docs). Skip the boring boilerplate code and get to the work that matters.

***

**CI/CD Check List:**

<!-- [![CLA assistant](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/cla.yml/badge.svg)]() -->
![dependency-check](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/dependency-check.yml/badge.svg)
![format-check](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/format-check.yml/badge.svg)
![lint-check](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/lint-check.yml/badge.svg)
![security-audit](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/security-audit.yml/badge.svg)
![spellcheck](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/spellcheck.yml/badge.svg)
![tests](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/tests.yml/badge.svg)
![typecheck](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/typecheck.yml/badge.svg)

***

## Usage Examples

**Example:** Pull from main branch.  
1. Pull Project with cookiecutter command:  
``` shell
$ cookiecutter git@github.com:jcook3701/github-docs-cookiecutter.git  
```
**Example:** Pull from develop branch.  
1. Pull code from development branch while testing updates.  
``` shell
$ cookiecutter git@github.com:jcook3701/github-docs-cookiecutter.git --checkout develop  
```

## Advance Examples

**Note:** The real intention of this project is to call it as a hook within other cookiecutter projects as shown below.  
**Explanation:** [ansible-galaxy-cookiecutter](https://github.com/jcook3701/ansible-galaxy-cookiecutter) template utilizes [nutri-matic](https://github.com/jcook3701/nutri-matic) hooks to pull both this documentation template along with [sphinx-cookiecutter](https://github.com/jcook3701/sphinx-cookiecutter) template into generated project ```$(PROJECT_ROOT)/docs/```.  

Utilization of [nutri-matic](https://github.com/jcook3701/nutri-matic) is the optimal way of integrating this template in projects.  

***

## Getting Started

* [Requirements]({{ site.github_io_url }}/manual/setup-guide/requirements)
* [Installation guide]({{ site.github_io_url }}/manual/introduction/installation-guide)  

## Documentation

The {{ site.title }} documentation is available at [docs]({{ site.github_io_url }}).  

## Contributing

If you're interested in contributing to the {{ site.title }} project:  
* Start by reading the [contributing guide]({{ site.github_io_url }}/manual/developer-resources/contribute).  
* Learn how to setup your local environment, in our [developer guide]({{ site.github_io_url }}/manual/contribute/developer-guide).  
* Look through our [style guide]({{ site.github_io_url }}/manual/contribute/style-guides/index).  

***

## Authors Notes

1. This code currently works with cookiecutter (2.6) from PyPi repositories.  

## License

{{ site.copyright }}  

This project is licensed under the **{{ site.license }} License**.  
See the [LICENSE]({{ site.repo_blob }}/LICENSE.md) file for the full license text.  

SPDX-License-Identifier: {{ site.license }}  
