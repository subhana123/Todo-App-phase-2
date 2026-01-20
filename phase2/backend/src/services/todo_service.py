from sqlalchemy.orm import Session
from src.db.todo_db_model import Todo
from src.models.todo_model import TodoCreate, TodoUpdate


class TodoService:
    @staticmethod
    async def get_todos(db: Session, skip: int = 0, limit: int = 100):
        todos = db.query(Todo).offset(skip).limit(limit).all()
        return todos

    @staticmethod
    async def get_todo_by_id(db: Session, todo_id: int):
        return db.query(Todo).filter(Todo.id == todo_id).first()

    @staticmethod
    async def create_todo(db: Session, todo: TodoCreate):
        db_todo = Todo(**todo.dict())
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

    @staticmethod
    async def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate):
        db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if not db_todo:
            return None
        
        update_data = todo_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_todo, field, value)
        
        db.commit()
        db.refresh(db_todo)
        return db_todo

    @staticmethod
    async def delete_todo(db: Session, todo_id: int):
        db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
        if not db_todo:
            return False
        
        db.delete(db_todo)
        db.commit()
        return True