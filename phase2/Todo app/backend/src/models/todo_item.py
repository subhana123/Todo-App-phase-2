from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from enum import Enum

if TYPE_CHECKING:
    from .user import User


class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TodoItemBase(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    is_completed: bool = Field(default=False)
    due_date: Optional[datetime] = Field(default=None)
    priority: PriorityEnum = Field(default=PriorityEnum.medium)


class TodoItem(TodoItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    user_id: int = Field(foreign_key="user.id")

    # Relationship to User
    user: Optional["User"] = Relationship(back_populates="todo_items")


class TodoItemCreate(TodoItemBase):
    pass


class TodoItemRead(TodoItemBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user_id: int


class TodoItemUpdate(SQLModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    is_completed: Optional[bool] = None
    due_date: Optional[datetime] = Field(default=None)
    priority: Optional[PriorityEnum] = None


class TodoItemUpdateStatus(SQLModel):
    is_completed: bool