# Todo API Backend

This is the backend for the Todo application, built with FastAPI and SQLModel.

## Features

- User authentication with JWT
- Secure task management with user isolation
- Full CRUD operations for tasks
- Task completion toggling
- RESTful API design

## Tech Stack

- Python 3.8+
- FastAPI
- SQLModel
- PostgreSQL (Neon Serverless)
- JWT for authentication
- Uvicorn ASGI server

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database URL and JWT secret
   ```
6. Run the application:
   ```bash
   uvicorn src.main:app --reload
   ```

## API Endpoints

### Authentication

- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get JWT token
- `POST /auth/logout` - Logout user

### Tasks

- `GET /api/{user_id}/tasks` - Get all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{task_id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{task_id}` - Update a task
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{task_id}/complete` - Toggle task completion status

## Environment Variables

- `DATABASE_URL` - PostgreSQL database URL
- `BETTER_AUTH_SECRET` - Secret key for JWT signing

## Running Tests

```bash
pytest tests/
```

## License

MIT