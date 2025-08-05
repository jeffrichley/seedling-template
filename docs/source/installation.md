# 📦 Installation Guide

> "The best time to plant a tree was 20 years ago. The second best time is now."
> — **Chinese Proverb**

Here’s how to install and set up the **Seedling** template so you can spend more time coding and less time duct-taping tools together. 🌱

---

## 🧰 Prerequisites

### Required

* **Python 3.11+** — Modern features + type hints
* **Git** — Version control
* **Copier** — Template engine (we’ll install it)

### Recommended

* **uv** — Fast Python package manager
* **Nox** — Task automation
* **Just** — Shortcut-friendly command runner *(optional but addictive)*

### Optional

* **pyenv** — Python version management
* **GitHub CLI** — For easy repo wrangling

---

## 🔧 Installing Required Tools

### 1 — Install uv *(recommended)*

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# pip fallback
pip install uv
```

### 2 — Install Copier

```bash
# With uv (recommended)
uv pip install copier

# With pip
pip install copier

# With pipx (isolated)
pipx install copier
```

### 3 — Install Nox *(recommended)*

```bash
# With uv
uv pip install nox

# With pip
pip install nox

# With pipx
pipx install nox
```

### 4 — Install Just *(optional, but highly recommended)*

```bash
# macOS
brew install just

# Linux
# Download from https://github.com/casey/just/releases or use your package manager

# Windows
choco install just
```

---

## 🌟 What the Template Provides

### ✅ **Already Included**

* Python deps: Black, Ruff, MyPy, pytest, Hypothesis, Sphinx…
* Pre-commit hooks
* Nox automation tasks
* Just command shortcuts
* GitHub Actions workflows

### 🔧 **You Install**

* Copier — Project generator
* uv — Dependency manager
* Nox — Automation runner
* Just — Command runner *(optional)*

---

## ✅ Verify Installation

```bash
copier --version
uv --version
nox --version
just --version   # optional
```

You should see version numbers (not error messages).

---

## ⚡ Quick Install Script

```bash
curl -LsSf https://raw.githubusercontent.com/jeffrichley/seedling/main/scripts/install-tools.sh | bash
```

What it does:

* Installs uv, Copier, Nox, Just
* Checks existing installs
* Prints next steps with pretty colors ✨

---

## 🛠️ Development Environment Setup

### 1 — Clone the Repo

```bash
git clone https://github.com/jeffrichley/seedling.git
cd seedling
```

### 2 — Python Environment

```bash
# pyenv
yenv install 3.11.0 && pyenv local 3.11.0

# uv
uv sync
```

### 3 — Dev Dependencies

```bash
uv sync --all-extras
# OR
pip install -e ".[dev]"
```

### 4 — Pre-commit Hooks

```bash
pre-commit install
```

---

## 🧪 Test the Installation

### 1 — Generate Test Project

```bash
copier copy . /tmp/test-project --trust
cd /tmp/test-project
```

### 2 — Verify

```bash
uv sync
nox -s tests
just quality
```

### 3 — Clean Up

```bash
rm -rf /tmp/test-project
```

---

## 🛠️ Troubleshooting

* **Copier not found** — `pip install copier`
* **uv missing** — `curl -LsSf https://astral.sh/uv/install.sh | sh`
* **Nox missing** — `pip install nox`
* **Just missing** — install from GitHub releases or your package manager
* **Python too old** — must be 3.11+
* **Permission errors** — use `--user` flag or a venv

See:

* [Copier Docs](https://copier.readthedocs.io/)
* [uv Docs](https://docs.astral.sh/uv/)
* [Nox Docs](https://nox.thea.codes/)
* [Just Docs](https://just.systems/)

---

## 🌱 Next Steps

1. Generate your first project → {doc}`quickstart`
2. Learn configuration → {doc}`configuration`
3. Explore examples → {doc}`examples`
4. Customize the template to your needs
