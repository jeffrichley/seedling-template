# 🌱 Seedling – Changelog

> "Progress is impossible without change, and those who cannot change their minds cannot change anything."
> — **George Bernard Shaw**

This log tracks every sprout, prune, and bloom in the Seedling template garden. We follow **[Keep a Changelog](https://keepachangelog.com/en/1.0.0/)** and **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**—but we’re not above dropping the occasional emoji when a release really slaps. 💃🕺

---

## \[0.1.0] – 2025‑08‑04

### Added

* **Initial stable release** of the Seedling Python project template
* **Complete CI/CD pipeline** with GitHub Actions workflows

  * Automated testing with `pytest` and coverage reporting
  * Code quality checks with **Ruff**, **Black**, and **MyPy**
  * Documentation building and deployment
  * Security scanning with CodeQL
  * Automated releases with semantic‑release
* **Modern Python tooling** integration

  * **uv** package manager for fast dependency management
  * **Nox** for task automation and multi‑environment testing
  * **Just** command runner for development shortcuts
  * **Sphinx** documentation with the Furo theme
* **Quality assurance** features

  * Pre‑commit hooks for code quality
  * Comprehensive linting and formatting
  * Type checking with MyPy
  * Security auditing with `pip-audit`
  * Complexity analysis with Radon
* **Professional documentation** setup

  * Sphinx docs with dark‑mode goodness
  * Automatic API documentation generation
  * GitHub Pages deployment
* **Template configuration** system

  * 15+ configurable template variables
  * Support for Python 3.11 +
  * Choice of license (MIT, Apache‑2.0, GPL‑3.0, BSD‑3‑Clause)
  * Customizable test‑coverage thresholds
* **Development workflow** tools

  * Full test scaffold (unit ▸ integration ▸ e2e)
  * Dev‑environment bootstrap scripts
  * Automated dependency updates
  * Git hooks + pre‑commit integration
* **Template documentation & guides**

  * Step‑by‑step usage walkthrough
  * Example project types (CLI, library, web app)
  * Configuration best practices
  * Troubleshooting guide
  * Template variable reference

### Changed

* **Branding**: Swapped Vine‑specific references for Seedling branding
* **CSS classes**: `.vine-highlight` → `.seedling-highlight`
* **Docs**: Beefed up with richer examples and screenshots
* **README**: Now wears professional badge bling 🏅

### Infrastructure

* **Repo setup**: Full GitHub repo bootstrap
* **Branch protection**: Main branch locked with required reviews
* **Issue templates**: Bug & feature templates
* **Pull‑request template**: Standardized PR checklist
* **Labels**: Comprehensive issue‑label set

### Release Notes

This debut release bundles everything you need to spin up **world‑class** Python projects with zero yak‑shaving.

---

## \[Unreleased]

### Planned

* Additional project‑type templates (FastAPI, ML Pipeline, etc.)
* Enhanced customization options via Copier prompts
* Community‑contributed examples
* Performance optimizations
* Extended documentation (FAQ, deep‑dive tutorials)
