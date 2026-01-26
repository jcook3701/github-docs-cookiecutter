---
layout: default
title: Contribute
nav_order: 2
parent: "Developer Resources"
---
## Contribute to {{ cookiecutter.project_name }}

This page lists resources for developers who want to contribute to the {{ cookiecutter.project_name }} ecosystem.

## Make technical contributions

### Contribute code to {{ cookiecutter.project_name }}

* [Contributing to {{ cookiecutter.project_name }}]()
* [Developer guide]({% raw %}{% link _manual/contribute/developer-guide.md %}{% endraw %})
* [Create a pull request] walks you through preparing a clear, descriptive pull request.
* Browse all [issues]({{ cookiecutter.repo_url }}/issues/new) to find a good first task. You can also filter by [help wanted]().

### Contribute without code

* Report a bug with the [bug report template]({{ cookiecutter.repo_url }}/issues/new?template=01-bug-report.yml) and include steps to reproduce.
* Submit a [feature request]({{ cookiecutter.repo_url }}/issues/new?template=02-feature-request.yml) to propose improvements.
* Report security vulnerabilities following our [security policy]({% raw %}{{ site.repo_blob }}/.github/SECURITY.md{% endraw %}).

### Best practices and style

Our [style guides]({% raw %}{% link _manual/contribute/style-guides/index.md %}{% endraw %}) outline {{ cookiecutter.project_name }} style for frontend, backend, documentation, and more, including best practices. Please read through them before you start editing or coding!
    * [Python style guide]({% raw %}{% link _manual/contribute/style-guides/python.md %}{% endraw %}).
    * [Typescript style guide]({% raw %}{% link _manual/contribute/style-guides/typescript.md %}{% endraw %}).
    * [YAML style guide]({% raw %}{% link _manual/contribute/style-guides/yaml.md %}{% endraw %}).
