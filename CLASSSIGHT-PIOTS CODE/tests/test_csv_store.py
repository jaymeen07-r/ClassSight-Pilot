"""
Unit tests for CSV Store module.
"""

import pytest
import pandas as pd
from pathlib import Path
from CLASSSIGHT_PIOTS_CODE.core.csv_store import CSVStore
from CLASSSIGHT_PIOTS_CODE.core.exceptions import ValidationError


@pytest.fixture
def csv_store(tmp_path):
    """Create temporary CSV store for testing."""
    return CSVStore(str(tmp_path))


@pytest.fixture
def sample_student_data():
    """Create sample student data."""
    return pd.DataFrame({
        'student_id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'email': ['alice@school.com', 'bob@school.com', 'charlie@school.com'],
        'class': ['9A', '9A', '9B']
    })


def test_csv_store_initialization(tmp_path):
    """Test CSVStore initialization."""
    store = CSVStore(str(tmp_path))
    assert store.data_dir == tmp_path


def test_csv_store_invalid_directory():
    """Test CSVStore with invalid directory."""
    with pytest.raises(ValueError):
        CSVStore('/nonexistent/path')


def test_read_csv_not_found(csv_store):
    """Test reading non-existent CSV."""
    with pytest.raises(FileNotFoundError):
        csv_store.read_csv('nonexistent.csv')


def test_validate_csv_structure(csv_store, sample_student_data):
    """Test CSV structure validation."""
    required_cols = ['student_id', 'name', 'email']
    result = csv_store.validate_csv_structure(sample_student_data, required_cols)
    assert result is True


def test_validate_csv_missing_columns(csv_store, sample_student_data):
    """Test validation with missing columns."""
    required_cols = ['student_id', 'name', 'missing_column']
    result = csv_store.validate_csv_structure(sample_student_data, required_cols)
    assert result is False
