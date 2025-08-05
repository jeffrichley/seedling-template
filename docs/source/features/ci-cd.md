# 🚀 CI/CD

> "Automation is not about replacing humans, it's about amplifying human potential."
> — **Unknown**

Seedling includes comprehensive CI/CD configuration for automated testing and deployment.

## Overview

The template provides:
- **GitHub Actions**: Automated workflows
- **Testing**: Automated test execution
- **Quality checks**: Automated code quality validation
- **Deployment**: Automated deployment to PyPI

## Workflows

### CI Workflow

The main CI workflow runs on every push and pull request and includes:

- **Multi-Python Testing**: Tests against Python 3.11 and 3.12
- **Dependency Installation**: Uses `uv sync` for fast dependency management
- **Test Execution**: Runs the full test suite with coverage reporting
- **Quality Checks**: Runs linting, type checking, and documentation validation
- **Automatic Triggers**: Runs on every push and pull request

### Release Workflow

Automated releases to PyPI that trigger on version tags:

- **Tag-Based Triggers**: Automatically runs when you push a version tag (e.g., `v1.0.0`)
- **Package Building**: Builds the Python package using `uv run build`
- **PyPI Publishing**: Automatically publishes to PyPI using `twine`
- **Secure Credentials**: Uses GitHub secrets for PyPI authentication
- **Quality Gates**: Only releases if all tests and quality checks pass

## Quality Gates

The CI pipeline enforces strict quality standards:

1. **Tests must pass** with 80%+ coverage
2. **Code quality checks** must pass (Ruff, MyPy)
3. **Security scans** must find no vulnerabilities
4. **Documentation** must build without errors

## Configuration

### Automatic Configuration

The workflows are automatically configured based on your template variables:

- **Python versions**: Uses the `python_versions` you specified
- **Package name**: Uses your `project_slug`
- **Repository**: Uses your `github_username`
- **Dependencies**: Automatically includes all your project dependencies

### Secrets Required

For full functionality, set up these GitHub secrets:

- **`PYPI_API_TOKEN`**: For publishing to PyPI
- **`CODECOV_TOKEN`**: For coverage reporting

## Best Practices

1. **Run tests locally** before pushing
2. **Use feature branches** for development
3. **Write meaningful commit messages**
4. **Review CI results** before merging
5. **Keep dependencies updated**

## Next Steps

- **Set up deployment environments**
- **Configure branch protection rules**
- **Add performance testing**
- **Set up monitoring and alerting**
