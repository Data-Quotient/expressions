# exceptions/custom_exceptions.py

from exceptions.base_exceptions import DataFusionBaseError

class DataTypeMismatchError(DataFusionBaseError):
    """Raised when there is a mismatch between expected and actual data types."""
    def __init__(self, expected_type, actual_type, column):
        self.expected_type = expected_type
        self.actual_type = actual_type
        self.column = column
        super().__init__(f"Data type mismatch in column '{column}': Expected {expected_type}, got {actual_type}.")

class ColumnNotFoundError(DataFusionBaseError):
    """Raised when a required column is missing in the DataFrame."""
    def __init__(self, column):
        self.column = column
        super().__init__(f"Column '{column}' not found in the DataFrame.")

class InvalidOperationError(DataFusionBaseError):
    """Raised when an invalid operation is performed on the DataFrame."""
    def __init__(self, operation, reason):
        self.operation = operation
        self.reason = reason
        super().__init__(f"Invalid operation '{operation}': {reason}.")
