from typing import Any, Dict, Generic, List, Optional, TypeVar
from pydantic import BaseModel
from fastapi import status
from fastapi.responses import JSONResponse


T = TypeVar('T')


class ApiResponse(BaseModel, Generic[T]):
    """Standard API response format"""
    success: bool = True
    data: Optional[T] = None
    message: Optional[str] = None
    error: Optional[str] = None
    status_code: int = status.HTTP_200_OK


class PaginatedResponse(BaseModel):
    """Paginated API response format"""
    success: bool = True
    data: List[Any]
    message: Optional[str] = None
    total: int
    page: int
    limit: int
    has_next: bool = False
    has_prev: bool = False
    status_code: int = status.HTTP_200_OK


def create_success_response(
    data: Any = None, 
    message: str = "Success", 
    status_code: int = status.HTTP_200_OK
) -> ApiResponse:
    """Create a success response"""
    return ApiResponse(
        success=True,
        data=data,
        message=message,
        status_code=status_code
    )


def create_error_response(
    error: str, 
    message: str = "Error occurred", 
    status_code: int = status.HTTP_400_BAD_REQUEST
) -> ApiResponse:
    """Create an error response"""
    return ApiResponse(
        success=False,
        error=error,
        message=message,
        status_code=status_code
    )


def create_paginated_response(
    data: List[Any],
    total: int,
    page: int,
    limit: int,
    message: str = "Success"
) -> PaginatedResponse:
    """Create a paginated response"""
    has_next = (page * limit) < total
    has_prev = page > 1
    
    return PaginatedResponse(
        data=data,
        total=total,
        page=page,
        limit=limit,
        message=message,
        has_next=has_next,
        has_prev=has_prev
    )


def json_success(data: Any = None, message: str = "Success", status_code: int = 200):
    """Return JSON success response"""
    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "data": data,
            "message": message,
            "status_code": status_code
        }
    )


def json_error(error: str, message: str = "Error occurred", status_code: int = 400):
    """Return JSON error response"""
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "error": error,
            "message": message,
            "status_code": status_code
        }
    )