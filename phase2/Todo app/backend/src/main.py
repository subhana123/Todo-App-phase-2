from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer
from sqlmodel import Session
from typing import Optional
from .models.user import UserBase
from .services.user_service import UserService
from .auth.jwt_handler import create_access_token
from .db_session import get_sync_session
from .auth.middleware import jwt_middleware


app = FastAPI(title="Todo API", description="RESTful API for managing todo items with JWT authentication")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    # Add the JWT middleware
    request, call_next = await jwt_middleware(request, call_next)

    # Add database session
    request.state.db = next(get_sync_session())
    try:
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.post("/auth/register")
def register(user_data: UserBase, db: Session = Depends(get_sync_session)):
    user_service = UserService(db)

    # Check if user already exists
    existing_user = user_service.get_user_by_email(user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Create new user
    user = user_service.create_user(user_data)

    # Create access token
    token_data = {"sub": str(user.id), "email": user.email}
    access_token = create_access_token(data=token_data)

    return {"access_token": access_token, "token_type": "bearer", "user_id": user.id}


@app.post("/auth/login")
def login(email: str, password: str, db: Session = Depends(get_sync_session)):
    user_service = UserService(db)

    user = user_service.authenticate_user(email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    token_data = {"sub": str(user.id), "email": user.email}
    access_token = create_access_token(data=token_data)

    return {"access_token": access_token, "token_type": "bearer", "user_id": user.id}


@app.post("/auth/logout")
def logout(token: str = Depends(HTTPBearer())):
    # In a real implementation, you might add the token to a blacklist
    # For now, we just return a success message
    return {"message": "Logged out successfully"}


@app.get("/api/{user_id}/tasks")
def get_user_tasks(
    user_id: str,  # Changed to str to match the path parameter
    completed: Optional[bool] = None,
    request: Request = Request,  # This won't work - need to get user from JWT
    db: Session = Depends(get_sync_session)
):
    # Get the authenticated user ID from the request state (set by middleware)
    authenticated_user_id = getattr(request.state, 'user_id', None)

    # Verify that the requested user ID matches the authenticated user
    if authenticated_user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot access another user's tasks"
        )

    from .services.task_service import TaskService
    task_service = TaskService(db)

    tasks = task_service.get_tasks_by_user(user_id, completed)
    return tasks


@app.post("/api/{user_id}/tasks")
def create_task(
    user_id: str,
    task_data: TaskBase,
    request: Request = Request,
    db: Session = Depends(get_sync_session)
):
    # Get the authenticated user ID from the request state (set by middleware)
    authenticated_user_id = getattr(request.state, 'user_id', None)

    # Verify that the requested user ID matches the authenticated user
    if authenticated_user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot create tasks for another user"
        )

    from .services.task_service import TaskService
    task_service = TaskService(db)

    task = task_service.create_task(user_id, task_data)
    return task


@app.get("/api/{user_id}/tasks/{task_id}")
def get_task(
    user_id: str,
    task_id: str,  # Changed to str to match the path parameter
    request: Request = Request,
    db: Session = Depends(get_sync_session)
):
    # Get the authenticated user ID from the request state (set by middleware)
    authenticated_user_id = getattr(request.state, 'user_id', None)

    # Verify that the requested user ID matches the authenticated user
    if authenticated_user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot access another user's tasks"
        )

    from .services.task_service import TaskService
    task_service = TaskService(db)

    task = task_service.get_task_by_id(task_id, user_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/api/{user_id}/tasks/{task_id}")
def update_task(
    user_id: str,
    task_id: str,
    task_data: TaskBase,
    request: Request = Request,
    db: Session = Depends(get_sync_session)
):
    # Get the authenticated user ID from the request state (set by middleware)
    authenticated_user_id = getattr(request.state, 'user_id', None)

    # Verify that the requested user ID matches the authenticated user
    if authenticated_user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot update another user's tasks"
        )

    from .services.task_service import TaskService
    task_service = TaskService(db)

    task = task_service.update_task(task_id, user_id, task_data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/api/{user_id}/tasks/{task_id}")
def delete_task(
    user_id: str,
    task_id: str,
    request: Request = Request,
    db: Session = Depends(get_sync_session)
):
    # Get the authenticated user ID from the request state (set by middleware)
    authenticated_user_id = getattr(request.state, 'user_id', None)

    # Verify that the requested user ID matches the authenticated user
    if authenticated_user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot delete another user's tasks"
        )

    from .services.task_service import TaskService
    task_service = TaskService(db)

    success = task_service.delete_task(task_id, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}


@app.patch("/api/{user_id}/tasks/{task_id}/complete")
def toggle_task_completion(
    user_id: str,
    task_id: str,
    completed: bool,
    request: Request = Request,
    db: Session = Depends(get_sync_session)
):
    # Get the authenticated user ID from the request state (set by middleware)
    authenticated_user_id = getattr(request.state, 'user_id', None)

    # Verify that the requested user ID matches the authenticated user
    if authenticated_user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot update another user's tasks"
        )

    from .services.task_service import TaskService
    task_service = TaskService(db)

    task = task_service.toggle_completion(task_id, user_id, completed)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)