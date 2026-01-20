# Todo API Documentation

## Overview
This is a simple Todo application API built with FastAPI. It provides endpoints for managing todo items and user authentication.

## Base URL
`http://localhost:8000/api/v1`

## Authentication
The API uses JWT tokens for authentication. To access protected endpoints, include the token in the Authorization header as follows:
```
Authorization: Bearer <your-jwt-token>
```

## Endpoints

### User Management

#### Register a new user
- **POST** `/users/register`
- Request Body:
```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```
- Response: User object with ID, username, email, and timestamps

#### Login
- **POST** `/auth/token`
- Form Data:
  - `username`: string
  - `password`: string
- Response:
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

#### Get current user info
- **GET** `/auth/users/me`
- Headers: `Authorization: Bearer <token>`
- Response: User object

### Todo Operations

#### Get all todos
- **GET** `/todos/`
- Query Parameters:
  - `skip`: integer (default: 0)
  - `limit`: integer (default: 100)
- Response: Array of todo objects

#### Get a specific todo
- **GET** `/todos/{todo_id}`
- Path Parameter:
  - `todo_id`: integer
- Response: Single todo object

#### Create a new todo
- **POST** `/todos/`
- Request Body:
```json
{
  "title": "string",
  "description": "string or null",
  "completed": boolean
}
```
- Response: Created todo object

#### Update a todo
- **PUT** `/todos/{todo_id}`
- Path Parameter:
  - `todo_id`: integer
- Request Body:
```json
{
  "title": "string or null",
  "description": "string or null",
  "completed": "boolean or null"
}
```
- Response: Updated todo object

#### Delete a todo
- **DELETE** `/todos/{todo_id}`
- Path Parameter:
  - `todo_id`: integer
- Response: Success message

## Todo Object Structure
```json
{
  "id": integer,
  "title": string,
  "description": string or null,
  "completed": boolean,
  "created_at": "datetime string",
  "updated_at": "datetime string"
}
```

## User Object Structure
```json
{
  "id": integer,
  "username": string,
  "email": string,
  "created_at": "datetime string",
  "updated_at": "datetime string",
  "is_active": boolean
}
```

## Running the Application

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables in a `.env` file:
```
DATABASE_URL=postgresql://username:password@localhost/dbname
SECRET_KEY=your-super-secret-key-change-before-deployment
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=True
```

3. Initialize the database:
```bash
python init_db.py
```

4. Run the application:
```bash
python run_server.py
```

The API will be available at `http://localhost:8000`.

## API Documentation
Auto-generated API documentation is available at:
- `http://localhost:8000/docs` (Swagger UI)
- `http://localhost:8000/redoc` (ReDoc)