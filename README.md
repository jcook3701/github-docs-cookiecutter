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

<p>Cookiecutter generator for documentation, company, blog, portfolio, and landing-page websites on <strong>GitHub Pages</strong> with Jekyll. Shared metadata, URLs, dependencies, front matter, and theme capabilities are managed by one central Jinja configuration.</p>

<h2 id="theme-compatibility">Theme compatibility</h2>

<p>The generator only publishes combinations that have the layouts, dependencies, and supporting files needed to build. Selecting an unimplemented theme or an incompatible website type stops generation with a message explaining the limitation.</p>

<table>
  <thead>
    <tr>
      <th>Theme selection</th>
      <th>Compatible website types</th>
      <th>Integration</th>
      <th>License</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">just-the-docs/just-the-docs@v0.11.0</code></td>
      <td>Documentation</td>
      <td>Pinned remote theme</td>
      <td>MIT</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">pmarsceill/just-the-docs</code></td>
      <td>Documentation</td>
      <td>Legacy alias normalized to the pinned canonical theme</td>
      <td>MIT</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">carlosperate/jekyll-theme-rtd</code></td>
      <td>Documentation</td>
      <td>Pinned remote theme plus licensed collection-navigation override</td>
      <td>BSD-2-Clause</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">mmistakes/minimal-mistakes</code></td>
      <td>Documentation, company, blog, portfolio, landing page</td>
      <td>Pinned remote theme plus generated site-type navigation</td>
      <td>MIT</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">raviriley/agency-jekyll-theme</code></td>
      <td>Company, portfolio, landing page</td>
      <td>Commit-pinned remote theme plus generated data and Pages-safe resource overrides</td>
      <td>MIT</td>
    </tr>
  </tbody>
</table>

<h3 id="blocked-full-site-templates">Blocked full-site templates</h3>

<p>The selections below are complete starter repositories rather than interchangeable remote themes. They remain visible for migration compatibility and research, but generation is deliberately blocked until their required source trees, build contracts, and attribution files can be maintained as tested resource packs.</p>

<table>
  <thead>
    <tr>
      <th>Theme selection</th>
      <th>Limitation</th>
      <th>Upstream license or status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">alshedivat/al-folio</code></td>
      <td>Uses <code class="language-plaintext highlighter-rouge">al_folio_core</code> and a large pinned plugin and collection contract.</td>
      <td>MIT</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">poole/lanyon</code></td>
      <td>Requires its complete Poole layouts, includes, public assets, and pagination setup.</td>
      <td>MIT</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">zerostaticthemes/jekyll-serif-theme</code></td>
      <td>Requires company collections, data, layouts, images, and third-party asset credits.</td>
      <td>MIT; preserve upstream asset credits</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">CloudCannon/hydra-jekyll-template</code></td>
      <td>Requires its full marketing and blog source tree; upstream marks it legacy and unmaintained.</td>
      <td>MIT; legacy</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">emilbaehr/automatic-app-landing-page</code></td>
      <td>Requires device assets and application-store metadata.</td>
      <td>MIT</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">LeNPaul/Millennial</code></td>
      <td>Requires its blog layouts, data settings, feeds, Sass, and static assets.</td>
      <td>MIT</td>
    </tr>
  </tbody>
</table>

<p>Project Pages receive a repository <code class="language-plaintext highlighter-rouge">baseurl</code>; user or organization Pages use the domain root. A custom domain produces a normalized hostname-only <code class="language-plaintext highlighter-rouge">CNAME</code>, but the domain must also be configured in the repository’s GitHub Pages settings. Agency sites show an email contact action unless a current Formspree form path is explicitly configured.</p>

<hr />

<p><strong>Utilizes:</strong><br />
The <strong>github-docs-cookiecutter</strong> depends on the following repositories for its documentation and sub-features.</p>

<ul>
  <li><strong><a href="https://github.com/jcook3701/cookiecutter-cookiecutter">cookiecutter-cookiecutter</a></strong> Generates cookiecutter template projects and is able to be queried by generated projects for autogenerated file updates.</li>
  <li><strong><a href="https://github.com/jcook3701/github-docs-cookiecutter">Github docs</a></strong> via the cookiecutter-cookiecutter this project is used as a sub-template to generate documentation.</li>
  <li><strong><a href="https://github.com/jcook3701/nutri-matic">Nutri-Matic</a></strong> cookiecutter hooks and tools for documentation build. The nutrimatic package has become a .</li>
</ul>

<p><strong>Maintains:</strong><br />
The <strong>github-docs-cookiecutter</strong> is used to maintain documentation for the following projects.</p>

<p><strong>Cookiecutter Projects:</strong></p>
<ul>
  <li><strong><a href="https://github.com/jcook3701/cookiecutter-cookiecutter">cookiecutter-cookiecutter</a></strong></li>
  <li><strong><a href="https://github.com/jcook3701/python3-cookiecutter">python3-cookiecutter</a></strong></li>
  <li><strong><a href="https://github.com/jcook3701/ansible-galaxy-cookiecutter">ansible-galaxy-cookiecutter</a></strong></li>
</ul>

<p><strong>Python Projects:</strong></p>
<ul>
  <li><strong><a href="https://github.com/jcook3701/nutri-matic">Nutri-Matic</a></strong></li>
</ul>

<p><strong>Ansible Projects:</strong></p>
<ul>
  <li><strong><a href="https://github.com/jcook3701/jcook3701.docker">jcook3701.docker</a></strong> Ansible Galaxy collection used to install docker packages.</li>
  <li><strong><a href="https://github.com/jcook3701/jcook3701.flatpak">jcook3701.flatpak</a></strong> Ansible Galaxy collection used to install flatpak packages.</li>
  <li><strong><a href="https://github.com/jcook3701/jcook3701.pkgs">jcook3701.pkgs</a></strong> Ansible Galaxy collection used to install system (Debian, Ubuntu, RHEL) packages.</li>
  <li><strong><a href="https://github.com/jcook3701/jcook3701.source">jcook3701.source</a></strong> Ansible Galaxy collection used to install packages from source code.</li>
  <li><strong><a href="https://github.com/jcook3701/jcook3701.snap">jcook3701.snap</a></strong> Ansible Galaxy collection used to install snap packages.</li>
</ul>

<hr />

<p>🛠️ <strong>CI/CD Check List:</strong></p>

<!-- [![CLA assistant](https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/cla.yml/badge.svg)]() -->
<ul>
  <li><img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/dependency-check.yml/badge.svg" alt="dependency-check" /></li>
  <li><img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/format-check.yml/badge.svg" alt="format-check" /></li>
  <li><img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/lint-check.yml/badge.svg" alt="lint-check" /></li>
  <li><img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/security-audit.yml/badge.svg" alt="security-audit" /></li>
  <li><img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/spellcheck.yml/badge.svg" alt="spellcheck" /></li>
  <li><img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/tests.yml/badge.svg" alt="tests" /></li>
  <li><img src="https://github.com/jcook3701/github-docs-cookiecutter/actions/workflows/typecheck.yml/badge.svg" alt="typecheck" /></li>
</ul>

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

<h2 id="-getting-started">🌱 Getting Started</h2>

<ul>
  <li><a href="https://jcook3701.github.io/github-docs-cookiecutter/manual/setup-guide/requirements">Requirements</a></li>
  <li><a href="https://jcook3701.github.io/github-docs-cookiecutter/manual/introduction/installation-guide">Installation guide</a></li>
</ul>

<h2 id="-documentation">📚 Documentation</h2>

<p>The github-docs-cookiecutter documentation is available at <a href="https://jcook3701.github.io/github-docs-cookiecutter">docs</a>.</p>

<h2 id="-contributing">🤝 Contributing</h2>

<p>If you’re interested in contributing to the github-docs-cookiecutter project:</p>
<ul>
  <li>Start by reading the <a href="https://jcook3701.github.io/github-docs-cookiecutter/manual/developer-resources/contribute">contributing guide</a>.</li>
  <li>Learn how to setup your local environment, in our <a href="https://jcook3701.github.io/github-docs-cookiecutter/manual/contribute/developer-guide">developer guide</a>.</li>
  <li>Look through our <a href="https://jcook3701.github.io/github-docs-cookiecutter/manual/contribute/style-guides/index">style guide</a>.</li>
</ul>

<hr />

<h2 id="-authors-notes">🍹 Authors Notes</h2>

<ol>
  <li>This code currently works with cookiecutter (2.6) from PyPi repositories.</li>
</ol>

<h2 id="️-license">⚖️ License</h2>

<p>Copyright (c) 2025-2026, Jared Cook</p>

<p>This project is licensed under the <strong>AGPL-3.0-or-later License</strong>.<br />
See the <a href="https://github.com/jcook3701/github-docs-cookiecutter/blob/master/LICENSE.md">LICENSE</a> file for the full license text.</p>

<p>SPDX-License-Identifier: AGPL-3.0-or-later</p>
