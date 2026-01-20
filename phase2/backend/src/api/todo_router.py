from fastapi import APIRouter, HTTPException, Depends
from typing import List
from src.models.todo_model import TodoCreate, TodoUpdate, TodoResponse
from src.services.todo_service import TodoService
from src.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[TodoResponse])
async def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all todos"""
    todos = await TodoService.get_todos(db, skip=skip, limit=limit)
    return todos


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a specific todo by ID"""
    todo = await TodoService.get_todo_by_id(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.post("/", response_model=TodoResponse)
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """Create a new todo"""
    new_todo = await TodoService.create_todo(db, todo)
    return new_todo


@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: int, todo_update: TodoUpdate, db: Session = Depends(get_db)):
    """Update a specific todo by ID"""
    updated_todo = await TodoService.update_todo(db, todo_id, todo_update)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated_todo


@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    """Delete a specific todo by ID"""
    deleted = await TodoService.delete_todo(db, todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}