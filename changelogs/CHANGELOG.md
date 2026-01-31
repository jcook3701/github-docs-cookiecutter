# --------------------------------------------------
# Changelog:
# --------------------------------------------------

## [unreleased]

### ⚙️  Miscellaneous

- Feat 03 (#17)

* chore(rev): rev up to new patch version after first tag release!

* fix(build): fix the build so that released changelogs work correctly now.  rev version now revs up readme file as well.

* fix(template): Updated project to use project_slug as cookiecutter standard.

* feat(template): added template generated settings under docs as standard.

* fix(tests): Fixed output of project path to the new expected output.

* fix(template): fixed cookiecutter.json.
- Feat 004 (#18)

* feat(upgrade): setting up project for upgrade from cookiecutter-cookiecutter.

* Update template

* Update template

* Update template
- Merge pull request #19 from jcook3701/develop

Feat 004 (#18)
- Merge pull request #20 from jcook3701/feat-005

Feat (005)
- Merge pull request #21 from jcook3701/develop

Develop
- Feat 006 (#23)

* feat(docs): Preparing project for Contributor License Agreements and getting major project documentation ready.

* chore(update): Update from cookiecutter-cookiecutter using cookiecutter_project_upgrader.
- Merge pull request #24 from jcook3701/develop

Feat 006 (#23)
- Feat 007 cla continued (#25)

* feat(cla): CLA documentation and much more.  Getting project contribution guidelines setup.

* fix(build): Fixed cookiecutter.json file to ensure build success.
- Merge pull request #26 from jcook3701/develop

Feat 007 cla continued (#25)
- Feat 009 jekyll ci cd (#27)

* fix(docs): fix for the jekyll ci/cd.  Switched to my makefile build and am using that build path.

* chore(upgrade): Update template from cookiecutter-cookiecutter parent project using cookiecutter_project_upgrader.
- Merge pull request #28 from jcook3701/develop

Feat 009 jekyll ci cd (#27)
- Feat 008 cla (#30)

* Update template

* fix(docs): fix for the jekyll ci/cd.  Switched to my makefile build and am using that build path.

* Update template

* fix(readme): Moved commit-message help out of readme into better spot within documentation.  Also info update for contributing.

* feat(cla): CLA Policy and CLA Privacy Policy setup.

* fix(license): Preparation for license update.

* Update template

* fix(build): fixed build errors.
- Merge pull request #32 from jcook3701/develop

Feat 008 cla (#30)
- Feat 010 (#33)

* chore(update) Update template from cookiecutter-cookiecutter.

* fix(license): Removed doubled copy of the license file.

* fix(links): Fix for document links.
- Merge pull request #34 from jcook3701/develop

Feat 010 (#33)
- Feat 011 cla fix (#35)

* fix(docs): jekyll ci/cd fix.

* fix(cla): Fixed cla path-to-document to not use a template file.
- Merge pull request #36 from jcook3701/develop

Feat 011 cla fix (#35)
- Feat 012 (#37)

* feat(build): Updates to documentation makefile.

* fix(cla): Fix for CLA fix for master branch.
- Merge pull request #38 from jcook3701/develop

Feat 012 (#37)
- Creating file for storing CLA Signatures
- Feat 012 (#39)

* feat(build): Updates to documentation makefile.

* fix(cla): Fix for CLA fix for master branch.

* chore(template) Update template from cookiecutter-cookiecutter repository. 

* fix(makefile): Minor fix for documentation emoji.
- Merge pull request #40 from jcook3701/develop

Feat 012 (#39)
- Feat 013 (#41)

* fix(makefile): emoji for documentation fixed.

* fix(ci/cd): Jekyll build and deploy fix.

* fix(cla): Forgot to add '$' to github.repo in cla ci/cd.
- Merge pull request #42 from jcook3701/develop

Feat 013 (#41)
- Feat 014 (#43)

* fix(links): Fix for document links.

* fix(links): More link fixes.

* feat(docs): Added variables to jekyll configuration.

* fix(upgrader): Fixed upgrader file.
- Merge pull request #44 from jcook3701/develop

Feat 014 (#43)
- Feat 015 (#45)

* fix(links): More link fixes along with a few configuration fixes to remove warnings.

* feat(links): More links and general docs template updates.

* feat(docs): Documentation updates.

* chore(upgrade): Update template from cookiecutter-cookiecutter.
- Merge pull request #46 from jcook3701/develop

Feat 015 (#45)
- Feat 016 (#47)

* fix(docs): Docs are not being updated with upgrade for some reason.  debugging.

* fix(docs): Revert. Docs are not being updated with upgrade for some reason.  debugging.

* fix(template): figured out _is_sub_template needs to be false for the documents.  Need to fix the cookiecutter-cookiecutter hooks.

* fix(configuration): cookiecutter upgrader configuration fix.

* fix(template): Forgot to add configuration setting to main settings file.

* fix(template): Forgot to add configuration setting to main settings file.

* fix(theme): Update to latest just the docs theme.

* fix(template): minor fix.
- Merge pull request #48 from jcook3701/develop

Feat 016 (#47)
- Feat 017 (#49)

* fix(configuration): I think this should fix the last of the problems with main showing up where master should for this repository.

* feat(docs): updates to setup, getting-started, and initial tutorials.

* fix(links): Major fixes for documentation links.

* fix(docs): Fixed license image shield.

* feat(faq): Added the Frequently asked questions page.

* fix(ci/cd): Removed doubles of pull request templates that are not needed.
- Merge pull request #50 from jcook3701/develop

Feat 017 (#49)
- Feat 018 (#51)

* chore(update): Update template using ```cookiecutter_project_upgrader``` from cookiecutter-cookiecutter.
- Merge pull request #52 from jcook3701/develop

Feat 018 (#51)
- *(CLA)* Creating file for storing CLA Signatures.
- Feat 019 (#53)

* fix(cla): removed signatures folder as it should be re-generated as cla/v1/signatures.json.

* feat(docs): Minor documentation update.

* fix(configuration): Update to template_type configuration.

* chore(update): Update template using ```cookiecutter_project_upgrader```
- Merge pull request #54 from jcook3701/develop

Feat 019 (#53)
- Feat 020 (#55)

* fix(docs): readme updates.

* fix(docs): readme ci/cd checklist updates.

* fix(docs): Fixed FAQ page name.

* feat(docs): updates to git commit message info.
- Merge pull request #56 from jcook3701/develop

Feat 020 (#55)
- Feat 021 (#57)

* fix(upgrader): Fix to move project back to cookiecutter template project.

* chore(update): Update template from cookiecutter-cookiecutter using cookiecutter_project_upgrader.

* feat(upgrader): Updates to upgrader configuration file to fix hooks upgrade.
- Merge pull request #58 from jcook3701/develop

Feat 021 (#57)

### 🐛 Fixed

- *(template)* Updates to template cookiecutter.json file.
- *(docs)* Fix for index file to ensure description doesn't mess with page header.

### 🚀 Added

- *(docs)* Fun emojis added to template readme.
## [0.1.0] - 2025-12-05

### ⚙️  Miscellaneous

- Initial commit
- Have a start of a chrome extension.
- Addding gitignore
- Just-the-docs-template
- Cookiecuter github docs
- Added footer and image-carousel
- Added CI and fixed directory format for cookiecuter.
- Lint and tests fixes
- Lint-fixes
- Ci tests fixes
- Ci tests fixes
- Merge pull request #1 from jcook3701/develop

Develop
- Put tests back because they are actually needed.
- Updates trying to ignore specific files for rendering
- Updates trying to ignore specific files for rendering
- Merge pull request #2 from jcook3701/develop

Develop
- Ready for testing.
- Ready for testing.
- Merge pull request #3 from jcook3701/develop

Develop
- Updates to index and readme.
- Merge pull request #4 from jcook3701/develop

updates to index and readme.
- Updates to gitignores and social-bar
- Merge pull request #5 from jcook3701/develop

updates to gitignores and social-bar
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Updates for social-bar.html
- Merge pull request #6 from jcook3701/develop

Develop
- Develop (#7)

* updated linting to avoid spiderwebing problems.  turned this into an actual python project with easy local testing.  updated ci/cd.  more to come.

* fixed linting errors and updates to cd/ci

* fixing linting and testing issues.

* fixes for ruff-linter
- Develop (#9)

* updated linting to avoid spiderwebing problems.  turned this into an actual python project with easy local testing.  updated ci/cd.  more to come.

* fixed linting errors and updates to cd/ci

* fixing linting and testing issues.

* fixes for ruff-linter

* added makefile to reduce makefile size of other projects. and updates to ci/cd

* updates to readme.

* updates to fix makefile.

* updates to fix makefile.

* Setup post gen hooks incase they are needed in the future.

* format fix.
- Develop (#10)

* updated linting to avoid spiderwebing problems.  turned this into an actual python project with easy local testing.  updated ci/cd.  more to come.

* fixed linting errors and updates to cd/ci

* fixing linting and testing issues.

* fixes for ruff-linter

* added makefile to reduce makefile size of other projects. and updates to ci/cd

* updates to readme.

* updates to fix makefile.

* updates to fix makefile.

* Setup post gen hooks incase they are needed in the future.

* format fix.

* readme update

* Small makefile updates
- Develop (#11)

* updated linting to avoid spiderwebing problems.  turned this into an actual python project with easy local testing.  updated ci/cd.  more to come.

* fixed linting errors and updates to cd/ci

* fixing linting and testing issues.

* fixes for ruff-linter

* added makefile to reduce makefile size of other projects. and updates to ci/cd

* updates to readme.

* updates to fix makefile.

* updates to fix makefile.

* Setup post gen hooks incase they are needed in the future.

* format fix.

* readme update

* Small makefile updates

* updates to project Makefiles and Gemfile.

---------

Co-authored-by: jcook3701 <jcook3701@gmail.com>
- Develop (#12)

* updated linting to avoid spiderwebing problems.  turned this into an actual python project with easy local testing.  updated ci/cd.  more to come.

* fixed linting errors and updates to cd/ci

* fixing linting and testing issues.

* fixes for ruff-linter

* added makefile to reduce makefile size of other projects. and updates to ci/cd

* updates to readme.

* updates to fix makefile.

* updates to fix makefile.

* Setup post gen hooks incase they are needed in the future.

* format fix.

* readme update

* Small makefile updates

* updates to project Makefiles and Gemfile.

* feat(build): CI/CD updates and major updates to use pre-commit, codespell, deptry, & pip-audit. Also setup configuration for git-cliff chanagelog generation.

---------

Co-authored-by: jcook3701 <jcook3701@gmail.com>
- Feat 01 (#13)

* feat(build): Updates to Makefile for changelog generation and future tag generation.

* docs(update): Updates to readme to make project easier for future users.

---------

Co-authored-by: jcook3701 <jcook3701@gmail.com>
- Merge pull request #14 from jcook3701/develop

Feat 01 (#13)
- Feat 02 (#15)

* docs(update): small build makefile updates along with updates for required packages in README.

* docs(readme): readme cleanup.

* docs(readme): readme cleanup.

* docs(readme): readme cleanup.

* build(makefile): Updates to makefile build.

---------

Co-authored-by: jcook3701 <jcook3701@gmail.com>
- Merge pull request #16 from jcook3701/develop

Develop

### 🐛 Fixed

- Fixes for repo name change

### 📚 Documentation

- *(readme)* Added extra make commands to documentation.

### 🚫 Removed

- Removed emacs backup
- Removed tests as they are not going to work with jekyll/liquid syntax .
- Removed hooks

### 🧪 Tests

- Testing symlink
- Testing symlink
- Testing symlink
- Testing symlink
- Testing symlink
- Testing symlink
- Testing symlink
- Testing symlink
- Testing symlink
- Testing symlink
- Tests test
- Tests test
- Tests test
- Tests test
- Tests test
- Tests test
