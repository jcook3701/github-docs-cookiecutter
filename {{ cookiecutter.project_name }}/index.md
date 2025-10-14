---
layout: default
title: {{ cookiecutter.project_name }}
nav_order: 1
description: {{ cookiecutter.description }}
---
{% if false %}
	{% include "image-carousel.html" %}
{% endif %}

{% raw %}
	{% include_relative "README.md" %}
{% endraw %}

# ☕ Support Me
If you enjoy this project, consider buying me a coffee or making code contributions.  

{% raw %}
	{% include social-bar.html %}
{% endraw %}
