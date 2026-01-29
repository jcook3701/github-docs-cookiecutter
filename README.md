<!--
  Auto-generated file. Do not edit directly.
  Edit /home/jcook/Documents/git_repo/github-doc-cookiecutter/docs/jekyll/README.md instead.
  Run ```make readme``` to regenerate this file
-->
<h1 id="github-docs-cookiecutter">github-docs-cookiecutter</h1>

<p><strong>Author:</strong> Jared Cook<br />
<strong>Version:</strong> 0.1.1</p>

<h2 id="overview">Overview</h2>
<p>Github docs cookiecutter template generation.</p>

<p>Template cookiecutter project for Github Pages (Jekyll).  This project can utilize a variety of different documentation templates but is focused mainly on a clean implementation of <a href="https://github.com/just-the-docs/just-the-docs">just the docs</a>. Skip the boring boilerplate code and get to the work that matters.</p>

<hr />

<p><a href="LICENSE"><img src="https://img.shields.io/github/license/jcook3701/github-docs-cookiecutter" alt="License" /></a></p>

<!-- [![CLA assistant](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/cla.yml/badge.svg)]() -->
<p><img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/dependency-check.yml/badge.svg" alt="dependency-check" />
<img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/format-check.yml/badge.svg" alt="format-check" />
<img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/lint-check.yml/badge.svg" alt="lint-check" />
<img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/security-audit.yml/badge.svg" alt="security-audit" />
<img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/spellcheck.yml/badge.svg" alt="spellcheck" />
<img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/tests.yml/badge.svg" alt="tests" />
<img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/typecheck.yml/badge.svg" alt="typecheck" /></p>

<hr />

<h2 id="usage-examples">Usage Examples:</h2>
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

<h2 id="advance-examples">Advance Examples:</h2>
<p><strong>Note:</strong> The real intention of this project is to call it as a hook within other cookiecutter projects as shown below.<br />
<strong>Explanation:</strong> <a href="https://github.com/jcook3701/ansible-galaxy-cookiecutter">ansible-galaxy-cookiecutter</a> template utilizes <a href="https://github.com/jcook3701/nutri-matic">nutri-matic</a> hooks to pull both this documentation template along with <a href="https://github.com/jcook3701/sphinx-cookiecutter">sphinx-cookiecutter</a> template into generated project <code class="language-plaintext highlighter-rouge">$(PROJECT_ROOT)/docs/</code>.</p>

<p>Utilization of <a href="https://github.com/jcook3701/nutri-matic">nutri-matic</a> is the optimal way of integrating this template in projects.</p>

<hr />

<h2 id="development-strategy">Development Strategy:</h2>
<p><strong>Note:</strong> All Makefile commands are used in ci/cd to ensure that if they pass locally they should also pass once pushed to github.</p>
<h3 id="️-build-environment-venv">🐍️ Build environment (.venv)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make <span class="nb">install</span>
</code></pre></div></div>
<h3 id="-dependency-management-deptry">🧬 Dependency Management (deptry)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make dependency-check
</code></pre></div></div>
<h3 id="️-security-audit-pip-audit">🛡️ Security Audit (pip-audit)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make security
</code></pre></div></div>
<h3 id="-formatting-black">🎨 Formatting (black)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make format-check
</code></pre></div></div>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make format-fix
</code></pre></div></div>
<h3 id="-linting-jinja2-cli-ruff-tomllint--yaml-lint">🔍 Linting (jinja2-cli, ruff, tomllint, &amp; yaml-lint)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make lint-check
</code></pre></div></div>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make lint-fix
</code></pre></div></div>
<h3 id="-spellchecking-codespell">🎓 Spellchecking (codespell)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make spellcheck
</code></pre></div></div>
<h3 id="-typechecking-mypy">🧠 Typechecking (mypy)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make typecheck
</code></pre></div></div>
<h3 id="-testing-pytest">🧪 Testing (pytest)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make <span class="nb">test</span>
</code></pre></div></div>
<h3 id="-release-git-tag">🚀 Release (git tag)</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make release
</code></pre></div></div>
<h3 id="-build-help">❓ Build Help</h3>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>make <span class="nb">help</span>
</code></pre></div></div>

<hr />

<h3 id="authors-notes">Authors Notes:</h3>
<ol>
  <li>This code currently works with cookiecutter 1.7 from Ubuntu’s apt repositories.</li>
</ol>
