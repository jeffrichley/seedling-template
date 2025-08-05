# 🌱 Seedling Template Guide

> "Give me six hours to chop down a tree and I will spend the first four sharpening the axe."
> — **Abraham Lincoln**

Welcome, planter of projects! This guide is your **sharpened axe**—showing you exactly how to sprout, nurture, and prune a world‑class Python repository using the Seedling template.

---

## 🌟 Why Seedling?

Seedling is a **Copier‑powered generator** that gives you:

| 🌱                       | What You Get                                                   | Why You’ll Love It                                        |
| ------------------------ | -------------------------------------------------------------- | --------------------------------------------------------- |
| **CI/CD, pre‑wired**     | GitHub Actions for tests, lint, type‑check, docs, and releases | Automated confidence, zero yak‑shaving                    |
| **Modern tooling**       | `uv`, Nox, Just, Black, Ruff, MyPy                             | Fast installs, one‑command dev tasks, opinionated quality |
| **Docs that don’t suck** | Sphinx + Furo (dark‑mode ready)                                | Because READMEs alone won’t cut it                        |
| **Enterprise hygiene**   | Pre‑commit hooks, security scanning, semantic‑release          | Impress your CTO *and* future you                         |

> 💡 **Tip:** Run `just` (generated project) to see all available dev shortcuts.

---

## 🚀 Quick Start

### 1 — Install Copier (minimal path)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # install uv
uv pip install copier                             # install Copier via uv
```

### 2 — Generate Your Project

```bash
# Interactive prompts
copier copy https://github.com/jeffrichley/seedling-template.git my-new-project

# Zero‑prompt (CI‑friendly)
copier copy https://github.com/jeffrichley/seedling-template.git my-new-project \
  --data-file project-data.yaml
```

Need an example data file? See [project-data.yaml](#📜-example-project-datayaml).

### 3 — Dive In

```bash
cd my-new-project
uv sync                 # install deps
uv run dev test         # run tests
uv run dev docs         # build docs
```

---

### 🧩 Template Variables & Prompts (12 total)

| # | Prompt (variable)        | What it controls                              | Example value |
|---|--------------------------|-----------------------------------------------|---------------|
| 1 | **Project Name**        (`project_name`)        | Human-friendly display name used in docs and metadata | `Data Wizard` |
| 2 | **Project Slug**        (`project_slug`)        | Import-safe package folder (lowercase, underscores) | `data_wizard` |
| 3 | **Project Description** (`project_description`) | Short tagline shown in README, `pyproject`, and PyPI | `A modern Python data toolkit` |
| 4 | **Project Keywords** (`project_keywords`) | Comma-separated keywords used in `pyproject.toml` for package metadata and search SEO | `ai, automation, audio` |
| 5 | **Author Name**         (`author_name`)         | Primary maintainer’s name for docs & license header | `Jane Doe` |
| 6 | **Author Email**        (`author_email`)        | Contact e-mail baked into `pyproject` metadata | `jane@example.com` |
| 7 | **GitHub Username**     (`github_username`)     | Used to craft repo URLs and badge links            | `janedoe` |
| 8 | **Copyright Year** (`copyright_year`)    | Year injected into the `LICENSE` file and doc headers | `2025` |
| 9 | **Version** (`version`) | Initial semantic version pinned in `pyproject.toml`, shown in badges & release tags | `0.1.0` |
| 10 | **License**             (`license`)             | SPDX ID dropped into `LICENSE` and `pyproject`     | `MIT` |
| 11 | **Python Versions**     (`python_versions`)     | Comma-separated list for CI matrix & `pyproject`   | `3.11,3.12` |
| 12 | **Coverage Threshold**  (`coverage_threshold`)  | Minimum % before CI fails                          | `80` |

---

## 🔧 Configuration Best Practices

### Naming

* **Slug first** – Make sure import path (`project_slug`) is short & unique.
* **Display Name** – Keep spaces & capitalisation; shown in docs/pyproject metadata.

### Python Matrix

* Pin two recent versions (e.g. 3.11 + 3.12); drop EOL ones early.
* Slide new minors in after they hit *stable* status.

### Dependency Strategy

* Runtime deps → `dependencies=` in `pyproject.toml`.
* Dev‑only deps → `group.dev.dependencies=` (keeps lean installs).

> 🔬 **Science says:** Smaller dependency graphs reduce supply‑chain risk.

### Testing

* **Unit** for business logic, **integration** for boundary layers, **e2e** for user flows.
* Use **pytest‑cov** + `just coverage-html` to eyeball blind spots.
* Hypothesis for property‑based fuzzing—catch those sneaky edge cases.

### Documentation

* Break up long tutorials; keep one topic per page.
* Use literal‑include to pull code blocks directly from source—no drift.
* Run `nox -s docs-linkcheck` before publishing; broken links are bad optics.

---

## 📜 Example project-data.yaml

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

## 🏗️ Post‑Generation Checklist

1. `cd my-new-project`
2. Run `uv sync` (installs all extras)
3. Initialise git: `git init && git add . && git commit -m "seedling: first sprout"`
4. Push to GitHub; branch protection rules FTW.
5. Enable GitHub Pages under **Settings → Pages** (docs will auto‑publish).

> 🛟 **Safety net:** Commit often; you can always prune branches—resurrecting lost work is harder.

---

## 🚑 Troubleshooting

| Symptom                               | Fix                                               |
| ------------------------------------- | ------------------------------------------------- |
| Copier fails with cryptic Jinja error | Upgrade Copier: `uv pip install --upgrade copier` |
| `uv sync` takes ages                  | Clear cache: `uv cache clean`                     |
| CI coverage < threshold               | Run `just coverage-html` → find gaps              |

Still stuck? File an issue—no reasonable question refused (unreasonable ones welcome if entertaining). 😎

---

## 🎉 Success Stories

- **The 10-Minute MVP:** A team scaffolded a service, shipped a working API before their coffee cooled, and then spent the rest of the stand-up debating Furo dark mode. Priorities. ☕️
- **CI Whisperer:** Someone pushed a fresh Seedling repo and the pipeline went green on the first try. Their manager accused them of faking screenshots. They did not. ✅
- **Yak-Free Weekend:** A side project launched without writing a new Makefile. Yaks remained gloriously unshaved. 🐃✂️🚫
- **Docs Convert:** A README skeptic built the Sphinx site and filed their first-ever docs PR. We printed it and put it on the fridge. 🧲
- **Lint Lottery Win:** Adopting the pre-commit config surfaced a sneaky bug. The bounty was paid in donuts. 🍩
- **The Great Rename:** Thanks to `project_slug`, a team avoided shipping `import project`. Future-you says thanks.

> “Results may vary. Side effects include faster pipelines, cleaner diffs, and sudden urges to write tests.”

Ready to add your legend? Plant your seed and tell us what grew.


---

## 🤝 Contributing to Seedling

* Fork → feature branch → PR
* Pass **all** Nox sessions: `nox -s tests lint type_check docs`
* Write docs for new features; we break hearts over undocumented magic.

See [Contributing Guide](../CONTRIBUTING.md) for the full ritual.

---

**Seedling** – Growing world‑class Python projects from the ground up. 🌱
