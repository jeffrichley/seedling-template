# 🌱 Seedling - Modern Python Project Template

[![Template](https://img.shields.io/badge/template-copier-brightgreen?logo=copier)](https://github.com/copier-org/copier)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![pre-commit enabled](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

A comprehensive Python project template with modern development tooling, automated CI/CD, and best practices built-in.

## 🚀 Quick Start

### Step 1: Install Required Tools

```bash
# Quick install all required tools
curl -LsSf https://raw.githubusercontent.com/jeffrichley/seedling-template/main/scripts/install-tools.sh | bash

# Or install manually
curl -LsSf https://astral.sh/uv/install.sh | sh
uv pip install copier
uv pip install nox
```

### Step 2: Generate Your Project

```bash
# Generate with interactive prompts
copier copy https://github.com/jeffrichley/seedling-template.git my-awesome-project

# Or use a data file for non-interactive generation
copier copy https://github.com/jeffrichley/seedling-template.git my-awesome-project --data-file project-data.yaml
```

### Step 3: Start Developing

```bash
cd my-awesome-project
uv sync                    # Install dependencies
uv run dev test           # Run tests
uv run dev docs           # Build documentation
```

### Example Data File (`project-data.yaml`)

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

## ✨ Features

- **Modern Python Setup**: Python 3.11+, uv package manager, type hints
- **Quality Tooling**: Black, Ruff, MyPy, pre-commit hooks
- **Testing**: pytest with coverage, hypothesis for property-based testing
- **Documentation**: Sphinx with Furo theme, automatic API docs
- **CI/CD**: GitHub Actions with comprehensive checks
- **Security**: pip-audit, dependency scanning
- **Development**: Nox for task automation, comprehensive dev tools

## 🛠️ What You Need to Install

### Required
- **uv**: Fast Python package manager (see [installation](https://docs.astral.sh/uv/getting-started/installation/))
- **Copier**: Template engine (`uv pip install copier`)
- **Nox**: Task automation (`uv pip install nox`)

### Optional but Recommended
- **Just**: Command runner for shortcuts (see [installation](https://just.systems/man/en/))

## 🎯 What the Template Provides

When you generate a project, it includes:

### ✅ **Automatically Included (No Installation Required)**
- **All Python dependencies** (Black, Ruff, MyPy, pytest, Sphinx, etc.)
- **Pre-commit hooks** for code quality
- **Nox automation** for development tasks
- **Just shortcuts** for common commands
- **GitHub Actions** for CI/CD
- **Complete test structure** with unit, integration, and e2e tests
- **Documentation setup** with Sphinx and Furo theme

## 📚 Documentation

- **[Quick Start](docs/source/quickstart.md)** - Get started in 5 minutes
- **[Installation Guide](docs/source/installation.md)** - Detailed installation instructions
- **[Template Guide](docs/template-guide.md)** - Complete usage instructions
- **[Architecture Decisions](docs/adr/)** - Design decisions and rationale
- **[Contributing](docs/contributing.md)** - How to contribute to the template

### Building Documentation

To build and view the documentation locally:

```bash
# Build documentation
cd docs && ./build-docs.sh

# Serve locally
cd docs && make serve
```

The documentation will be available at http://localhost:8000

## 🛠️ Template Configuration

The template supports various configuration options:

- **Project metadata**: name, description, author, license
- **Python versions**: 3.11, 3.12, 3.13
- **Optional features**: CLI interface, conda fallback
- **Quality thresholds**: coverage, complexity limits

## 🎯 What You Get

A fully configured Python project with:

```
my-awesome-project/
├── src/my_awesome_project/     # Your package code
├── tests/                      # Test suite
│   ├── unit/                   # Unit tests
│   ├── integration/            # Integration tests
│   └── e2e/                    # End-to-end tests
├── docs/                       # Documentation
├── .github/                    # GitHub Actions workflows
├── pyproject.toml             # Modern Python configuration
├── .pre-commit-config.yaml    # Code quality hooks
├── noxfile.py                 # Development tasks
├── justfile                   # Development shortcuts
└── README.md                  # Project documentation
```

## 🤝 Contributing

See [CONTRIBUTING.md](docs/contributing.md) for details on contributing to the template.

## 🔧 Troubleshooting

### Common Issues

**Template generation fails**
```bash
# Make sure you have the latest version of Copier
uv pip install --upgrade copier

# Try with verbose output
copier copy https://github.com/jeffrichley/seedling-template.git my-project --trust -v
```

**Dependencies fail to install**
```bash
# Make sure you have uv installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Try clearing uv cache
uv cache clean
```

**Tests fail after generation**
```bash
# Make sure all dependencies are installed
uv sync --all-extras

# Run tests with verbose output
uv run pytest -v
```

### Getting Help

- 📖 **[Template Guide](docs/template-guide.md)** - Complete usage instructions
- 🐛 **[Issues](https://github.com/jeffrichley/seedling-template/issues)** - Report bugs or request features
- 💬 **[Discussions](https://github.com/jeffrichley/seedling-template/discussions)** - Ask questions and get help

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.
