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

<h2 id="overview-1">Overview:</h2>
<p>Template cookiecutter project for Github Pages (Jekyll).  Skip the boring stuff and get to the work that matters.</p>

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

<h2 id="commit-help">Commit Help:</h2>
<p><strong>Note:</strong> Commits are required to be conventional git commit message.  This helps with the auto-generation of the changelog files and is enforced by pre-commit.<br />
<strong>example:</strong></p>
<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code>&lt;<span class="nb">type</span><span class="o">&gt;[</span>optional scope]: &lt;description&gt;

<span class="o">[</span>optional body]

<span class="o">[</span>optional footer<span class="o">(</span>s<span class="o">)]</span>
</code></pre></div></div>
<ul>
  <li><code class="language-plaintext highlighter-rouge">&lt;type&gt;</code>: A required noun that describes the nature of the change.</li>
  <li><code class="language-plaintext highlighter-rouge">[optional scope]</code>: An optional phrase within parentheses that specifies the part of the codebase being affected (e.g., fix(parser):).</li>
  <li><code class="language-plaintext highlighter-rouge">&lt;description&gt;</code>: A required short, imperative-mood summary of the changes.</li>
  <li><code class="language-plaintext highlighter-rouge">[optional body]</code>: A longer description providing additional context and “what and why” details.</li>
  <li><code class="language-plaintext highlighter-rouge">[optional footer(s)]</code>: Used for adding meta-information, such as issue references (Fixes #123) or indicating breaking changes.</li>
</ul>

<hr />

<h2 id="requirements">Requirements:</h2>
<ol>
  <li>Python 3.11
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span><span class="nb">sudo </span>apt <span class="nb">install </span>python3.11
</code></pre></div>    </div>
  </li>
  <li><a href="https://rust-lang.org/tools/install/">rustup</a><br />
<strong>Note:</strong> I found that it is easiest to use rustup to manage rustc and cargo but this is not required.<br />
<strong>Example:</strong> Install rustup with the following:
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>curl <span class="nt">--proto</span> <span class="s1">'=https'</span> <span class="nt">--tlsv1</span>.2 <span class="nt">-sSf</span> https://sh.rustup.rs | sh
</code></pre></div>    </div>
  </li>
  <li><a href="https://git-cliff.org/">git-cliff</a><br />
<strong>Note:</strong> git-cliff can generate changelog files from the Git history by utilizing conventional commits as well as regex-powered custom parsers.
    <div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cargo <span class="nb">install </span>git-cliff
</code></pre></div>    </div>
  </li>
</ol>

<hr />

<h3 id="authors-notes">Authors Notes:</h3>
<ol>
  <li>This code currently works with cookiecutter 1.7 from Ubuntu’s apt repositories.</li>
</ol>

<!--
### Authors Hidden TODO's
12/4/2025 - Need to weigh out if it is worth the work to move to DJLint as jinja2 seems to be doing the job well.
1. ~~[markdown](https://github.com/jackdewinter/pymarkdown) linter.~~  
      * ~~[docs](https://pymarkdown.readthedocs.io/en/latest/getting-started/)~~  
2. [djlint](https://djlint.com/)  
      * Swap jinja2 for djlint...

-->
