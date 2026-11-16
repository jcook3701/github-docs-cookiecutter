# test_bake_project.py for github-docs-cookiecutter
#
# SPDX-FileCopyrightText: Copyright (c) 2025-2026, Jared Cook
# SPDX-License-Identifier: AGPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Integration tests for real Cookiecutter-generated Jekyll projects."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any

import pytest
import yaml  # type: ignore[import-untyped]
from pytest_cookies.plugin import Cookies, Result

JUST_THE_DOCS = "just-the-docs/just-the-docs@v0.11.0"
JUST_THE_DOCS_ALIAS = "pmarsceill/just-the-docs"
READ_THE_DOCS = "carlosperate/jekyll-theme-rtd"
MINIMAL_MISTAKES = "mmistakes/minimal-mistakes"
AGENCY = "raviriley/agency-jekyll-theme"

SUPPORTED_THEMES = (
    (JUST_THE_DOCS, "documentation", JUST_THE_DOCS, "default"),
    (JUST_THE_DOCS_ALIAS, "documentation", JUST_THE_DOCS, "default"),
    (READ_THE_DOCS, "documentation", f"{READ_THE_DOCS}@v1.4.0", "default"),
    (MINIMAL_MISTAKES, "blog", f"{MINIMAL_MISTAKES}@4.28.1", "home"),
    (
        AGENCY,
        "company",
        f"{AGENCY}@d477a171ec9633c980c8ef9098eeac39b60ceba3",
        "home",
    ),
)

UNSUPPORTED_THEMES = (
    "alshedivat/al-folio",
    "poole/lanyon",
    "zerostaticthemes/jekyll-serif-theme",
    "CloudCannon/hydra-jekyll-template",
    "emilbaehr/automatic-app-landing-page",
    "LeNPaul/Millennial",
)

SITE_TYPE_CASES = (
    ("documentation", JUST_THE_DOCS, "_manual/introduction/index.md"),
    ("company", MINIMAL_MISTAKES, "about.md"),
    ("blog", MINIMAL_MISTAKES, "categories.md"),
    ("portfolio", MINIMAL_MISTAKES, "_projects/featured-project.md"),
    ("landing_page", MINIMAL_MISTAKES, "features.md"),
)

MINIMAL_MISTAKES_NAVIGATION_CASES = (
    ("documentation", "/manual/introduction/getting-started"),
    ("company", "/services/"),
    ("blog", "/categories/"),
    ("portfolio", "/projects/featured/"),
    ("landing_page", "/features/"),
)


@pytest.fixture(autouse=True)
def _cookiecutter_ci(monkeypatch: pytest.MonkeyPatch) -> None:
    """Run only deterministic generation steps in Cookiecutter hooks.

    CI mode still exercises Nutri-Matic's suffix renamer and this template's
    site finalization, while skipping unrelated project-seeding commands.
    """
    monkeypatch.setenv("CI", "1")


def _bake(cookies: Cookies, **extra_context: object) -> Path:
    """Bake a project and return its generated path.

    Args:
        cookies: pytest-cookies fixture.
        **extra_context: Cookiecutter context overrides.

    Returns:
        Path to the successfully generated project.
    """
    result = cookies.bake(extra_context=extra_context or None)
    assert result.exit_code == 0, result.exception
    assert result.exception is None
    project_path = result.project_path
    assert isinstance(project_path, Path)
    return project_path


def _load_yaml(path: Path) -> dict[str, Any]:
    """Load a YAML mapping and assert that it is nonempty."""
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data


def _load_front_matter(path: Path) -> dict[str, Any]:
    """Load and validate a Markdown file's leading YAML front matter."""
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines and lines[0] == "---", f"front matter must start {path}"
    try:
        closing_index = lines.index("---", 1)
    except ValueError as error:  # pragma: no cover - assertion message path
        raise AssertionError(f"front matter is not closed in {path}") from error
    data = yaml.safe_load("\n".join(lines[1:closing_index]))
    assert isinstance(data, dict)
    assert isinstance(data.get("title"), str)
    assert isinstance(data.get("layout"), str)
    return data


def _assert_no_jinja_suffixes(project_path: Path) -> None:
    """Assert Nutri-Matic finalized every generated Jinja filename."""
    remaining = [path for path in project_path.rglob("*") if path.name.endswith(".j2")]
    assert remaining == []


def test_bake_with_defaults(cookies: Cookies) -> None:
    """Ensure the default documentation project is fully finalized."""
    project_path = _bake(cookies)

    assert (project_path / "Makefile").is_file()
    assert (project_path / "Gemfile").is_file()
    assert (project_path / "_config.yml").is_file()
    assert (project_path / "_manual").is_dir()
    assert not (project_path / ".cookiecutter-site.json").exists()
    config = _load_yaml(project_path / "_config.yml")
    assert {"Makefile", "README.md", "docs"}.issubset(config["exclude"])
    _assert_no_jinja_suffixes(project_path)


def test_bake_with_custom_name(cookies: Cookies) -> None:
    """Ensure a custom project name controls the output directory."""
    project_path = _bake(cookies, project_name="Test Project")
    assert project_path.name == "test-project"


@pytest.mark.parametrize(
    ("theme", "site_type", "remote_theme", "home_layout"),
    SUPPORTED_THEMES,
)
def test_supported_theme_outputs(
    cookies: Cookies,
    theme: str,
    site_type: str,
    remote_theme: str,
    home_layout: str,
) -> None:
    """Bake every functional remote theme selection with pinned metadata."""
    project_path = _bake(cookies, theme=theme, site_type=site_type)
    config = _load_yaml(project_path / "_config.yml")
    index = _load_front_matter(project_path / "index.md")
    gemfile = (project_path / "Gemfile").read_text(encoding="utf-8")

    assert config["remote_theme"] == remote_theme
    assert index["layout"] == home_layout
    assert "jekyll-remote-theme" in config["plugins"]
    assert 'gem "jekyll-remote-theme"' in gemfile
    for plugin in config["plugins"]:
        assert f'gem "{plugin}"' in gemfile
    _assert_no_jinja_suffixes(project_path)


@pytest.mark.parametrize("theme", UNSUPPORTED_THEMES)
def test_full_site_starters_fail_explicitly(cookies: Cookies, theme: str) -> None:
    """Do not emit sites for starters whose required resources are not vendored."""
    result: Result = cookies.bake(extra_context={"theme": theme})
    assert result.exit_code != 0
    assert result.exception is not None
    assert result.project_path is None


def test_theme_matrix_covers_every_configured_selection() -> None:
    """Keep the support contract in sync with all eleven theme choices."""
    covered = {theme for theme, *_rest in SUPPORTED_THEMES} | set(UNSUPPORTED_THEMES)
    assert len(covered) == 11


@pytest.mark.parametrize(("site_type", "theme", "expected_path"), SITE_TYPE_CASES)
def test_site_type_content_selection(
    cookies: Cookies,
    site_type: str,
    theme: str,
    expected_path: str,
) -> None:
    """Generate useful content while excluding documentation from other sites."""
    project_path = _bake(cookies, site_type=site_type, theme=theme)

    assert (project_path / expected_path).is_file()
    _load_front_matter(project_path / "index.md")
    if site_type == "documentation":
        assert (project_path / "_manual").is_dir()
        assert (project_path / "_resources").is_dir()
    else:
        assert not (project_path / "_manual").exists()
        assert not (project_path / "_resources").exists()


@pytest.mark.parametrize(
    ("site_type", "expected_url"), MINIMAL_MISTAKES_NAVIGATION_CASES
)
def test_minimal_mistakes_navigation_matches_generated_content(
    cookies: Cookies, site_type: str, expected_url: str
) -> None:
    """Replace the remote theme's sample masthead links for every site type."""
    project_path = _bake(cookies, site_type=site_type, theme=MINIMAL_MISTAKES)
    navigation = _load_yaml(project_path / "_data/navigation.yml")
    entries = navigation["main"]

    assert isinstance(entries, list)
    assert expected_url in {entry["url"] for entry in entries}
    assert all(entry["title"] != "Quick-Start Guide" for entry in entries)


def test_company_values_yaml_and_repository_owner(cookies: Cookies) -> None:
    """Preserve apostrophes and distinguish repository ownership from socials."""
    project_path = _bake(
        cookies,
        project_name="Cooks Portal",
        company="Cook's Code, Inc.",
        description="Cook's products & services: reliable, fast, and friendly.",
        github_org="cooks-code",
        github_username="cook-personal",
        site_type="company",
        theme=MINIMAL_MISTAKES,
    )
    config = _load_yaml(project_path / "_config.yml")
    readme = (project_path / "README.md").read_text(encoding="utf-8")

    assert config["title"] == "Cook's Code, Inc."
    assert (
        config["description"]
        == "Cook's products & services: reliable, fast, and friendly."
    )
    assert config["repository"] == "cooks-code/cooks-portal"
    assert config["repo_url"] == "https://github.com/cooks-code/cooks-portal"
    assert config["url"] == "https://cooks-code.github.io"
    assert config["baseurl"] == "/cooks-portal"
    assert "jekyll-paginate" not in config["plugins"]
    assert config["atom_feed"]["hide"] is True
    assert "Cook's Code, Inc." in readme
    assert "{{" not in readme


def test_pages_routing_and_custom_domain(cookies: Cookies) -> None:
    """Generate correct custom-domain routing and a normalized CNAME."""
    project_path = _bake(
        cookies,
        site_type="company",
        theme=MINIMAL_MISTAKES,
        custom_domain="https://Docs.Example.com:8443/subpath?preview=1",
    )
    config = _load_yaml(project_path / "_config.yml")

    assert config["url"] == "https://docs.example.com"
    assert config["baseurl"] == ""
    assert (project_path / "CNAME").read_text(encoding="utf-8") == "docs.example.com\n"


def test_user_or_organization_pages_have_no_baseurl(cookies: Cookies) -> None:
    """Do not add a repository path to user or organization Pages sites."""
    project_path = _bake(
        cookies,
        pages_site_type="user_or_organization",
    )
    config = _load_yaml(project_path / "_config.yml")
    assert config["url"] == "https://jcook3701.github.io"
    assert config["baseurl"] == ""
    assert config["github_io_url"] == "https://jcook3701.github.io"
    assert not (project_path / "CNAME").exists()


def test_front_matter_is_valid_and_theme_aware(cookies: Cookies) -> None:
    """Validate all documentation front matter and Just-the-Docs navigation."""
    project_path = _bake(cookies)
    pages = [project_path / "index.md"]
    pages.extend(sorted((project_path / "_manual").rglob("*.md")))
    pages.extend(sorted((project_path / "_resources").rglob("*.md")))

    for page in pages:
        metadata = _load_front_matter(page)
        assert metadata["layout"] == "default"

    style_guide = _load_front_matter(
        project_path / "_manual/contribute/style-guides/python.md"
    )
    assert style_guide["parent"] == "Style Guide"
    assert style_guide["grand_parent"] == "Contribute"


def test_liquid_and_deployment_workflow_are_preserved(cookies: Cookies) -> None:
    """Keep Liquid expressions intact and emit a current Pages workflow."""
    project_path = _bake(cookies)
    carousel = (project_path / "_includes/image-carousel.html").read_text(
        encoding="utf-8"
    )
    workflow = (project_path / ".github/workflows/pages.yml").read_text(
        encoding="utf-8"
    )
    makefile = (project_path / "Makefile").read_text(encoding="utf-8")

    assert "{% assign slides = site.carousel_images %}" in carousel
    assert "{{ image.src | relative_url }}" in carousel
    assert "${{ steps.pages.outputs.base_path }}" in workflow
    assert "run: make build" in workflow
    assert "JEKYLL_BUILD_ARGS" in workflow
    assert "actions/configure-pages@v5" in workflow
    assert "actions/upload-pages-artifact@v4" in workflow
    assert "actions/deploy-pages@v5" in workflow
    assert "$(JEKYLL_BUILD_ARGS)" in makefile
    dry_run = subprocess.run(
        ["make", "-n", "build", "JEKYLL_BUILD_ARGS=--baseurl /preview"],
        cwd=project_path,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "--baseurl /preview" in dry_run.stdout


def test_generated_makefile_preserves_special_character_metadata(
    cookies: Cookies,
) -> None:
    """Keep Make and the shell from reinterpreting generated help metadata."""
    project_path = _bake(
        cookies,
        project_name="Cash #1 $HOME Site",
        author="D'Angelo #1 $USER",
        version="1.0 # beta $VERSION",
    )
    help_result = subprocess.run(
        ["make", "-s", "help"],
        cwd=project_path,
        check=True,
        capture_output=True,
        text=True,
    )

    assert "Cash #1 $HOME Site" in help_result.stdout
    assert "D'Angelo #1 $USER" in help_result.stdout
    assert "1.0 # beta $VERSION" in help_result.stdout


def test_agency_theme_materializes_required_data(cookies: Cookies) -> None:
    """Supply the data and portfolio content required by Agency's home layout."""
    project_path = _bake(cookies, site_type="company", theme=AGENCY)

    assert (project_path / "_data/navigation.yml").is_file()
    assert (project_path / "_data/sitetext.yml").is_file()
    assert (project_path / "_data/style.yml").is_file()
    assert (project_path / "THIRD_PARTY_NOTICES.md").is_file()
    assert (project_path / "legal.md").is_file()
    contact = (project_path / "_includes/contact.html").read_text(encoding="utf-8")
    footer = (project_path / "_includes/footer.html").read_text(encoding="utf-8")
    head = (project_path / "_includes/head.html").read_text(encoding="utf-8")
    layout = (project_path / "_layouts/default.html").read_text(encoding="utf-8")
    assert "mailto:{{ site.email | escape }}" in contact
    assert "{{ '/legal/' | relative_url }}" in footer
    assert "{{ '/assets/css/agency.css' | relative_url }}" in head
    assert "{{ '/assets/js/agency.min.js' | relative_url }}" in layout
    portfolio_items = list((project_path / "_portfolio").glob("*.md"))
    assert portfolio_items
    _load_front_matter(portfolio_items[0])


def test_agency_formspree_path_uses_supported_theme_setting(cookies: Cookies) -> None:
    """Configure Agency's current Formspree endpoint instead of email fallback."""
    project_path = _bake(
        cookies,
        site_type="company",
        theme=AGENCY,
        formspree_form_path="f/example-form-id",
    )
    config = _load_yaml(project_path / "_config.yml")

    assert config["formspree_form_path"] == "f/example-form-id"


def test_rtd_theme_materializes_collection_navigation(cookies: Cookies) -> None:
    """Make generated documentation collections visible in RTD's sidebar."""
    project_path = _bake(cookies, theme=READ_THE_DOCS)
    navigation = (project_path / "_includes/nav.html").read_text(encoding="utf-8")
    page = _load_front_matter(project_path / "_manual/introduction/getting-started.md")

    assert "site.manual" in navigation
    assert "site.resources" in navigation
    assert page["nav_order"] == 1
    assert (project_path / "THIRD_PARTY_NOTICES.md").is_file()
