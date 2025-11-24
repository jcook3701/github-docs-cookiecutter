"""ansible-galaxy-cookiecutter Package

© All rights reserved. Jared Cook

See the LICENSE file for more details.

Author: Jared Cook
Discription: Post project generation Scripts.
"""

import os
import sys
from pathlib import Path

# Add the generated package to sys.path so Python can find it
PROJECT_DIR = Path.cwd()
# HOOKS_DIR = PROJECT_DIR / "_shared_hooks" / "post_gen_logic"
# sys.path.insert(0, str(HOOKS_DIR))


def main() -> None:
    """Cookiecutter Post Generation Scripts"""
    # Detect CI (e.g. GitHub Actions, GitLab CI, etc.)
    if os.getenv("CI"):
        print("⚙️  Detected CI environment — skipping GitHub Docs generation.")
        return


if __name__ == "__main__":
    main()
