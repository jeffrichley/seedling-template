"""File system testing fixtures for {{ project_name }}.

This module provides fixtures for testing file system operations.
Use these fixtures when you need to test code that reads, writes, or manipulates files.

When to use:
- Integration tests that need real file operations
- Tests that verify file reading and writing
- Tests that check file system interactions
- Tests that need temporary files or directories

How to use:
1. Import the fixtures you need in your test file
2. Add them as parameters to your test functions
3. Use the provided file paths and directories in your tests

Example:
    def test_file_operations(temp_file):
        # Use temp_file to test file operations
        temp_file.write_text("test content")
        assert temp_file.read_text() == "test content"
"""

from collections.abc import Generator
from pathlib import Path

import pytest


@pytest.fixture(scope="function")
def temp_file(temp_directory: Path) -> Generator[Path, None, None]:
    """Provide a temporary file for testing.

    This fixture creates a temporary file that is automatically cleaned up
    after each test. Use this for tests that need to read from or write to files.

    Example:
        def test_file_reading(temp_file):
            # Write test data
            temp_file.write_text("Hello, World!")

            # Test reading
            content = temp_file.read_text()
            assert content == "Hello, World!"
    """
    temp_file_path = temp_directory / "test_file.txt"
    yield temp_file_path
    # Cleanup is handled by temp_directory fixture


@pytest.fixture(scope="function")
def temp_files(temp_directory: Path) -> Generator[dict[str, Path], None, None]:
    """Provide multiple temporary files for testing.

    This fixture creates multiple temporary files with different names
    that can be used in tests requiring multiple files.

    Example:
        def test_multiple_files(temp_files):
            # Write to different files
            temp_files["input"].write_text("input data")
            temp_files["config"].write_text('{"key": "value"}')

            # Test operations with multiple files
            assert temp_files["input"].read_text() == "input data"
            assert temp_files["config"].read_text() == '{"key": "value"}'
    """
    files = {
        "input": temp_directory / "input.txt",
        "output": temp_directory / "output.txt",
        "config": temp_directory / "config.json",
        "log": temp_directory / "test.log",
    }

    yield files
    # Cleanup is handled by temp_directory fixture


@pytest.fixture(scope="function")
def sample_files(temp_directory: Path) -> Generator[dict[str, Path], None, None]:
    """Provide sample files with pre-populated content.

    This fixture creates files with sample content that can be used
    across multiple tests. Use this when you need consistent test data.

    Example:
        def test_file_processing(sample_files):
            # Files already have content
            content = sample_files["config"].read_text()
            assert "debug" in content
    """
    files = {
        "config": temp_directory / "config.json",
        "data": temp_directory / "data.csv",
        "template": temp_directory / "template.txt",
    }

    # Create files with sample content
    files["config"].write_text('{"debug": true, "timeout": 30}')
    files["data"].write_text(
        "id,name,email\n1,Alice,alice@example.com\n2,Bob,bob@example.com"
    )
    files["template"].write_text("Hello {{name}}, welcome to {{project}}!")

    yield files
    # Cleanup is handled by temp_directory fixture


@pytest.fixture(scope="function")
def mock_file_system() -> Generator[dict[str, object], None, None]:
    """Provide a mock file system for unit testing.

    This fixture provides a mock file system that can be used to test
    file interaction code without requiring real file operations.
    Use this in unit tests where you want to verify file calls
    without actually creating files.

    Example:
        def test_file_service_creates_file(mock_file_system):
            with patch('pathlib.Path', mock_file_system):
                service = FileService()
                service.create_file("test.txt", "content")

                mock_file_system["write_text"].assert_called_once_with("content")
    """
    mock = {
        "exists": True,
        "is_file": True,
        "is_dir": False,
        "read_text": "mock file content",
        "write_text": None,
        "mkdir": None,
        "rmdir": None,
    }

    yield mock


@pytest.fixture(scope="function")
def large_file(temp_directory: Path) -> Generator[Path, None, None]:
    """Provide a large file for performance testing.

    This fixture creates a file with a significant amount of data
    that can be used for testing performance characteristics.

    Example:
        def test_large_file_processing(large_file):
            # Test processing of large files
            result = process_large_file(large_file)
            assert result.is_success
    """
    large_file_path = temp_directory / "large_file.txt"

    # Create a file with 1MB of data
    content = "x" * 1024 * 1024  # 1MB
    large_file_path.write_text(content)

    yield large_file_path
    # Cleanup is handled by temp_directory fixture


@pytest.fixture(scope="function")
def nested_directory_structure(temp_directory: Path) -> Generator[Path, None, None]:
    """Provide a nested directory structure for testing.

    This fixture creates a complex directory structure with files
    at different levels that can be used for testing directory traversal.

    Example:
        def test_directory_traversal(nested_directory_structure):
            # Test walking through nested directories
            files = list(nested_directory_structure.rglob("*.txt"))
            assert len(files) > 0
    """
    # Create nested directory structure
    (temp_directory / "level1" / "level2" / "level3").mkdir(parents=True, exist_ok=True)

    # Create files at different levels
    (temp_directory / "root.txt").write_text("root file")
    (temp_directory / "level1" / "level1.txt").write_text("level1 file")
    (temp_directory / "level1" / "level2" / "level2.txt").write_text("level2 file")
    (temp_directory / "level1" / "level2" / "level3" / "level3.txt").write_text(
        "level3 file"
    )

    yield temp_directory
    # Cleanup is handled by temp_directory fixture


# Add your project-specific file fixtures below:
#
# @pytest.fixture
# def image_file():
#     """Provide a test image file."""
#     # Implementation here
#
# @pytest.fixture
# def zip_file():
#     """Provide a test zip file."""
#     # Implementation here
