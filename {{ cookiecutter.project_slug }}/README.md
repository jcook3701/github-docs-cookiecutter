# {{ site.title }}

[![License](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})](LICENSE.md)

__Author:__ {{ site.author }}  
__Version:__ {{ site.version }}  

## Overview
{{ site.description }}  

__CI/CD Check List:__
* ![dependency-check]({{ site.repo_url }}/actions/workflows/dependency-check.yml/badge.svg)
* ![format-check]({{ site.repo_url }}/actions/workflows/format-check.yml/badge.svg)
* ![lint-check]({{ site.repo_url }}/actions/workflows/lint-check.yml/badge.svg)
* ![security-audit]({{ site.repo_url }}/actions/workflows/security-audit.yml/badge.svg)
* ![spellcheck]({{ site.repo_url }}/actions/workflows/spellcheck.yml/badge.svg)
* ![tests]({{ site.repo_url }}/actions/workflows/tests.yml/badge.svg)
* ![typecheck]({{ site.repo_url }}/actions/workflows/typecheck.yml/badge.svg)

***

## Getting Started
* [Get {{ cookiecutter.project_name}}]
* [Installation guides]

## Documentation
The {{ cookiecutter.project_name }} documentation is available at [docs]({{ site.github_io_url }})

## Contributing
If you're interested in contributing to the {{ cookiecutter.project_name }} project:
* Start by reading the [contributing guide]({{ site.github_io_url }}/developer-resources/contribute.md).
* Learn how to setup your local environment, in our [developer guide]({{ site.github_io_url }}/contribute/developer-guide.md).
* Look through our [style guide]({{ site.github_io_url }}/contribute/style-guides/index.md).

## License
{{ cookiecutter.copyright }}

This project is licensed under the __{{ cookiecutter.license }} License__.
See the [LICENSE]({{ site.repo_blob }}/LICENSE.md) file for the full license text.

SPDX-License-Identifier: {{ cookiecutter.license }}
