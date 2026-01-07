"""
Custom Exception Classes

Defines application-specific exceptions with proper error handling.
"""


class ClassSightException(Exception):
    """Base exception for ClassSight application."""
    pass


class AuthenticationError(ClassSightException):
    """Raised when authentication fails."""
    pass


class AuthorizationError(ClassSightException):
    """Raised when user lacks required permissions."""
    pass


class ValidationError(ClassSightException):
    """Raised when data validation fails."""
    pass


class DataNotFoundError(ClassSightException):
    """Raised when requested data is not found."""
    pass


class DatabaseError(ClassSightException):
    """Raised when database operations fail."""
    pass


class ReportGenerationError(ClassSightException):
    """Raised when report generation fails."""
    pass
