# ⚙️ Configuration Guide

> "By failing to prepare, you are preparing to fail."
> — **Benjamin Franklin**

This guide covers every configurable option in the **Seedling** template so you can shape your project exactly how you want it. 🌱

---

## 🧩 Template Variables & Prompts (12 total)

| #  | Prompt (variable)                               | What it controls                                                                      | Example value                  |
| -- | ----------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------ |
| 1  | **Project Name**        (`project_name`)        | Human-friendly display name used in docs and metadata                                 | `Data Wizard`                  |
| 2  | **Project Slug**        (`project_slug`)        | Import-safe package folder (lowercase, underscores)                                   | `data_wizard`                  |
| 3  | **Project Description** (`project_description`) | Short tagline shown in README, `pyproject`, and PyPI                                  | `A modern Python data toolkit` |
| 4  | **Project Keywords** (`project_keywords`)       | Comma-separated keywords used in `pyproject.toml` for package metadata and search SEO | `ai, automation, audio`        |
| 5  | **Author Name**         (`author_name`)         | Primary maintainer’s name for docs & license header                                   | `Jane Doe`                     |
| 6  | **Author Email**        (`author_email`)        | Contact e-mail baked into `pyproject` metadata                                        | `jane@example.com`             |
| 7  | **GitHub Username**     (`github_username`)     | Used to craft repo URLs and badge links                                               | `janedoe`                      |
| 8  | **Copyright Year** (`copyright_year`)           | Year injected into the `LICENSE` file and doc headers                                 | `2025`                         |
| 9  | **Version** (`version`)                         | Initial semantic version pinned in `pyproject.toml`, shown in badges & release tags   | `0.1.0`                        |
| 10 | **License**             (`license`)             | SPDX ID dropped into `LICENSE` and `pyproject`                                        | `MIT`                          |
| 11 | **Python Versions**     (`python_versions`)     | Comma-separated list for CI matrix & `pyproject`                                      | `3.11,3.12`                    |
| 12 | **Coverage Threshold**  (`coverage_threshold`)  | Minimum % before CI fails                                                             | `80`                           |

---

## 📂 Configuration Examples

### Basic Python Package

```yaml
project_name: "My Package"
project_slug: "my_package"
project_description: "A simple Python package"
author_name: "Your Name"
author_email: "your.email@example.com"
github_username: "yourusername"
license: "MIT"
python_versions: "3.11,3.12"
coverage_threshold: 80
```

### CLI Application

```yaml
project_name: "My CLI App"
project_slug: "my_cli_app"
project_description: "A command-line interface application"
author_name: "Your Name"
author_email: "your.email@example.com"
github_username: "yourusername"
license: "Apache-2.0"
python_versions: "3.12"
coverage_threshold: 85
include_cli: true
```

### Enterprise Library

```yaml
project_name: "Enterprise Library"
project_slug: "enterprise_library"
project_description: "A comprehensive enterprise-grade Python library"
project_keywords: "enterprise,library,python,api,rest"
author_name: "Your Full Name"
author_email: "your.full.name@company.com"
github_username: "yourusername"
copyright_year: "2024"
version: "1.0.0"
license: "Apache-2.0"
python_versions: "3.11,3.12,3.13"
coverage_threshold: 95
include_cli: true
enable_conda_fallback: true
```

---

## ⚙️ Using Configuration Files

### Method 1 — Interactive Prompts

```bash
copier copy https://github.com/jeffrichley/seedling.git my-project
# Answer prompts interactively
```

### Method 2 — Data File

```yaml
# my-config.yaml
project_name: "My Project"
project_slug: "my_project"
project_description: "My awesome project"
author_name: "Your Name"
author_email: "your.email@example.com"
github_username: "yourusername"
license: "MIT"
python_versions: "3.11,3.12"
coverage_threshold: 85
```

```bash
copier copy https://github.com/jeffrichley/seedling.git my-project --data-file my-config.yaml
```

### Method 3 — Command Line Arguments

```bash
copier copy https://github.com/jeffrichley/seedling.git my-project \
  --data project_name="My Project" \
  --data project_slug="my_project" \
  --data author_name="Your Name" \
  --data license="MIT"
```

---

## 🧪 Validation Rules

* **Python Versions**: Comma-separated list, valid Python version numbers, at least one required.
* **Coverage Threshold**: Integer 0–100, used in CI/CD gates.
* **Project Slug**: Lowercase letters, numbers, underscores only.

---

## 🔄 Post-Generation Configuration

Update the template:

```bash
cd my-project
copier update
```

Override a setting:

```bash
copier update --data coverage_threshold=90
```

Skip specific files:

```bash
copier update --skip .github/workflows/ci.yml
```

---

## 🔒 Environment Variables

For sensitive data:

```bash
export SEEDLING_AUTHOR_EMAIL="your.email@example.com"
export SEEDLING_GITHUB_USERNAME="yourusername"

copier copy https://github.com/jeffrichley/seedling.git my-project
```

---

## 🌱 Best Practices

1. Use descriptive names
2. Choose licenses intentionally
3. Set realistic coverage targets (start at 80%)
4. Commit configuration files for reproducibility
5. Keep them under version control

---

## 🛟 Troubleshooting

* **Invalid slug** — lowercase letters, numbers, underscores only
* **Bad Python version format** — e.g., `3.11,3.12`
* **Coverage threshold invalid** — must be 0–100

See the {doc}`examples` page for more working configs.
