# 🤝 Contributing to Seedling

> "Alone we can do so little; together we can do so much."
> — **Helen Keller**

Thanks for wanting to help grow **Seedling**! 🌱 This guide lays out how to get set up, keep quality sky‑high, and land your changes smoothly. Expect clear steps, a dash of sass, and no broken builds. 😉

---

## 📜 Code of Conduct

By joining in, you agree to help maintain a respectful, inclusive, and welcoming space for everyone. Our community thrives when people feel safe and inspired.

---

## 🛠️ Development Setup

### Prerequisites

* **Python 3.11+** — Modern features + type hints
* **uv** — Fast Python package manager *(recommended)*
* **Git** — Version control
* **Copier** — Template engine for local testing

### Installation

```bash
# Clone the repository
git clone https://github.com/jeffrichley/seedling.git
cd seedling

# Install dependencies
uv sync
```

💡 **Tip:** If you don’t have `uv`, grab it from [uv install docs](https://docs.astral.sh/uv/).

---

## 📚 Documentation

### Building Documentation

We keep docs comprehensive and locally buildable.

#### Prerequisites

* **uv** — Fast Python package manager
* **Sphinx** — Documentation generator

#### Quick Build

```bash
cd docs
./build-docs.sh
```

#### Manual Build

```bash
cd docs
uv sync        # Install doc deps
make html      # Build HTML
make serve     # Serve locally
```

Your docs will be live at **[http://localhost:8000](http://localhost:8000)**.

#### Structure

```
docs/
├── source/            # Source files (Markdown/MyST)
├── build/             # Generated output
├── pyproject.toml     # Doc dependencies
├── Makefile           # Build targets
└── build-docs.sh      # Build script
```

#### Adding New Docs

1. Create a file under `docs/source/`
2. Use `.md` with MyST syntax
3. Update `docs/source/index.md` navigation if needed
4. Build & verify locally
5. Match existing style

---

## 🧪 Testing Template Generation

When editing the template, always ensure it still generates valid projects.

```bash
copier copy . /tmp/test-project --trust
cd /tmp/test-project
uv sync
uv run dev test
uv run dev checkit
cd .. && rm -rf /tmp/test-project
```

---

## 🎯 Quality Requirements

All contributions must pass these gates:

1. **Linting** — Ruff, zero warnings
2. **Type Safety** — MyPy strict, zero errors
3. **Coverage** — ≥80%
4. **Complexity** — Xenon‑approved maintainability
5. **Dead Code** — None (Vulture)
6. **Security** — No vulns (pip‑audit)

### Pre‑commit Checks

```bash
# All checks
uv run dev checkit

# Individual checks
uv run dev lint
uv run dev typecheck
uv run dev test
uv run dev quality-gates
```

---

## 🔄 Contribution Process

### 1. Fork & Clone

```bash
git clone https://github.com/YOUR_USERNAME/seedling.git
cd seedling
git remote add upstream https://github.com/jeffrichley/seedling.git
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/short-bug-description
```

### 3. Make Changes

* Follow code style guidelines
* Add tests for new features
* Update docs where relevant
* Test template generation

### 4. Test Everything

```bash
uv run dev checkit
copier copy . /tmp/test-project --trust
# ...verify build/tests, then clean up
```

### 5. Commit & Push

```bash
git add .
git commit -m "feat: add amazing new feature"
git push origin feature/your-feature-name
```

### 6. Open a PR

* Describe changes clearly
* Link related issues
* Include screenshots for UI changes
* Confirm template generation works

---

## 📝 Code Style Guidelines

### Python Code

* PEP 8 + Black formatting
* Type hints everywhere
* Docstrings for public functions
* Small, focused functions
* Descriptive variable names

### Template Files

* Clear, descriptive variable names
* Comment tricky Jinja2 logic
* Test generation with varied configs
* Keep it maintainable

### Documentation

* Clear, concise, consistent
* Code examples where useful
* Verify all links
* Match existing style

---

## 🧪 Testing Requirements

### Template

* Multiple configs
* Verify builds
* Check all tools
* Test edge cases

### Documentation

* Build locally
* Check links
* Run examples
* Test search

---

## 👀 Review Process

1. Automated checks pass
2. Template generation verified
3. Docs updated
4. Maintainer code review
5. Final tests before merge

---

## 🆘 Getting Help

* Search GitHub issues
* Read the docs
* Ask in Discussions
* Join our community chat

---

## 📄 License

By contributing, you agree your work will be MIT‑licensed.
