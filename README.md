# 🌱 Seedling – Modern Python Project Template

> “Any fool can write code that a computer can understand.
> Good programmers write code that humans can understand.”
> — **Martin Fowler**

[![Template](https://img.shields.io/badge/template-copier-brightgreen?logo=copier)](https://github.com/copier-org/copier)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![pre‑commit enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit\&logoColor=white)](https://github.com/pre-commit/pre-commit)

Seedling is the **“just add water”** template for modern Python projects: batteries included, CI wired up, quality gates armed, and zero yak‑shaving required. Clone it, answer a few prompts, and you’re sprinting instead of scaffolding. 🌱✨

---

## 🚀 Quick Start (Minimal Installation)

*Just want to sprout a fresh project without installing the whole tool garden? This path’s for you.*

> “Automation: because typing the same command twice is a bug.” — *Every sane developer ever*

### 1 ⎯ Install Copier

```bash
# Using uv (recommended – faster than a double espresso)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv pip install copier

# Using pip (your call)
pip install copier
```

### 2 ⎯ Generate Your Project

```bash
# Interactive prompts
copier copy https://github.com/jeffrichley/seedling-template.git my-awesome-project

# Fully non‑interactive (CI‑friendly)
copier copy https://github.com/jeffrichley/seedling-template.git my-awesome-project \
  --data-file project-data.yaml
```

Boom. 🌟 Your new repo is ready, complete with a **Getting Started** guide inside.

### 📜 Example `project-data.yaml`

```yaml
project_name: "My Awesome Project"
project_slug: "my_awesome_project"
project_description: "A modern Python project built with best practices"
author_name: "Your Name"
author_email: "your.email@example.com"
github_username: "yourusername"
license: "MIT"
python_versions: "3.11,3.12"
coverage_threshold: 80
```

---

## 🛠️ Full Installation (For Working Inside Generated Projects)

Ready to wield the *full* Seedling toolbox? Follow the white rabbit 🐇.

### 1 ⎯ Install All Required Tools

```bash
# One‑liner to grab everything
curl -LsSf https://raw.githubusercontent.com/jeffrichley/seedling-template/main/scripts/install-tools.sh | bash

# Manual route (choose your own adventure)
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
uv pip install copier
uv pip install nox

```

### Install Just (command runner)

- **macOS**: `brew install just`
- **Linux**: download the binary from the [releases](https://github.com/casey/just/releases) page and add it to your `PATH`
- **Windows**: `choco install just`


### 2 ⎯ Generate Your Project *(same as above)*

```bash
# Interactive prompts
copier copy https://github.com/jeffrichley/seedling-template.git my-awesome-project

# Non‑interactive (CI‑friendly)
copier copy https://github.com/jeffrichley/seedling-template.git my-awesome-project \
  --data-file project-data.yaml
```

💡 **Pro tip:** Need an example data file? See [project-data.yaml](#📜-example-project-datayaml).

### 3 ⎯ Start Developing

```bash
cd my-awesome-project
uv sync                 # Install dependencies
uv run dev test         # Run tests 🧪
uv run dev docs         # Build docs 📚
```

---

## 📚 Documentation

### Building the Documentation

The project includes comprehensive documentation built with Sphinx and the Furo theme. Here's how to generate and serve it:

#### Quick Build
```bash
cd docs
uv sync                 # Install documentation dependencies
uv run make html        # Build HTML documentation
```

#### Build and Serve Locally
```bash
cd docs
uv sync                 # Install documentation dependencies
uv run make html        # Build HTML documentation
uv run make serve       # Serve at http://localhost:8000
```

#### Alternative: Use the Build Script
```bash
./docs/build-docs.sh    # Builds docs and provides serving instructions
```

#### Manual Build Steps
```bash
cd docs
uv sync                 # Install dependencies from docs/pyproject.toml
uv run sphinx-build -b html source build/html
```

The built documentation will be available in `docs/build/html/`. Open `index.html` in your browser to view it locally.

### Documentation Structure
- **API Reference**: Auto-generated from your code's docstrings
- **User Guide**: Step-by-step tutorials and examples
- **Architecture Decisions**: ADRs in `docs/source/adr/`
- **Contributing Guide**: Development setup and guidelines

---

## ✨ Features at a Glance

| Category            | Goodies                                            |
| ------------------- | -------------------------------------------------- |
| **Modern Python**   | 3.11 +, `uv`, type hints everywhere                |
| **Quality Tooling** | Black, Ruff, MyPy, pre‑commit hooks                |
| **Testing**         | pytest + coverage, Hypothesis for property testing |
| **Docs**            | Sphinx + Furo theme, auto API docs                 |
| **CI/CD**           | GitHub Actions with lint/type/coverage gates       |
| **Security**        | pip‑audit & dep scanning                           |
| **DX**              | Nox tasks + Just command shortcuts                 |

> “Simplicity is the soul of efficiency.” — **Austin Freeman**

---

## 🛠️ Installation Matrix

### Minimal (Project Creation Only)

* **Copier** → `uv pip install copier` *(or `pip install copier`)*

### Full (Dev Environment)

* **uv** – fast package manager / venv wizard
  Install: `curl -LsSf https://astral.sh/uv/install.sh | sh`
* **Copier** – project generator
  Install: `uv pip install copier`
* **Nox** – task orchestrator
  Install: `uv pip install nox`
* **Just** – friendly task aliases
  Install: see [https://just.systems](https://just.systems)

---

## 🎯 What the Template Plants in Your Repo

<details>
<summary>Click to peek 👀</summary>

```
my-awesome-project/
├── src/my_awesome_project/     # Your package code
├── tests/                      # Unit ▸ Integration ▸ E2E
├── docs/                       # Sphinx site
├── .github/                    # CI workflows
├── pyproject.toml              # Single source of truth
├── .pre-commit-config.yaml     # Quality gatekeepers
├── noxfile.py                  # Automated tasks
├── justfile                    # Convenience aliases
└── README.md                   # (This file!)
```

</details>

---

## 🤝 Contributing

We love PRs, coffee, and good commit messages. Start with **`docs/contributing.md`** for process & etiquette.

---

## 🔧 Troubleshooting 101

### Template generation fails

```bash
# Update Copier to latest
uv pip install --upgrade copier

# Run with verbose output to see what tripped
copier copy https://github.com/jeffrichley/seedling-template.git my-project --trust -v
```

### Dependencies won’t install

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # Ensure uv exists
uv cache clean                                    # Nuke cache gremlins
```

### Tests are grumpy

```bash
uv sync --all-extras     # Ensure full dependency graph
uv run pytest -v         # Run with verbose to pinpoint failures
```

Need more? Hit **Issues** or **Discussions** on GitHub and we’ll get you sorted. 💬

---

## 📄 License

Seedling is MIT‑licensed. Use it, fork it, build the next big thing — just don’t blame us if you become allergic to boilerplate. 😉
