# 🔍 Quality Tooling

Seedling includes comprehensive quality tooling to ensure your code meets the highest standards.

## Overview

The template includes modern Python development tools for:
- **Code formatting**: Black and isort
- **Linting**: Ruff for fast Python linting
- **Type checking**: MyPy for static type analysis
- **Security**: pip-audit for vulnerability scanning
- **Code quality**: Vulture for dead code detection

## Tools Included

### Black - Code Formatting

Automatic code formatting with consistent style:

```bash
# Format code
just lint
# or
nox -s lint
# or
uv run ruff check src tests --fix && uv run black --check src tests

# Check formatting
just lint
# or
nox -s lint
# or
uv run ruff check src tests --fix && uv run black --check src tests
```

**Configuration**: Uses Black's default settings (88 character line length)

### Ruff - Fast Linting

Ultra-fast Python linter with comprehensive rules:

```bash
# Lint code
just lint
# or
nox -s lint
# or
uv run ruff check src tests --fix

# Auto-fix issues (Ruff auto-fixes by default)
just lint
# or
nox -s lint
# or
uv run ruff check src tests --fix
```

**Features**:
- 10-100x faster than flake8
- Built-in import sorting
- Auto-fixing capabilities
- Comprehensive rule set

### MyPy - Type Checking

Static type checking for Python:

```bash
# Type check
just type-check
# or
nox -s type_check
# or
uv run mypy src tests

# Type check with strict mode (configured in pyproject.toml)
just type-check
# or
nox -s type_check
# or
uv run mypy src tests
```

**Configuration**: Strict type checking with zero errors required

### pip-audit - Security Scanning

Dependency vulnerability scanning:

```bash
# Scan for vulnerabilities
just security
# or
nox -s security
# or
uv run pip-audit --progress-spinner=off

# Scan with detailed output
uv run pip-audit --progress-spinner=off
```

### Vulture - Dead Code Detection

Find unused code and imports:

```bash
# Find dead code
uv run vulture src tests
# (No just/nox equivalent - use direct command)
```

## Pre-commit Hooks

All quality tools are integrated with pre-commit hooks:

```bash
# Install pre-commit hooks
just pre-commit
# or
nox -s pre-commit
# or
uv run pre-commit run --all-files

# Run all hooks
just pre-commit
# or
nox -s pre-commit
# or
uv run pre-commit run --all-files
```

**Hooks included**:
- Black formatting
- Ruff linting
- MyPy type checking
- pip-audit security scan
- Vulture dead code detection

## Quality Gates

The template enforces strict quality standards:

### Coverage Requirements

- **Minimum coverage**: 80% (configurable)
- **New code**: 100% coverage required
- **Critical paths**: 100% coverage required

### Code Quality

- **Zero linting errors**: All Ruff rules must pass
- **Zero type errors**: MyPy must pass with no errors
- **Zero security issues**: pip-audit must find no vulnerabilities
- **Zero dead code**: Vulture must find no unused code

## Configuration

### Ruff Configuration

```toml
# pyproject.toml
[tool.ruff]
target-version = "py311"
line-length = 88
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "UP", # pyupgrade
]
ignore = [
    "E501",  # line too long, handled by black
    "B008",  # do not perform function calls in argument defaults
]

[tool.ruff.per-file-ignores]
"__init__.py" = ["F401"]
"tests/**/*" = ["B011"]
```

### MyPy Configuration

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true

[[tool.mypy.overrides]]
module = [
    "tests.*",
]
disallow_untyped_defs = false
```

## CI/CD Integration

All quality tools are integrated into the CI/CD pipeline:

- **Automated checks**: Quality tools run automatically on every commit
- **Quality gates**: Build fails if any quality checks fail
- **Fast feedback**: Issues are caught early in the development process
- **Consistent standards**: All contributors must meet the same quality standards
- **Documentation validation**: Ensures documentation builds correctly

## Best Practices

### Code Style

1. **Use type hints** for all functions
2. **Write docstrings** for public APIs
3. **Keep functions small** and focused
4. **Use meaningful variable names**
5. **Follow PEP 8** with Black formatting

### Testing

1. **Write tests first** (TDD approach)
2. **Aim for high coverage** (80% minimum)
3. **Test edge cases** and error conditions
4. **Use property-based testing** with Hypothesis
5. **Mock external dependencies**

### Security

1. **Regular dependency updates**
2. **Security scanning** with pip-audit
3. **Input validation** for all user inputs
4. **Secure configuration** management
5. **Regular security reviews**

## Troubleshooting

### Common Issues

#### MyPy Errors

```bash
# Check specific file
uv run mypy src/your_package/file.py

# Show error codes
uv run mypy --show-error-codes src/
```

#### Ruff Issues

```bash
# Show rule explanations
uv run ruff rule E501

# Generate configuration
uv run ruff --generate-config
```

#### Coverage Issues

```bash
# Generate coverage report
just coverage
# or
nox -s coverage_html
# or
uv run coverage html

# Check specific files
uv run pytest --cov=src/your_package
```

### Getting Help

- **Ruff documentation**: https://docs.astral.sh/ruff/
- **MyPy documentation**: https://mypy.readthedocs.io/
- **Black documentation**: https://black.readthedocs.io/
- **pip-audit documentation**: https://pypi.org/project/pip-audit/

## Next Steps

- **Configure quality thresholds** for your project
- **Set up pre-commit hooks** in your development workflow
- **Integrate with your IDE** for real-time feedback
- **Customize tool configurations** as needed 