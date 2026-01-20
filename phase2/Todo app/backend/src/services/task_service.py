from sqlmodel import Session, select
from typing import Optional, List
from uuid import UUID
from ..models.task import Task, TaskBase
from ..models.user import User


class TaskService:
    def __init__(self, session: Session):
        self.session = session

    def create_task(self, user_id: UUID, task_data: TaskBase) -> Task:
        db_task = Task(
            title=task_data.title,
            description=task_data.description,
            completed=task_data.completed,
            user_id=user_id
        )
        self.session.add(db_task)
        self.session.commit()
        self.session.refresh(db_task)
        return db_task

    def get_tasks_by_user(self, user_id: UUID, completed: Optional[bool] = None) -> List[Task]:
        query = select(Task).where(Task.user_id == user_id)
        
        if completed is not None:
            query = query.where(Task.completed == completed)
            
        tasks = self.session.exec(query).all()
        return tasks

    def get_task_by_id(self, task_id: UUID, user_id: UUID) -> Optional[Task]:
        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        task = self.session.exec(statement).first()
        return task

    def update_task(self, task_id: UUID, user_id: UUID, task_data: TaskBase) -> Optional[Task]:
        task = self.get_task_by_id(task_id, user_id)
        if not task:
            return None
        
        # Update task attributes
        task.title = task_data.title
        task.description = task_data.description
        task.completed = task_data.completed
        
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task

    def delete_task(self, task_id: UUID, user_id: UUID) -> bool:
        task = self.get_task_by_id(task_id, user_id)
        if not task:
            return False
        
        self.session.delete(task)
        self.session.commit()
        return True

    def toggle_completion(self, task_id: UUID, user_id: UUID, completed: bool) -> Optional[Task]:
        task = self.get_task_by_id(task_id, user_id)
        if not task:
            return None
        
        task.completed = completed
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        return task