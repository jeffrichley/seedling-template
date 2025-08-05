# 🧪 Testing

> "Testing leads to failure, and failure leads to understanding."
> — **Burt Rutan**

Seedling includes a comprehensive testing framework with modern Python testing tools and **enforceable testing rules** to ensure consistent, maintainable, high-quality tests.

## Overview

The template provides:
- **pytest**: Modern Python testing framework
- **Coverage**: Test coverage measurement (≥90% required)
- **Hypothesis**: Property-based testing
- **Mocking**: Built-in mocking capabilities
- **Test organization**: Clear test structure with markers
- **Quality gates**: Automated enforcement of testing standards

## Core Principles

✅ **Test WHAT the system does, not HOW it does it** - Focus on public behavior, not internal implementation
✅ **All production code must have tests** - No exceptions
✅ **Tests must be readable, reliable, and relevant**
✅ **Maintain ≥90% line and branch coverage** - Security-critical code requires 100%
✅ **Tests are tiered by scope and purpose** - Each type has a specific role
✅ **Tests must be isolated, fast, focused, and descriptive**

## Test Structure

```
tests/
├── unit/                    # Fast, isolated function/class tests
│   ├── __init__.py
│   └── test_example.py
├── integration/             # Cross-module or DB/file system I/O
│   └── __init__.py
├── functional/              # High-level, multi-layer behavior
│   └── __init__.py
├── e2e/                     # End-to-end user flows or API
│   └── __init__.py
└── performance/             # Load/latency testing
    └── __init__.py
```

### Test Directory + Marker Pairings

| Directory              | Purpose                            | Marker                 |
|------------------------|------------------------------------|------------------------|
| `tests/unit/`          | Fast, isolated function/class tests | `@pytest.mark.unit`    |
| `tests/integration/`   | Cross-module or DB/file system I/O  | `@pytest.mark.integration` |
| `tests/functional/`    | High-level, multi-layer behavior    | `@pytest.mark.functional`  |
| `tests/e2e/`           | End-to-end user flows or API         | `@pytest.mark.e2e`     |
| `tests/performance/`   | Load/latency testing                | `@pytest.mark.performance` |

## Available Commands

The template provides multiple ways to run commands:

### Just Commands (Recommended)
```bash
just test          # Run tests with coverage
just test-unit     # Run unit tests only
just test-integration  # Run integration tests only
just test-functional   # Run functional tests only
just test-e2e      # Run e2e tests only
just test-performance # Run performance tests only
just lint          # Run linting and formatting
just type-check    # Run type checking
just docs          # Build documentation
just coverage      # Generate HTML coverage report
just security      # Run security audit
just quality       # Run all quality checks
just pre-commit    # Run pre-commit hooks
```



### Nox Commands (Alternative)
```bash
nox -s tests       # Run tests with coverage
nox -s lint        # Run linting and formatting
nox -s type_check  # Run type checking
nox -s docs        # Build documentation
nox -s coverage_html # Generate HTML coverage report
nox -s security    # Run security audit
nox -s pre-commit  # Run pre-commit hooks
```

### Direct uv Commands (Raw)
```bash
uv run pytest tests --cov=src --cov-report=term-missing  # Run tests with coverage
uv run ruff check src tests --fix                        # Run Ruff linting
uv run black --check src tests                           # Run Black formatting
uv run mypy src tests                                    # Run MyPy type checking
uv run sphinx-build -W docs/source docs/build            # Build documentation
uv run coverage html                                     # Generate HTML coverage
uv run pip-audit --progress-spinner=off                  # Run security audit
uv run pre-commit run --all-files                        # Run pre-commit hooks
```

## Running Tests

### Basic Testing

```bash
# Run all tests
just test
# or
nox -s tests
# or
uv run pytest tests --cov=src --cov-report=term-missing

# Run with coverage (coverage is included by default)
just test
# or
nox -s tests
# or
uv run pytest tests --cov=src --cov-report=term-missing

# Run specific test file
uv run pytest tests/unit/test_example.py

# Run specific test function
uv run pytest tests/unit/test_example.py::test_main_function_returns_processed_string
```

### Test Categories by Marker

```bash
# Run only unit tests
uv run pytest -m unit

# Run only integration tests
uv run pytest -m integration

# Run only functional tests
uv run pytest -m functional

# Run only e2e tests
uv run pytest -m e2e

# Run only performance tests
uv run pytest -m performance

# Run fast tests (exclude slow)
uv run pytest -m "not slow"
```

### Coverage Testing

```bash
# Run with coverage report (included by default)
just test
# or
nox -s tests

# Generate HTML coverage report
just coverage
# or
nox -s coverage_html
# or
uv run coverage html

# Check coverage threshold (configured in pyproject.toml)
just test
# or
nox -s tests
# or
uv run pytest tests --cov=src --cov-report=term-missing
```

## Writing Tests



### Test Structure Rules

#### ✅ Function Naming
Use: `test_<thing_under_test>_<expected_behavior>`

```python
def test_export_method_creates_output_file():
def test_register_raises_on_duplicate():
def test_yaml_loader_parses_valid_input():
```

#### ✅ Docstrings
Every test must have a 1-line docstring explaining **what is being tested**:

```python
def test_register_raises_on_duplicate():
    '''Test that register() raises ValueError if a name is already registered.'''
```

#### ✅ Arrange-Act-Assert Structure
Tests must follow the Arrange-Act-Assert structure with blank lines between phases:

```python
def test_register_raises_on_duplicate():
    '''Raises if duplicate name is registered.'''

    # Arrange
    registry = Registry()
    registry.register("foo", {})

    # Act
    with pytest.raises(ValueError):
        registry.register("foo", {})

    # Assert
    assert "foo" in registry.names
```

### Unit Tests

```python
# tests/unit/test_example.py
import pytest
from your_package.example import main_function


@pytest.mark.unit
def test_main_function_returns_processed_string():
    '''Returns processed string when given valid input.'''
    
    # Arrange
    input_text = "test input"
    
    # Act
    result = main_function(input_text)
    
    # Assert
    assert result == "Processed: test input"


@pytest.mark.unit
def test_main_function_handles_empty_input():
    '''Returns processed string when given empty input.'''
    
    # Arrange
    input_text = ""
    
    # Act
    result = main_function(input_text)
    
    # Assert
    assert result == "Processed: "


@pytest.mark.unit
def test_main_function_raises_on_none_input():
    '''Raises ValueError when given None input.'''
    
    # Arrange
    input_text = None
    
    # Act & Assert
    with pytest.raises(ValueError, match="Input cannot be None"):
        main_function(input_text)
```

### Property-Based Testing

```python
# tests/unit/test_property_based.py
from hypothesis import given, strategies as st
from your_package.example import main_function


@pytest.mark.unit
@given(st.text())
def test_main_function_properties(input_text):
    '''Test main function properties with any text input.'''
    
    # Act
    result = main_function(input_text)
    
    # Assert - Property 1: Result is always a string
    assert isinstance(result, str)
    
    # Assert - Property 2: Result always starts with "Processed: "
    assert result.startswith("Processed: ")
    
    # Assert - Property 3: Result length is predictable
    assert len(result) == len("Processed: ") + len(input_text)
```

### Integration Tests

```python
# tests/integration/test_integration.py
import pytest
from your_package.core import CoreClass
from your_package.config import Config


@pytest.mark.integration
class TestCoreIntegration:
    '''Integration tests for core functionality.'''
    
    def test_core_processes_data_with_config(self):
        '''Processes data successfully with configuration.'''
        
        # Arrange
        config = Config(debug=True, timeout=30)
        core = CoreClass(config)
        test_data = "test data"
        
        # Act
        result = core.process_data(test_data)
        
        # Assert
        assert result.is_success
        assert result.data == "processed test data"
    
    def test_core_saves_data_to_database(self, db_connection):
        '''Saves data successfully to database.'''
        
        # Arrange
        core = CoreClass(db_connection=db_connection)
        test_data = "test data"
        
        # Act
        result = core.save_data(test_data)
        
        # Assert
        assert result.is_success
        
        # Verify data was saved
        saved_data = db_connection.get_data()
        assert test_data in saved_data
```

### Functional Tests

```python
# tests/functional/test_functional.py
import pytest
from your_package.service import Service
from your_package.repository import Repository


@pytest.mark.functional
class TestServiceFunctional:
    '''Functional tests for service layer.'''
    
    def test_service_creates_user_with_valid_data(self, mock_repository):
        '''Creates user successfully with valid data.'''
        
        # Arrange
        service = Service(repository=mock_repository)
        user_data = {"name": "Alice", "email": "alice@example.com"}
        
        # Act
        result = service.create_user(user_data)
        
        # Assert
        assert result.is_success
        assert result.user.name == "Alice"
        mock_repository.save_user.assert_called_once()
```

### End-to-End Tests

```python
# tests/e2e/test_e2e.py
import pytest
from your_package.cli import main


@pytest.mark.e2e
class TestCLIEndToEnd:
    '''End-to-end tests for CLI functionality.'''
    
    def test_cli_processes_file_successfully(self, capsys):
        '''Processes file successfully through CLI.'''
        
        # Arrange
        with pytest.MonkeyPatch().context() as m:
            m.setattr('sys.argv', ['your_package', 'process', 'test.txt'])
            
            # Act
            main()
            
            # Assert
            captured = capsys.readouterr()
            assert "Processing test.txt" in captured.out
            assert "Success" in captured.out
    
    def test_cli_handles_missing_file_error(self, capsys):
        '''Handles missing file error gracefully.'''
        
        # Arrange
        with pytest.MonkeyPatch().context() as m:
            m.setattr('sys.argv', ['your_package', 'process', 'nonexistent.txt'])
            
            # Act
            main()
            
            # Assert
            captured = capsys.readouterr()
            assert "Error" in captured.err
            assert "File not found" in captured.err
```

### Performance Tests

```python
# tests/performance/test_performance.py
import pytest
import time
from your_package.performance import slow_function


@pytest.mark.performance
def test_slow_function_completes_within_timeout():
    '''Completes within acceptable time limit.'''
    
    # Arrange
    start_time = time.time()
    
    # Act
    result = slow_function()
    
    # Assert
    execution_time = time.time() - start_time
    assert result is not None
    assert execution_time < 1.0  # Should complete in under 1 second
```

## Test Configuration

### pytest Configuration

```toml
# pyproject.toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--strict-config",
    "--verbose",
    "--tb=short",
]
markers = [
    "unit: marks tests as unit tests",
    "integration: marks tests as integration tests",
    "functional: marks tests as functional tests",
    "e2e: marks tests as end-to-end tests",
    "performance: marks tests as performance tests",
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
]
```

### Coverage Configuration

```toml
# pyproject.toml
[tool.coverage.run]
source = ["src"]
omit = [
    "*/tests/*",
    "*/test_*",
    "*/__pycache__/*",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "class .*\\bProtocol\\):",
    "@(abc\\.)?abstractmethod",
]
fail_under = 90
```

## Test Fixtures

### Built-in Fixtures

The template provides essential fixtures in `tests/conftest.py`:

- `temp_directory`: Temporary directory for file-based tests
- `sample_data`: Minimal test data for various scenarios
- `mock_logger`: Mock logger for testing logging behavior

### Extended Fixture Libraries

Additional fixture libraries are available in `tests/fixtures/`:

- `database_fixtures.py`: Database testing helpers (SQLite, mocks, sample data)
- `file_fixtures.py`: File system testing helpers (temp files, sample files, large files)

### Common Fixtures

```python
# tests/conftest.py
import pytest
from unittest.mock import MagicMock
from your_package.config import Config
from your_package.database import Database


@pytest.fixture
def config():
    '''Provide test configuration.'''
    return Config(debug=True, timeout=10)


@pytest.fixture
def db_connection():
    '''Provide test database connection.'''
    db = Database(":memory:")
    db.create_tables()
    yield db
    db.close()


@pytest.fixture
def mock_repository():
    '''Provide mock repository for testing.'''
    mock = MagicMock(spec=Repository)
    mock.save_user.return_value = True
    mock.get_user.return_value = None
    return mock


@pytest.fixture
def sample_data():
    '''Provide sample test data.'''
    return {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
        ],
        "products": [
            {"id": 1, "name": "Product A", "price": 10.99},
            {"id": 2, "name": "Product B", "price": 20.99},
        ]
    }
```

## Mocking Rules

### ✅ Mock External Systems
- Filesystem (`os`, `pathlib`, etc.)
- Time (`datetime`, `sleep`)
- Networking (`httpx`, `requests`)
- Databases and ORMs
- Cloud SDKs

### ✅ How to Mock
```python
from unittest.mock import patch, MagicMock

@pytest.mark.unit
def test_function_creates_file():
    '''Creates file when given valid path.'''
    
    # Arrange
    file_path = "/tmp/test.txt"
    
    # Act & Assert
    with patch('pathlib.Path.write_text') as mock_write:
        create_file(file_path, "content")
        mock_write.assert_called_once_with("content")
```

### ❌ Never Mock
- The method you're testing
- Internal functions without compelling reason

### ✅ Do Mock Your Code ONLY IF Justified
> If using Cursor/AI, request permission before mocking internals:

```text
INTERNAL MOCK REQUEST:
I want to mock `TimelineBuilder._build_layers()` because it's slow and already tested elsewhere.
```

## Best Practices

### Test Organization

1. **Group related tests** in classes with descriptive names
2. **Use descriptive test names** that explain the scenario
3. **Follow AAA pattern**: Arrange, Act, Assert with blank lines
4. **Keep tests independent** and isolated
5. **Use fixtures** for common setup
6. **Place tests in correct directories** with appropriate markers

### Test Quality

1. **Test the behavior**, not the implementation
2. **Write tests first** (TDD approach)
3. **Test edge cases** and error conditions
4. **Use property-based testing** for complex logic
5. **Mock external dependencies** only
6. **Keep runtime <200ms** for unit tests

### Coverage Goals

1. **Maintain ≥90% coverage** overall
2. **100% coverage** for security-critical code
3. **100% coverage** for new code
4. **Test error handling** paths
5. **Test boundary conditions**
6. **Use `# pragma: no cover`** only for platform-specific or unreachable code

## Advanced Testing

### Parameterized Tests

```python
import pytest


@pytest.mark.unit
@pytest.mark.parametrize("input_text,expected", [
    ("hello", "Processed: hello"),
    ("world", "Processed: world"),
    ("", "Processed: "),
])
def test_main_function_with_various_inputs(input_text, expected):
    '''Test main function with multiple inputs.'''
    
    # Act
    result = main_function(input_text)
    
    # Assert
    assert result == expected
```

### Async Testing

```python
import pytest
import asyncio
from your_package.async_module import async_function


@pytest.mark.unit
@pytest.mark.asyncio
async def test_async_function_returns_processed_result():
    '''Returns processed result for async function.'''
    
    # Arrange
    input_text = "test"
    
    # Act
    result = await async_function(input_text)
    
    # Assert
    assert result == "async processed: test"
```

### Mutation Testing (Advanced)

Use `mutmut` or `cosmic-ray` to verify test strength:

```bash
# Install mutation testing
uv add mutmut

# Run mutation testing
uv run mutmut run --paths-to-mutate src/your_package/
```

Required for:
- Reward functions
- Decision graphs
- Flow control systems

## CI/CD Integration

### Automated Testing

The template includes automated testing in CI/CD that:

- **Runs on every commit**: Tests are automatically executed on push and pull requests
- **Multi-Python support**: Tests against all specified Python versions
- **Coverage reporting**: Generates coverage reports and uploads to Codecov
- **Quality gates**: Fails the build if coverage drops below 90%
- **Fast execution**: Uses `uv` for fast dependency installation and test execution
- **Marker-based execution**: Runs different test types in appropriate environments

### CI Strategy

Split jobs by marker:

```yaml
- name: Unit Tests
  run: pytest -m unit

- name: Integration Tests
  run: pytest -m integration

- name: Functional Tests
  run: pytest -m functional

- name: End-to-End Tests (nightly)
  run: pytest -m e2e

- name: Performance Tests (weekly)
  run: pytest -m performance
```

## Troubleshooting

### Common Issues

#### Import Errors

```bash
# Check Python path
PYTHONPATH=src uv run pytest

# Install in editable mode
uv pip install -e .
```

#### Coverage Issues

```bash
# Check coverage configuration
uv run coverage run --source=src -m pytest
uv run coverage report

# Debug coverage
uv run coverage debug data
```

#### Slow Tests

```bash
# Run only fast tests
uv run pytest -m "not slow"

# Profile test performance
uv run pytest --durations=10
```

### Getting Help

- **pytest documentation**: https://docs.pytest.org/
- **Hypothesis documentation**: https://hypothesis.readthedocs.io/
- **Coverage documentation**: https://coverage.readthedocs.io/
- **pytest-cov documentation**: https://pytest-cov.readthedocs.io/

## Anti-patterns to Avoid

| Bad Practice                  | Instead...                          |
|------------------------------|-------------------------------------|
| `assert True`                | Write meaningful assertions         |
| Over-patching                | Use `@patch` only where needed      |
| Mocking internal logic       | Inject or test real implementations |
| Testing mocks instead of logic | Assert true behavior and outputs  |
| Test state dependent on config | Inject config with fixtures       |
| Fragile static assertions    | Use dynamic or relational assertions |



## Project-Specific Testing Guide

For detailed guidance on writing tests for your specific project, see the comprehensive testing guide in your project's `tests/README.md` file.

## Next Steps

- **Set up test databases** for integration tests
- **Configure test environments** for different scenarios
- **Add performance benchmarks** for critical functions
- **Set up test data factories** for complex test scenarios
- **Implement mutation testing** for critical code paths 