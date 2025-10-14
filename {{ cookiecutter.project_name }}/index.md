---
layout: default
title: {{ cookiecutter.project_name }}
nav_order: 1
description: {{ cookiecutter.description }}
---
{% if site.carousel_images %}
	{% include image-carousel.html %}
{% endif %}

{% include README.md %}

# ☕ Support Me
If you enjoy this project, consider buying me a coffee or making code contributions.  

{% include social-bar.html %}
