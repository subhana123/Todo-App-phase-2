from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session
from typing import List, Optional
from ..models.todo_item import (
    TodoItem, TodoItemCreate, TodoItemRead, TodoItemUpdate, TodoItemUpdateStatus
)
from ..services.todo_service import TodoService
from ..api.auth import get_current_user
from ..db.database import get_session
from ..models.user import User
from ..utils.responses import create_success_response, create_error_response


router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", response_model=dict)
def get_user_todos(
    current_user: User = Depends(get_current_user),
    db_session: Session = Depends(get_session),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, le=100),
    status: Optional[str] = Query(None, regex="^(all|pending|completed)$")
):
    """Get all todo items for the current user"""
    try:
        todo_items = TodoService.get_todo_items_for_user(
            user_id=current_user.id,
            db_session=db_session,
            skip=skip,
            limit=limit,
            status_filter=status
        )
        
        # Format the response to include pagination info
        return create_success_response(
            data={
                "items": todo_items,
                "total": len(todo_items),  # In a real app, you'd get the actual total count
                "offset": skip,
                "limit": limit
            },
            message="Todo items retrieved successfully"
        )
    except Exception as e:
        return create_error_response(
            error=str(e),
            message="Failed to retrieve todo items"
        )


@router.post("/", response_model=TodoItemRead)
def create_todo(
    todo_create: TodoItemCreate,
    current_user: User = Depends(get_current_user),
    db_session: Session = Depends(get_session)
):
    """Create a new todo item for the current user"""
    try:
        todo_item = TodoService.create_todo_item(
            todo_create=todo_create,
            user_id=current_user.id,
            db_session=db_session
        )
        return create_success_response(
            data=todo_item,
            message="Todo item created successfully"
        )
    except Exception as e:
        return create_error_response(
            error=str(e),
            message="Failed to create todo item"
        )


@router.get("/{todo_id}", response_model=TodoItemRead)
def get_todo(
    todo_id: int,
    current_user: User = Depends(get_current_user),
    db_session: Session = Depends(get_session)
):
    """Get a specific todo item by ID"""
    try:
        todo_item = TodoService.get_todo_item_by_id(
            todo_id=todo_id,
            user_id=current_user.id,
            db_session=db_session
        )
        
        if not todo_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo item not found"
            )
        
        return create_success_response(
            data=todo_item,
            message="Todo item retrieved successfully"
        )
    except HTTPException:
        raise
    except Exception as e:
        return create_error_response(
            error=str(e),
            message="Failed to retrieve todo item"
        )


@router.put("/{todo_id}", response_model=TodoItemRead)
def update_todo(
    todo_id: int,
    todo_update: TodoItemUpdate,
    current_user: User = Depends(get_current_user),
    db_session: Session = Depends(get_session)
):
    """Update a specific todo item by ID"""
    try:
        updated_todo = TodoService.update_todo_item(
            todo_id=todo_id,
            user_id=current_user.id,
            todo_update=todo_update,
            db_session=db_session
        )
        
        if not updated_todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo item not found"
            )
        
        return create_success_response(
            data=updated_todo,
            message="Todo item updated successfully"
        )
    except HTTPException:
        raise
    except Exception as e:
        return create_error_response(
            error=str(e),
            message="Failed to update todo item"
        )


@router.patch("/{todo_id}/complete", response_model=TodoItemRead)
def update_todo_status(
    todo_id: int,
    status_update: TodoItemUpdateStatus,
    current_user: User = Depends(get_current_user),
    db_session: Session = Depends(get_session)
):
    """Update the completion status of a specific todo item"""
    try:
        updated_todo = TodoService.update_todo_status(
            todo_id=todo_id,
            user_id=current_user.id,
            status_update=status_update,
            db_session=db_session
        )
        
        if not updated_todo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo item not found"
            )
        
        return create_success_response(
            data=updated_todo,
            message="Todo item status updated successfully"
        )
    except HTTPException:
        raise
    except Exception as e:
        return create_error_response(
            error=str(e),
            message="Failed to update todo item status"
        )


@router.delete("/{todo_id}")
def delete_todo(
    todo_id: int,
    current_user: User = Depends(get_current_user),
    db_session: Session = Depends(get_session)
):
    """Delete a specific todo item by ID"""
    try:
        success = TodoService.delete_todo_item(
            todo_id=todo_id,
            user_id=current_user.id,
            db_session=db_session
        )
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo item not found"
            )
        
        return create_success_response(
            message="Todo item deleted successfully"
        )
    except HTTPException:
        raise
    except Exception as e:
        return create_error_response(
            error=str(e),
            message="Failed to delete todo item"
        )