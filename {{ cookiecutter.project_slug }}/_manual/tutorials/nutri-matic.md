---
layout: default
title: Create Virtual Environment
nav_order: 1
parent: Tutorials
---
## Nutri-Matic Setup

First clone the nutri-matic python utility.  This is needed to clone all jcook3701's, cookiecutter templates, with ```cookiecutter``` command.
```shell
$ git clone git@github.com:jcook3701/nutri-matic.git
```

Next, create a [virtual environment]({% raw %}{% link _manual/tutorials/create-virtual-env.md %}{% endraw %}) to store nutri-matic install. This is need to avoid installing packages directly to the system python instance.  

Finally, install [Nutri-Matic](https://github.com/jcook3701/nutri-matic) from [pypi](https://pypi.org/project/nutri-matic/) repository.  

```shell
$ python -m pip install nutri-matic
```
