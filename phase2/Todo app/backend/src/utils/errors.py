import logging
from fastapi import HTTPException, status
from typing import Dict, Any


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TodoException(HTTPException):
    """Custom exception for todo-related errors"""
    def __init__(self, detail: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(status_code=status_code, detail=detail)


class UserException(HTTPException):
    """Custom exception for user-related errors"""
    def __init__(self, detail: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(status_code=status_code, detail=detail)


class AuthException(HTTPException):
    """Custom exception for authentication-related errors"""
    def __init__(self, detail: str, status_code: int = status.HTTP_401_UNAUTHORIZED):
        super().__init__(status_code=status_code, detail=detail)


# Error responses
def create_error_response(message: str, error_code: str = None) -> Dict[str, Any]:
    """Create standardized error response"""
    error_dict = {"detail": message}
    if error_code:
        error_dict["error_code"] = error_code
    return error_dict


# Logging utilities
def log_info(message: str):
    logger.info(message)


def log_error(message: str):
    logger.error(message)


def log_warning(message: str):
    logger.warning(message)