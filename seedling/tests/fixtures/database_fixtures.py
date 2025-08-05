"""Database testing fixtures for {{ project_name }}.

This module provides fixtures for testing database interactions.
Use these fixtures when you need to test code that interacts with databases.

When to use:
- Integration tests that need real database operations
- Tests that verify data persistence and retrieval
- Tests that check database constraints and relationships

How to use:
1. Import the fixtures you need in your test file
2. Add them as parameters to your test functions
3. Use the provided database connections in your tests

Example:
    def test_user_save_and_retrieve(db_connection):
        # Use db_connection to test database operations
        user = User(name="Test User")
        db_connection.save(user)
        retrieved = db_connection.get_user(user.id)
        assert retrieved.name == "Test User"
"""

import pytest
import sqlite3
from pathlib import Path
from typing import Generator
from unittest.mock import MagicMock


@pytest.fixture
def sqlite_memory_db() -> Generator[sqlite3.Connection, None, None]:
    """Provide an in-memory SQLite database for testing.
    
    This fixture creates a temporary SQLite database in memory that is
    automatically cleaned up after each test. Use this for fast database tests
    that don't need persistence.
    
    Example:
        def test_user_operations(sqlite_memory_db):
            # Create tables
            sqlite_memory_db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
            
            # Test operations
            sqlite_memory_db.execute("INSERT INTO users (name) VALUES (?)", ("Test User",))
            result = sqlite_memory_db.execute("SELECT name FROM users").fetchone()
            assert result[0] == "Test User"
    """
    
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()


@pytest.fixture
def sqlite_temp_db(temp_directory: Path) -> Generator[sqlite3.Connection, None, None]:
    """Provide a temporary SQLite database file for testing.
    
    This fixture creates a temporary SQLite database file that is
    automatically cleaned up after each test. Use this when you need
    to test file-based database operations.
    
    Example:
        def test_database_persistence(sqlite_temp_db):
            # Test operations that require file persistence
            sqlite_temp_db.execute("CREATE TABLE data (id INTEGER PRIMARY KEY, value TEXT)")
            sqlite_temp_db.commit()
            
            # Verify data persists
            result = sqlite_temp_db.execute("SELECT COUNT(*) FROM data").fetchone()
            assert result[0] == 0
    """
    
    db_path = temp_directory / "test.db"
    conn = sqlite3.connect(str(db_path))
    yield conn
    conn.close()


@pytest.fixture
def mock_database() -> MagicMock:
    """Provide a mock database for unit testing.
    
    This fixture provides a mock database that can be used to test
    database interaction code without requiring a real database.
    Use this in unit tests where you want to verify database calls
    without actually executing them.
    
    Example:
        def test_user_service_saves_user(mock_database):
            service = UserService(database=mock_database)
            user = User(name="Test User")
            
            service.save_user(user)
            
            mock_database.save_user.assert_called_once_with(user)
    """
    
    mock = MagicMock()
    mock.save_user = MagicMock()
    mock.get_user = MagicMock()
    mock.update_user = MagicMock()
    mock.delete_user = MagicMock()
    mock.commit = MagicMock()
    mock.rollback = MagicMock()
    return mock


@pytest.fixture
def database_with_sample_data(sqlite_memory_db: sqlite3.Connection) -> Generator[sqlite3.Connection, None, None]:
    """Provide a database with sample data for testing.
    
    This fixture creates a database with pre-populated sample data
    that can be used across multiple tests. Use this when you need
    consistent test data for integration tests.
    
    Example:
        def test_user_queries(database_with_sample_data):
            # Database already has sample users
            result = database_with_sample_data.execute(
                "SELECT COUNT(*) FROM users"
            ).fetchone()
            assert result[0] > 0
    """
    
    # Create tables
    sqlite_memory_db.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Insert sample data
    sample_users = [
        ("Alice Johnson", "alice@example.com"),
        ("Bob Smith", "bob@example.com"),
        ("Charlie Brown", "charlie@example.com"),
    ]
    
    for name, email in sample_users:
        sqlite_memory_db.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )
    
    sqlite_memory_db.commit()
    yield sqlite_memory_db


# Add your project-specific database fixtures below:
# 
# @pytest.fixture
# def postgres_test_db():
#     """Provide a PostgreSQL test database."""
#     # Implementation here
# 
# @pytest.fixture
# def mysql_test_db():
#     """Provide a MySQL test database."""
#     # Implementation here 