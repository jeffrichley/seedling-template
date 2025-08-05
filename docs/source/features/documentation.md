# 📚 Documentation

Seedling includes comprehensive documentation tooling with Sphinx and modern documentation practices.

## Overview

The template provides:
- **Sphinx**: Professional documentation generator
- **Furo theme**: Modern, responsive documentation theme
- **MyST parser**: Markdown support for Sphinx
- **API documentation**: Automatic API documentation
- **Search functionality**: Full-text search

## Documentation Structure

```
docs/
├── source/                    # Source files
│   ├── index.md              # Main documentation index
│   ├── contributing.md       # Contributing guide
│   └── _static/              # Static assets
├── build/                    # Built documentation
└── pyproject.toml           # Documentation dependencies
```

## Building Documentation

```bash
# Build documentation
just docs
# or
nox -s docs
# or
uv run sphinx-build -W docs/source docs/build

# Serve locally (after building)
cd docs/build/html
python -m http.server 8000
```

## Writing Documentation

### Markdown Support

Use MyST Markdown with Sphinx extensions:

```markdown
# Your Documentation

## Code Examples

```python
def example_function():
    return "Hello, World!"
```

## Cross-References

See {doc}`../configuration` for template configuration options and {doc}`../examples` for usage examples.
```

### API Documentation

Automatic API documentation with autodoc:

```markdown
# API Reference

## Core Module

```{eval-rst}
.. automodule:: your_package.core
   :members:
   :undoc-members:
   :show-inheritance:
```
```

## Configuration

### Sphinx Configuration

```python
# docs/source/conf.py
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
]

html_theme = "furo"
```

### MyST Extensions

```python
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]
```

## Best Practices

1. **Write clear, concise documentation**
2. **Include code examples**
3. **Use cross-references**
4. **Test all links**
5. **Keep documentation up to date**

## Deployment

### GitHub Pages

The template includes automatic documentation deployment:

- **Automatic builds**: Documentation is built and deployed on every commit
- **GitHub Pages**: Automatically publishes to your project's GitHub Pages site
- **Branch protection**: Only deploys from the main branch
- **Custom domain support**: Can be configured to use a custom domain
- **Version history**: Maintains documentation history across releases

## Next Steps

- **Customize the theme** for your brand
- **Add more documentation sections**
- **Set up automatic deployment**
- **Integrate with your CI/CD pipeline** 