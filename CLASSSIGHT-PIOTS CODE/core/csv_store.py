"""
CSV Data Store Module

Handles reading, writing, and validating CSV data files
with proper error handling and type safety.
"""

from typing import Dict, List, Optional, Any, Union
from pathlib import Path
import pandas as pd
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class CSVStore:
    """
    Manages CSV file operations for educational data storage.
    
    This class provides methods to read, write, validate, and 
    manage CSV files used throughout the ClassSight system.
    
    Attributes:
        data_dir (Path): Directory containing CSV files
        encoding (str): Character encoding for file operations
        
    Example:
        >>> store = CSVStore('./data')
        >>> df = store.read_student_data()
        >>> store.validate_csv_structure(df)
    """
    
    def __init__(
        self, 
        data_dir: Union[str, Path] = './data',
        encoding: str = 'utf-8'
    ) -> None:
        """
        Initialize CSVStore instance.
        
        Args:
            data_dir: Path to directory containing CSV files
            encoding: File encoding (default: utf-8)
            
        Raises:
            ValueError: If data_dir does not exist
        """
        self.data_dir = Path(data_dir)
        self.encoding = encoding
        
        if not self.data_dir.exists():
            raise ValueError(f"Data directory does not exist: {data_dir}")
            
    def read_csv(
        self, 
        filename: str,
        sheet_name: Optional[str] = None
    ) -> pd.DataFrame:
        """
        Read CSV file with validation.
        
        Args:
            filename: Name of CSV file to read
            sheet_name: Sheet name for Excel files
            
        Returns:
            Loaded DataFrame
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If data is invalid
        """
        file_path = self.data_dir / filename
        
        if not file_path.exists():
            logger.error(f"CSV file not found: {file_path}")
            raise FileNotFoundError(f"File not found: {filename}")
            
        try:
            df = pd.read_csv(file_path, encoding=self.encoding)
            logger.info(f"Successfully loaded CSV: {filename}")
            return df
        except Exception as e:
            logger.error(f"Error reading CSV {filename}: {str(e)}")
            raise
    
    def validate_csv_structure(
        self, 
        df: pd.DataFrame,
        required_columns: List[str]
    ) -> bool:
        """
        Validate CSV structure against requirements.
        
        Args:
            df: DataFrame to validate
            required_columns: List of required column names
            
        Returns:
            True if valid, False otherwise
        """
        missing = set(required_columns) - set(df.columns)
        if missing:
            logger.warning(f"Missing columns: {missing}")
            return False
        return True
