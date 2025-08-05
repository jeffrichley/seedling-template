# 🚀 Quick Start Guide

> "Give me six hours to chop down a tree and I will spend the first four sharpening the axe."
> — **Abraham Lincoln**

Get up and running with **Seedling** in under 5 minutes! 🌱 This guide walks you through the essentials so you can start coding instead of configuring.

---

## 🧰 Prerequisites

* **Python 3.11+** — Modern language features & type hints
* **Git** — Version control (because you *will* want history)
* **Copier** — Template engine (we’ll install it)
* **uv** — Fast Python package manager *(recommended)*
* **Nox** — Task automation *(recommended)*
* **Just** — Command runner for shortcuts *(optional, but addictive)*

---

## 📦 Installation

### 1 — Install Required Tools

```bash
# One-stop shop (recommended)
curl -LsSf https://raw.githubusercontent.com/jeffrichley/seedling/main/scripts/install-tools.sh | bash

# Or roll your own
curl -LsSf https://astral.sh/uv/install.sh | sh
uv pip install copier
uv pip install nox
```

**Install Just** (command runner)

* **macOS**: `brew install just`
* **Linux**: download binary from [releases](https://github.com/casey/just/releases) and add to `PATH`
* **Windows**: `choco install just`

---

### 2 — Generate Your First Project

```bash
copier copy https://github.com/jeffrichley/seedling-template.git my-awesome-project
```

You’ll be prompted for config:

```
project_name [My Awesome Project]: My Data Science Tool
project_slug [my_awesome_project]: my_data_science_tool
project_description [A modern Python project built with best practices]: A powerful data science toolkit
author_name [Your Name]: Jane Doe
author_email [your.name@example.com]: jane.doe@example.com
github_username [yourusername]: janedoe
license (MIT, Apache-2.0, GPL-3.0, BSD-3-Clause) [MIT]: MIT
python_versions [3.11,3.12]: 3.11,3.12
coverage_threshold [80]: 85
```

---

### 3 — Navigate to Your Project

```bash
cd my-awesome-project
```

### 4 — Set Up Development Environment

```bash
uv sync            # Install dependencies
pre-commit install # Activate hooks
just quality       # Run initial quality sweep
```

### 5 — Start Developing!

```bash
nox -s tests   # via Nox (recommended)
just test      # via Just
just lint      # Format & lint
just docs      # Build docs
```

---

## 🎯 What Just Happened?

1. **Project Structure** — Ready-to-go Python scaffolding
2. **Dependencies** — Installed & configured
3. **Quality Tools** — Hooks, linting, tests in place
4. **CI/CD** — GitHub Actions locked & loaded
5. **Docs** — Sphinx site bootstrapped

---

## 📁 Your New Project Structure

```
my-awesome-project/
├── src/my_data_science_tool/    # Your package code
├── tests/                       # Unit ▸ Integration ▸ E2E
├── docs/                        # Documentation
├── .github/                     # CI workflows
├── pyproject.toml               # Config central
├── .pre-commit-config.yaml      # Quality rules
├── noxfile.py                   # Automation scripts
├── justfile                     # Command shortcuts
└── README.md                    # Project overview
```

---

## 🛠️ Available Commands

### Using **Nox**

```bash
nox -s tests        # Run tests
nox -s lint         # Lint code
nox -s type_check   # Type checking
nox -s docs         # Build docs
nox -s lint type_check docs # All checks
```

### Using **Just**

```bash
just test       # Tests
just lint       # Lint
just type-check # Type checking
just docs       # Docs
just quality    # All checks
```

### Using **uv** Directly

```bash
uv sync
uv run pytest
uv run black src tests
uv run ruff check src tests --fix
uv run mypy src tests
```

---

## 🎯 What the Template Provides

### ✅ **Automatically Included**

* Python deps: Black, Ruff, MyPy, pytest, Sphinx, etc.
* Pre-commit hooks
* Nox automation
* Just shortcuts
* GitHub Actions CI/CD
* Complete test scaffold
* Docs with Sphinx + Furo

### 🔧 **What You Install**

* Copier — Project generator
* uv — Dependency manager
* Nox — Task automation
* Just — Shortcuts *(optional)*

---

## 🌱 Next Steps

* **Read the docs** — Peek into the `docs/` folder
* **Customize configs** — Edit `pyproject.toml` & friends
* **Add code** — Start in `src/my_data_science_tool/`
* **Write tests** — Keep `tests/` healthy
* **Deploy** — Push to GitHub; CI/CD takes it from there

For more details, see the {doc}`installation` and {doc}`configuration` guides.
