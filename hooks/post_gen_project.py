# post_gen_project.py for github-docs-cookiecutter
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

import json
import os
import shutil
from pathlib import Path
from urllib.parse import urlsplit

from nutrimatic.core import make
from nutrimatic.hooks.post_gen_logic import (
    generate_docs_templates,
    get_make_cmds,
    rename_j2_templates,
)

MANIFEST_NAME = ".cookiecutter-site.json"
RESOURCE_ROOTS = {
    "site": "_site_resources",
    "theme": "_theme_resources",
}


def _load_site_manifest(project_root: Path) -> dict[str, object]:
    """Load and minimally validate the generated-site manifest.

    Args:
        project_root: Root of the freshly generated Cookiecutter project.

    Returns:
        Parsed manifest values.

    Raises:
        RuntimeError: If the manifest is missing.
        ValueError: If the manifest is not valid JSON or has an unknown schema.
    """
    manifest_path = project_root / MANIFEST_NAME
    if not manifest_path.is_file():
        msg = (
            f"Missing {MANIFEST_NAME}; the generated project cannot be finalized. "
            "The central theme registry must render this manifest."
        )
        raise RuntimeError(msg)

    try:
        manifest_data: object = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        msg = f"Invalid JSON in {MANIFEST_NAME}: {error}"
        raise ValueError(msg) from error

    if not isinstance(manifest_data, dict):
        msg = f"Invalid {MANIFEST_NAME}: the top-level value must be an object."
        raise ValueError(msg)
    if manifest_data.get("schema_version") != 1:
        schema = manifest_data.get("schema_version")
        msg = f"Unsupported {MANIFEST_NAME} schema version: {schema!r}."
        raise ValueError(msg)

    return manifest_data


def _manifest_text(manifest: dict[str, object], key: str) -> str:
    """Return a required non-empty string from the site manifest.

    Args:
        manifest: Parsed generated-site manifest.
        key: Manifest key to read.

    Returns:
        The stripped manifest value.

    Raises:
        ValueError: If the value is missing or is not a non-empty string.
    """
    value = manifest.get(key)
    if not isinstance(value, str) or not value.strip():
        msg = f"Invalid {MANIFEST_NAME}: {key!r} must be a non-empty string."
        raise ValueError(msg)
    return value.strip()


def _manifest_bool(manifest: dict[str, object], key: str) -> bool:
    """Return a required boolean from the site manifest.

    Args:
        manifest: Parsed generated-site manifest.
        key: Manifest key to read.

    Returns:
        The manifest boolean.

    Raises:
        ValueError: If the value is not a boolean.
    """
    value = manifest.get(key)
    if not isinstance(value, bool):
        msg = f"Invalid {MANIFEST_NAME}: {key!r} must be a boolean."
        raise ValueError(msg)
    return value


def _validate_selection(manifest: dict[str, object]) -> tuple[str, str]:
    """Ensure the requested theme and site type are a supported combination.

    Args:
        manifest: Parsed generated-site manifest.

    Returns:
        The selected theme and site type.

    Raises:
        RuntimeError: If the selected theme is not implemented.
        ValueError: If the theme and site type are incompatible.
    """
    theme = _manifest_text(manifest, "selected_theme")
    site_type = _manifest_text(manifest, "site_type")
    support_message = _manifest_text(manifest, "support_message")

    if not _manifest_bool(manifest, "theme_supported"):
        msg = f"Theme {theme!r} is not supported for site type {site_type!r}: {support_message}"
        raise RuntimeError(msg)
    if not _manifest_bool(manifest, "site_type_supported"):
        msg = f"Theme {theme!r} is incompatible with site type {site_type!r}: {support_message}"
        raise ValueError(msg)
    if not _manifest_bool(manifest, "selection_supported"):
        msg = f"Theme {theme!r} cannot generate site type {site_type!r}: {support_message}"
        raise ValueError(msg)

    return theme, site_type


def _copy_resource_tree(source: Path, project_root: Path) -> None:
    """Merge a staged resource tree without replacing generated files.

    Existing files take precedence over staged resources. Directories are
    merged recursively so independent site and theme packs can contribute to
    the same generated directory.

    Args:
        source: Staged resource-pack directory.
        project_root: Destination project root.

    Raises:
        FileExistsError: If a file/directory type conflict prevents merging.
        RuntimeError: If a staged entry is neither a regular file nor directory.
    """
    for item in sorted(source.rglob("*")):
        relative_path = item.relative_to(source)
        destination = project_root / relative_path

        if item.is_dir():
            if destination.exists() and not destination.is_dir():
                msg = f"Resource directory collides with file: {relative_path}"
                raise FileExistsError(msg)
            destination.mkdir(parents=True, exist_ok=True)
            continue

        if item.is_file():
            if destination.exists():
                if destination.is_dir():
                    msg = f"Resource file collides with directory: {relative_path}"
                    raise FileExistsError(msg)
                print(f"⚠️  Preserving existing generated file: {relative_path}")
                continue
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, destination)
            continue

        msg = f"Unsupported staged resource entry: {item}"
        raise RuntimeError(msg)


def _materialize_resource_packs(
    project_root: Path, manifest: dict[str, object]
) -> None:
    """Publish the resource packs selected by the central registry.

    Args:
        project_root: Root of the freshly generated project.
        manifest: Parsed generated-site manifest.

    Raises:
        RuntimeError: If a selected resource pack is absent.
        ValueError: If a resource-pack identifier is malformed.
    """
    resource_packs = manifest.get("resource_packs")
    if not isinstance(resource_packs, list) or not all(
        isinstance(pack, str) for pack in resource_packs
    ):
        msg = f"Invalid {MANIFEST_NAME}: 'resource_packs' must be a list of strings."
        raise ValueError(msg)

    for resource_pack in resource_packs:
        category, separator, pack_name = resource_pack.partition("/")
        if (
            not separator
            or category not in RESOURCE_ROOTS
            or not pack_name
            or "/" in pack_name
            or pack_name in {".", ".."}
        ):
            msg = f"Invalid resource-pack identifier: {resource_pack!r}."
            raise ValueError(msg)

        source = project_root / RESOURCE_ROOTS[category] / pack_name
        if not source.is_dir():
            msg = f"Selected resource pack is missing: {resource_pack!r}."
            raise RuntimeError(msg)
        _copy_resource_tree(source, project_root)


def _remove_generated_path(path: Path) -> None:
    """Remove a known generated file or directory when it exists.

    Args:
        path: Explicit generated path to remove.
    """
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def _custom_domain_hostname(custom_domain: str) -> str:
    """Normalize a custom-domain value to the hostname required by CNAME.

    Args:
        custom_domain: Domain input, optionally including a URL scheme or path.

    Returns:
        Lowercase hostname without a trailing dot.

    Raises:
        ValueError: If the input does not contain a usable hostname.
    """
    domain = custom_domain.strip()
    parsed = urlsplit(domain if "://" in domain else f"//{domain}")
    hostname = parsed.hostname
    if hostname is None or not hostname.strip():
        msg = f"Invalid custom domain {custom_domain!r}: no hostname was found."
        raise ValueError(msg)

    normalized = hostname.strip().rstrip(".").lower()
    if not normalized or any(character.isspace() for character in normalized):
        msg = f"Invalid custom domain {custom_domain!r}: malformed hostname."
        raise ValueError(msg)
    return normalized


def _write_cname(project_root: Path, manifest: dict[str, object]) -> None:
    """Write a normalized GitHub Pages CNAME only for custom domains.

    Args:
        project_root: Root of the freshly generated project.
        manifest: Parsed generated-site manifest.

    Raises:
        ValueError: If ``custom_domain`` is not a string or cannot be normalized.
    """
    custom_domain = manifest.get("custom_domain")
    if not isinstance(custom_domain, str):
        msg = f"Invalid {MANIFEST_NAME}: 'custom_domain' must be a string."
        raise ValueError(msg)

    cname_path = project_root / "CNAME"
    if not custom_domain.strip():
        _remove_generated_path(cname_path)
        return

    hostname = _custom_domain_hostname(custom_domain)
    cname_path.write_text(f"{hostname}\n", encoding="utf-8")


def finalize_generated_project(project_root: Path) -> None:
    """Finalize supported resources and remove generation-only artifacts.

    Args:
        project_root: Root of the freshly generated Cookiecutter project.
    """
    manifest = _load_site_manifest(project_root)
    _, site_type = _validate_selection(manifest)
    _materialize_resource_packs(project_root, manifest)

    if site_type != "documentation":
        _remove_generated_path(project_root / "_manual")
        _remove_generated_path(project_root / "_resources")

    _write_cname(project_root, manifest)

    for staging_root in RESOURCE_ROOTS.values():
        _remove_generated_path(project_root / staging_root)
    _remove_generated_path(project_root / MANIFEST_NAME)


def main() -> None:
    """Run Cookiecutter post-generation initialization."""
    # Rename rendered Jinja2 files and directories before other initialization.
    # This must also run in CI, even when documentation generation is skipped.
    rename_j2_templates()

    # Materialize the selected resource packs and remove staging artifacts for
    # both local and CI generation before optional initialization can return.
    finalize_generated_project(Path.cwd())

    # Detect CI (e.g. GitHub Actions, GitLab CI, etc.)
    if os.getenv("CI"):
        print("⚙️  Detected CI environment — skipping GitHub Docs generation.")
        return
    os.environ["COOKIECUTTER_HOOKS"] = "true"

    # Access cookiecutter context safely
    context = json.loads("""{{ cookiecutter | jsonify }}""")
    generate_docs_templates(context)

    # Run make commands to get project seeded
    make_cmds: list[str] = get_make_cmds(context)

    for cmd in make_cmds:
        make(cmd)


if __name__ == "__main__":
    main()
