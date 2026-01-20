import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.db_session import get_sync_session
from sqlmodel import Session, create_engine
from sqlmodel.pool import StaticPool
from src.models.user import User
from src.models.task import Task
from unittest.mock import DependencyOverride


# Create a test database
@pytest.fixture(scope="module")
def test_db():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    # Create tables
    from src.models.user import User
    from src.models.task import Task
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(bind=engine)
    
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="module")
def client(test_db):
    def override_get_db():
        yield test_db
    
    app.dependency_overrides[get_sync_session] = override_get_db
    with TestClient(app) as c:
        yield c


def test_create_user(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "name": "Test User",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["user_id"]


def test_login_user(client):
    # First register a user
    client.post(
        "/auth/register",
        json={
            "email": "login@example.com",
            "name": "Login User",
            "password": "password123"
        }
    )
    
    # Then try to login
    response = client.post(
        "/auth/login",
        params={
            "email": "login@example.com",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


def test_create_task(client):
    # Register a user first
    response = client.post(
        "/auth/register",
        json={
            "email": "taskuser@example.com",
            "name": "Task User",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    user_data = response.json()
    user_id = user_data["user_id"]
    token = user_data["access_token"]
    
    # Create a task
    response = client.post(
        f"/api/{user_id}/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Test Task",
            "description": "This is a test task",
            "completed": False
        }
    )
    assert response.status_code == 200
    task_data = response.json()
    assert task_data["title"] == "Test Task"


def test_get_user_tasks(client):
    # Register a user first
    response = client.post(
        "/auth/register",
        json={
            "email": "getusertasks@example.com",
            "name": "Get Tasks User",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    user_data = response.json()
    user_id = user_data["user_id"]
    token = user_data["access_token"]
    
    # Create a task
    client.post(
        f"/api/{user_id}/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Another Test Task",
            "description": "This is another test task",
            "completed": False
        }
    )
    
    # Get user tasks
    response = client.get(
        f"/api/{user_id}/tasks",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) >= 1


def test_update_task(client):
    # Register a user first
    response = client.post(
        "/auth/register",
        json={
            "email": "updatetask@example.com",
            "name": "Update Task User",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    user_data = response.json()
    user_id = user_data["user_id"]
    token = user_data["access_token"]
    
    # Create a task
    response = client.post(
        f"/api/{user_id}/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Task to Update",
            "description": "Original description",
            "completed": False
        }
    )
    assert response.status_code == 200
    task_data = response.json()
    task_id = task_data["id"]
    
    # Update the task
    response = client.put(
        f"/api/{user_id}/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Updated Task",
            "description": "Updated description",
            "completed": True
        }
    )
    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["title"] == "Updated Task"
    assert updated_task["completed"] is True


def test_toggle_task_completion(client):
    # Register a user first
    response = client.post(
        "/auth/register",
        json={
            "email": "toggletask@example.com",
            "name": "Toggle Task User",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    user_data = response.json()
    user_id = user_data["user_id"]
    token = user_data["access_token"]
    
    # Create a task
    response = client.post(
        f"/api/{user_id}/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "title": "Task to Toggle",
            "description": "Task for toggling completion",
            "completed": False
        }
    )
    assert response.status_code == 200
    task_data = response.json()
    task_id = task_data["id"]
    
    # Toggle task completion
    response = client.patch(
        f"/api/{user_id}/tasks/{task_id}/complete",
        headers={"Authorization": f"Bearer {token}"},
        json={"completed": True}
    )
    assert response.status_code == 200
    toggled_task = response.json()
    assert toggled_task["completed"] is True