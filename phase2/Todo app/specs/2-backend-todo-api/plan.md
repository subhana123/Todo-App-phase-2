# Implementation Plan: Backend Todo API

**Feature Branch**: `2-backend-todo-api`
**Created**: 2026-01-17
**Status**: Draft
**Author**: Qwen Code Assistant

## Technical Context

- **Backend Framework**: FastAPI
- **ORM**: SQLModel
- **Authentication**: Better Auth with JWT
- **Database**: Neon Serverless PostgreSQL
- **Environment**: Windows OS with PowerShell
- **Project Location**: C:\Users\hma\Desktop\Todo app\phase2\Todo app
- **Current State**: Initial setup phase - backend folder structure needs to be created
- **Dependencies**: 
  - Python 3.8+
  - FastAPI
  - SQLModel
  - Better Auth
  - Neon PostgreSQL driver
  - PyJWT
  - python-dotenv
- **Integration Points**: Frontend will connect to these RESTful API endpoints

## Constitution Check

- **User-Centric Design**: API endpoints will follow RESTful conventions for intuitive usage
- **Data Persistence & Reliability**: Using Neon Serverless PostgreSQL for reliable data storage
- **Test-First (NON-NEGOTIABLE)**: Will implement tests for all endpoints and authentication flows
- **Responsive Cross-Platform Compatibility**: RESTful API will be accessible from any client
- **Privacy & Security**: JWT authentication required for all endpoints, user data isolation enforced
- **Performance Optimization**: Efficient database queries with proper indexing

## Gates

- ✅ Technology alignment: FastAPI, SQLModel, Better Auth, Neon PostgreSQL align with requirements
- ✅ Architecture compatibility: RESTful API architecture supports frontend integration
- ✅ Security compliance: JWT authentication and user data isolation planned
- ✅ Performance considerations: Proper indexing and query optimization planned
- ❌ Implementation readiness: Need to verify all dependencies are available and compatible

## Phase 0: Outline & Research

### Research Tasks

1. **Unknown: Better Auth JWT Integration**
   - Research: How to integrate Better Auth JWT plugin with FastAPI
   - Best Practices: Standard JWT implementation patterns in FastAPI
   - Patterns: Authentication middleware patterns for user identification

2. **Unknown: Neon PostgreSQL Connection**
   - Research: Best practices for connecting FastAPI to Neon Serverless PostgreSQL
   - Best Practices: Connection pooling and session management
   - Patterns: Async database operations in FastAPI

3. **Unknown: SQLModel Model Relationships**
   - Research: How to properly define User and Task models with foreign key relationships
   - Best Practices: Model validation and serialization patterns
   - Patterns: Many-to-one relationship between User and Task

4. **Unknown: Environment Configuration**
   - Research: Secure handling of environment variables (DATABASE_URL, BETTER_AUTH_SECRET)
   - Best Practices: Environment configuration patterns in FastAPI
   - Patterns: Configuration management for different environments

## Phase 1: Design & Contracts

### Data Model

#### User Model
- id: UUID (primary key)
- email: String (unique, indexed)
- name: String
- created_at: DateTime (default now)

#### Task Model
- id: UUID (primary key)
- user_id: UUID (foreign key to User.id, indexed)
- title: String (required)
- description: String (optional)
- completed: Boolean (default false)
- created_at: DateTime (default now)
- updated_at: DateTime (default now, auto-update)

### API Contracts

#### Authentication Endpoints
- POST /auth/login → Authenticate user and return JWT
- POST /auth/register → Register new user and return JWT
- POST /auth/logout → Logout user

#### Task Management Endpoints
- GET /api/{user_id}/tasks → List tasks for authenticated user
- POST /api/{user_id}/tasks → Create new task
- GET /api/{user_id}/tasks/{id} → Task details
- PUT /api/{user_id}/tasks/{id} → Update task
- DELETE /api/{user_id}/tasks/{id} → Delete task
- PATCH /api/{user_id}/tasks/{id}/complete → Toggle complete status

### Quickstart Guide

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables: `DATABASE_URL`, `BETTER_AUTH_SECRET`
4. Run database migrations: `alembic upgrade head`
5. Start the server: `uvicorn main:app --reload`
6. Access API at `http://localhost:8000`

## Phase 2: Implementation Plan

### Phase 2A: Setup
1. Create backend folder structure
2. Initialize FastAPI project
3. Add SQLModel ORM and Neon DB connection
4. Configure environment variables: DATABASE_URL, BETTER_AUTH_SECRET

### Phase 2B: Database Models
1. Define User model (id, email, name, created_at)
2. Define Task model (id, user_id FK, title, description, completed, timestamps)
3. Create migration scripts if needed
4. Ensure indexes on user_id and completed

### Phase 2C: Authentication
1. Integrate Better Auth JWT plugin
2. Configure JWT issuance and verification
3. Create middleware to extract user from token
4. Protect all /api endpoints

### Phase 2D: RESTful API
1. Implement GET /api/{user_id}/tasks → List tasks for authenticated user
2. Implement POST /api/{user_id}/tasks → Create new task
3. Implement GET /api/{user_id}/tasks/{id} → Task details
4. Implement PUT /api/{user_id}/tasks/{id} → Update task
5. Implement DELETE /api/{user_id}/tasks/{id} → Delete task
6. Implement PATCH /api/{user_id}/tasks/{id}/complete → Toggle complete
7. Add input validation and error handling
8. Ensure queries filter by authenticated user

### Phase 2E: Testing & Debug
1. Test JWT flow (valid/expired tokens)
2. Verify user isolation
3. Test CRUD functionality
4. Ensure database persistence in Neon
5. Verify proper HTTP status codes (200, 201, 401, 404, 422)

## Dependencies & Order

- Database models must be completed before API implementation
- Authentication must be completed before protected API endpoints
- Environment configuration must be set up before database connections

## Exit Criteria

- All endpoints functional and secure
- Users can only access their own tasks
- Backend fully documented and spec-aligned
- Ready for frontend integration
- All tests passing