# 📚 Examples

> "The best way to learn is by doing."
> — **Paul Halmos**

Want to see **Seedling** sprout in different soils? Here are ready-to-run configurations and project structures so you can skip the guesswork and get building. 🌱

---

## 🏗 Project Types

### Basic Python Package

Minimal and clean — ideal for simple libraries or utilities.

```bash
copier copy https://github.com/jeffrichley/seedling.git my-package \
  --data project_name="My Package" \
  --data project_slug="my_package" \
  --data project_description="A simple Python package" \
  --data author_name="Your Name" \
  --data author_email="your.email@example.com" \
  --data github_username="yourusername" \
  --data license="MIT" \
  --data python_versions="3.11,3.12"
```

**Result** → Basic Python package scaffold with quality tooling baked in.

### CLI Application

For command-line tools that mean business.

```bash
copier copy https://github.com/jeffrichley/seedling.git my-cli-app \
  --data project_name="My CLI App" \
  --data project_slug="my_cli_app" \
  --data project_description="A command-line interface application" \
  --data include_cli=true \
  --data license="Apache-2.0" \
  --data python_versions="3.12"
```

**Result** → CLI-ready structure with argument parsing and entry points.

### Data Science Project

Purpose-built for ML pipelines and data analysis.

```bash
copier copy https://github.com/jeffrichley/seedling.git my-ml-project \
  --data project_name="ML Pipeline" \
  --data project_slug="ml_pipeline" \
  --data project_description="A machine learning pipeline for data analysis" \
  --data project_keywords="machine-learning,data-science,python,pipeline" \
  --data coverage_threshold=75 \
  --data license="MIT" \
  --data python_versions="3.11,3.12"
```

**Result** → Data science setup with tests, docs, and quality gates.

### Enterprise Library

Production-grade, policy-compliant, and rock-solid.

```bash
copier copy https://github.com/jeffrichley/seedling.git enterprise-lib \
  --data project_name="Enterprise Library" \
  --data project_slug="enterprise_library" \
  --data project_description="A comprehensive enterprise-grade Python library" \
  --data project_keywords="enterprise,library,python,api,rest" \
  --data author_name="Your Full Name" \
  --data author_email="your.full.name@company.com" \
  --data github_username="yourusername" \
  --data copyright_year="2024" \
  --data version="1.0.0" \
  --data license="Apache-2.0" \
  --data python_versions="3.11,3.12,3.13" \
  --data coverage_threshold=95 \
  --data include_cli=true \
  --data enable_conda_fallback=true
```

**Result** → Enterprise-ready template with strict quality enforcement.

---

## 🗂 Configuration Files

### Minimal Config

```yaml
project_name: "Minimal Project"
project_slug: "minimal_project"
project_description: "A minimal Python project"
author_name: "Your Name"
author_email: "your.email@example.com"
github_username: "yourusername"
license: "MIT"
python_versions: "3.11"
coverage_threshold: 80
```

Usage:

```bash
copier copy https://github.com/jeffrichley/seedling.git my-project --data-file minimal-config.yaml
```

### Full Config

```yaml
project_name: "Enterprise Library"
project_slug: "enterprise_library"
project_description: "A comprehensive enterprise-grade Python library with full CI/CD, documentation, and quality tooling"
project_keywords: "enterprise,library,python,api,rest"
author_name: "Your Full Name"
author_email: "your.full.name@company.com"
github_username: "yourusername"
copyright_year: "2024"
version: "1.0.0"
license: "Apache-2.0"
python_versions: "3.11,3.12,3.13"
coverage_threshold: 95
```

Usage:

```bash
copier copy https://github.com/jeffrichley/seedling.git my-project --data-file full-config.yaml
```

---

## 📂 Generated Project Examples

### Basic Package Structure

```
my-package/
├── src/my_package/
├── tests/
├── docs/
├── .github/
├── pyproject.toml
├── .pre-commit-config.yaml
├── noxfile.py
├── README.md
└── LICENSE
```

### CLI Application Structure

```
my-cli-app/
├── src/my_cli_app/
├── tests/
├── docs/
├── .github/
├── pyproject.toml
├── .pre-commit-config.yaml
├── noxfile.py
├── README.md
└── LICENSE
```

---

## 🔄 Post-Generation Workflows

### Basic Dev Loop

```bash
uv sync
pre-commit install
uv run dev checkit
uv run dev test
uv run dev format
uv run dev docs
```

### CI/CD Goodies

* **CI**: Tests & checks on every push/PR
* **Release**: Automated semantic releases
* **Security**: Dependency scanning
* **Docs**: Auto-deploy to GitHub Pages

### Quality Gates

* Formatting: Black & isort
* Linting: Ruff
* Typing: MyPy
* Coverage: Threshold enforcement
* Security: pip-audit

---

## 🛠 Customization Examples

### Adding Dependencies

```toml
[project]
dependencies = [
    "requests>=2.28.0",
    "pandas>=1.5.0",
    "numpy>=1.24.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "black>=23.0.0",
]
```

### Custom GitHub Actions

```yaml
name: Custom Workflow
on: [push, pull_request]
jobs:
  custom:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Custom workflow"
```

### Custom Docs

```markdown
# Custom Documentation
Add your project-specific documentation here.
```

---

## 💡 Contributing Examples

Got a great setup? Submit a PR with:

1. A config file
2. A short use-case description
3. Generated project tree
4. Post-generation steps
