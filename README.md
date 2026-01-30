<!--
  Auto-generated file. Do not edit directly.
  Edit /home/jcook/Documents/git_repo/github-doc-cookiecutter/docs/jekyll/README.md instead.
  Run ```make readme``` to regenerate this file
-->
<h1 id="github-docs-cookiecutter">github-docs-cookiecutter</h1>

<p><a href="LICENSE.md"><img src="https://img.shields.io/github/license/jcook3701/github-docs-cookiecutter" alt="License" /></a></p>

<p><strong>Author:</strong> Jared Cook<br />
<strong>Version:</strong> 0.1.1</p>

<h2 id="overview">Overview</h2>
<p>Github docs cookiecutter template generation.</p>

<p>Template cookiecutter project for Github Pages (Jekyll).  This project can utilize a variety of different documentation templates but is focused mainly on a clean implementation of <a href="https://github.com/just-the-docs/just-the-docs">just the docs</a>. Skip the boring boilerplate code and get to the work that matters.</p>

<hr />

<p><strong>CI/CD Check List:</strong></p>

<!-- [![CLA assistant](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/cla.yml/badge.svg)]() -->
<p><img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/dependency-check.yml/badge.svg" alt="dependency-check" />
<img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/format-check.yml/badge.svg" alt="format-check" />
<img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/lint-check.yml/badge.svg" alt="lint-check" />
<img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/security-audit.yml/badge.svg" alt="security-audit" />
<img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/spellcheck.yml/badge.svg" alt="spellcheck" />
<img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/tests.yml/badge.svg" alt="tests" />
<img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/typecheck.yml/badge.svg" alt="typecheck" /></p>

<hr />

<h2 id="usage-examples">Usage Examples</h2>

<p><strong>Example:</strong> Pull from main branch.</p>
<ol>
  <li>Pull Project with cookiecutter command:
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cookiecutter git@github.com:jcook3701/github-docs-cookiecutter.git  
</code></pre></div>    </div>
    <p><strong>Example:</strong> Pull from develop branch.</p>
  </li>
  <li>Pull code from development branch while testing updates.
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cookiecutter git@github.com:jcook3701/github-docs-cookiecutter.git <span class="nt">--checkout</span> develop  
</code></pre></div>    </div>
  </li>
</ol>

<h2 id="advance-examples">Advance Examples</h2>

<p><strong>Note:</strong> The real intention of this project is to call it as a hook within other cookiecutter projects as shown below.<br />
<strong>Explanation:</strong> <a href="https://github.com/jcook3701/ansible-galaxy-cookiecutter">ansible-galaxy-cookiecutter</a> template utilizes <a href="https://github.com/jcook3701/nutri-matic">nutri-matic</a> hooks to pull both this documentation template along with <a href="https://github.com/jcook3701/sphinx-cookiecutter">sphinx-cookiecutter</a> template into generated project <code class="language-plaintext highlighter-rouge">$(PROJECT_ROOT)/docs/</code>.</p>

<p>Utilization of <a href="https://github.com/jcook3701/nutri-matic">nutri-matic</a> is the optimal way of integrating this template in projects.</p>

<hr />

<h2 id="getting-started">Getting Started</h2>

<ul>
  <li><a href="https://jcook3701.github.io/github-docs-cookiecutter/manual/setup-guide/requirements">Requirements</a></li>
  <li><a href="https://jcook3701.github.io/github-docs-cookiecutter/manual/introduction/installation-guide">Installation guide</a></li>
</ul>

<h2 id="documentation">Documentation</h2>

<p>The github-docs-cookiecutter documentation is available at <a href="https://jcook3701.github.io/github-docs-cookiecutter">docs</a>.</p>

<h2 id="contributing">Contributing</h2>

<p>If you’re interested in contributing to the github-docs-cookiecutter project:</p>
<ul>
  <li>Start by reading the <a href="https://jcook3701.github.io/github-docs-cookiecutter/manual/developer-resources/contribute">contributing guide</a>.</li>
  <li>Learn how to setup your local environment, in our <a href="https://jcook3701.github.io/github-docs-cookiecutter/manual/contribute/developer-guide">developer guide</a>.</li>
  <li>Look through our <a href="https://jcook3701.github.io/github-docs-cookiecutter/manual/contribute/style-guides/index">style guide</a>.</li>
</ul>

<hr />

<h2 id="authors-notes">Authors Notes</h2>

<ol>
  <li>This code currently works with cookiecutter (2.6) from PyPi repositories.</li>
</ol>

<h2 id="license">License</h2>

<p>Copyright (c) 2025-2026, Jared Cook</p>

<p>This project is licensed under the <strong>AGPL-3.0-or-later License</strong>.
See the <a href="https://github.com/jcook3701/github-docs-cookiecutter/blob/master/LICENSE.md">LICENSE</a> file for the full license text.</p>

<p>SPDX-License-Identifier: AGPL-3.0-or-later</p>
