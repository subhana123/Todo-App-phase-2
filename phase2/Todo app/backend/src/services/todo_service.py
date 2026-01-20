from sqlmodel import Session, select
from typing import List, Optional
from ..models.todo_item import TodoItem, TodoItemCreate, TodoItemUpdate, TodoItemUpdateStatus
from ..models.user import User
from ..utils.errors import TodoException


class TodoService:
    """Service class for todo-related operations"""
    
    @classmethod
    def create_todo_item(cls, todo_create: TodoItemCreate, user_id: int, db_session: Session) -> TodoItem:
        """Create a new todo item for a user"""
        todo_item = TodoItem(
            title=todo_create.title,
            description=todo_create.description,
            is_completed=todo_create.is_completed,
            due_date=todo_create.due_date,
            priority=todo_create.priority,
            user_id=user_id
        )
        
        db_session.add(todo_item)
        db_session.commit()
        db_session.refresh(todo_item)
        
        return todo_item
    
    @classmethod
    def get_todo_item_by_id(cls, todo_id: int, user_id: int, db_session: Session) -> Optional[TodoItem]:
        """Get a specific todo item by ID for a user"""
        todo_item = db_session.get(TodoItem, todo_id)
        
        if todo_item is None:
            return None
        
        # Ensure the todo item belongs to the requesting user
        if todo_item.user_id != user_id:
            raise TodoException(
                detail="Access denied: You can only access your own todo items",
                status_code=403
            )
        
        return todo_item
    
    @classmethod
    def get_todo_items_for_user(
        cls, 
        user_id: int, 
        db_session: Session, 
        skip: int = 0, 
        limit: int = 20,
        status_filter: Optional[str] = None
    ) -> List[TodoItem]:
        """Get all todo items for a user with optional filtering and pagination"""
        query = select(TodoItem).where(TodoItem.user_id == user_id)
        
        # Apply status filter if provided
        if status_filter:
            if status_filter.lower() == "completed":
                query = query.where(TodoItem.is_completed == True)
            elif status_filter.lower() == "pending":
                query = query.where(TodoItem.is_completed == False)
        
        # Apply pagination
        query = query.offset(skip).limit(limit)
        
        todo_items = db_session.exec(query).all()
        return todo_items
    
    @classmethod
    def update_todo_item(
        cls, 
        todo_id: int, 
        user_id: int, 
        todo_update: TodoItemUpdate, 
        db_session: Session
    ) -> Optional[TodoItem]:
        """Update a todo item for a user"""
        todo_item = cls.get_todo_item_by_id(todo_id, user_id, db_session)
        
        if todo_item is None:
            return None
        
        # Update fields that are provided
        update_data = todo_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(todo_item, field, value)
        
        db_session.add(todo_item)
        db_session.commit()
        db_session.refresh(todo_item)
        
        return todo_item
    
    @classmethod
    def update_todo_status(
        cls, 
        todo_id: int, 
        user_id: int, 
        status_update: TodoItemUpdateStatus, 
        db_session: Session
    ) -> Optional[TodoItem]:
        """Update the completion status of a todo item for a user"""
        todo_item = cls.get_todo_item_by_id(todo_id, user_id, db_session)
        
        if todo_item is None:
            return None
        
        todo_item.is_completed = status_update.is_completed
        
        db_session.add(todo_item)
        db_session.commit()
        db_session.refresh(todo_item)
        
        return todo_item
    
    @classmethod
    def delete_todo_item(cls, todo_id: int, user_id: int, db_session: Session) -> bool:
        """Delete a todo item for a user"""
        todo_item = cls.get_todo_item_by_id(todo_id, user_id, db_session)
        
        if todo_item is None:
            return False
        
        db_session.delete(todo_item)
        db_session.commit()
        
        return True