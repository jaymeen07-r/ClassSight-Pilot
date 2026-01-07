"""
Logging Configuration Module

Provides centralized logging configuration for all modules.
"""

import logging
import logging.handlers
from pathlib import Path
from datetime import datetime


def setup_logging(
    log_level: str = 'INFO',
    log_dir: str = './logs'
) -> None:
    """
    Configure application-wide logging.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_dir: Directory to store log files
    """
    Path(log_dir).mkdir(exist_ok=True)
    
    log_file = Path(log_dir) / f"classsight_{datetime.now().strftime('%Y%m%d')}.log"
    
    # Create logger
    logger = logging.getLogger('classsight')
    logger.setLevel(getattr(logging, log_level))
    
    # File handler
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10485760,  # 10MB
        backupCount=10
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def get_logger(name: str) -> logging.Logger:
    """Get logger instance for module."""
    return logging.getLogger(f'classsight.{name}')
