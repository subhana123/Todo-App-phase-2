# Tasks: Backend Todo API

**Feature Branch**: `2-backend-todo-api`
**Created**: 2026-01-17
**Status**: Draft
**Author**: Qwen Code Assistant

## Implementation Strategy

This document outlines the implementation tasks for the Backend Todo API. The approach follows an incremental delivery model where each user story builds upon the previous one, starting with the most critical functionality (secure access) and progressing to full CRUD operations.

The implementation will follow the priority order of user stories:
1. **User Story 1 (P1)**: Secure Todo Management - Establishes authentication and data isolation
2. **User Story 2 (P2)**: Todo CRUD Operations - Implements core functionality
3. **User Story 3 (P3)**: Todo Completion Operation - Adds status management

Each user story is designed to be independently testable, with the minimum viable product (MVP) achievable after completing User Story 1.

## Dependencies

- Database models must be completed before API implementation
- Authentication must be completed before protected API endpoints
- Environment configuration must be set up before database connections

## Parallel Execution Examples

Within each user story, the following tasks can be executed in parallel:
- Model creation and validation
- Service layer implementation
- Endpoint development
- Test creation

## Phase 1: Setup

### Goal
Initialize the project structure with all required dependencies and configurations.

- [X] T001 Create backend folder structure in `backend/src/`
- [X] T002 Initialize FastAPI project with proper directory structure
- [ ] T003 Install dependencies: FastAPI, SQLModel, Better Auth, psycopg2-binary, python-dotenv, pyjwt
- [X] T004 Configure environment variables: DATABASE_URL, BETTER_AUTH_SECRET in `.env` file
- [X] T005 Create requirements.txt with all project dependencies
- [X] T006 Set up database connection configuration using SQLModel and Neon PostgreSQL

## Phase 2: Foundational

### Goal
Establish the foundational components required for all user stories: database models, authentication system, and middleware.

- [X] T007 Create User model with id, email, name, created_at fields in `backend/src/models/user.py`
- [X] T008 Create Task model with id, user_id, title, description, completed, timestamps in `backend/src/models/task.py`
- [X] T009 Implement foreign key relationship between User and Task models
- [X] T010 Add proper indexes on user_id and completed fields in Task model
- [X] T011 Implement database session management with async context managers
- [X] T012 Integrate Better Auth JWT plugin with FastAPI
- [X] T013 Configure JWT issuance and verification
- [X] T014 Create middleware to extract user from JWT token
- [X] T015 Protect all /api endpoints with authentication middleware
- [X] T016 Implement database migration setup with Alembic

## Phase 3: User Story 1 - Secure Todo Management (Priority: P1)

### Goal
Enable registered users to securely access the todo application via a RESTful API with confidence that their data is protected and isolated from other users.

### Independent Test Criteria
Can be fully tested by authenticating with a valid JWT token, creating todo items, and verifying that I can only access my own items and not those of other users.

- [X] T017 [US1] Implement POST /auth/register endpoint to register new users
- [X] T018 [US1] Implement POST /auth/login endpoint to authenticate users and return JWT
- [X] T019 [US1] Implement POST /auth/logout endpoint to logout users
- [X] T020 [US1] Create UserService for user-related operations in `backend/src/services/user_service.py`
- [X] T021 [US1] Implement GET /api/{user_id}/tasks endpoint to list user's tasks
- [X] T022 [US1] Add validation to ensure users can only access their own tasks
- [X] T023 [US1] Test JWT authentication with valid tokens
- [ ] T024 [US1] Test JWT authentication with invalid or expired tokens
- [X] T025 [US1] Verify user data isolation by testing cross-user access attempts

## Phase 4: User Story 2 - Todo CRUD Operations (Priority: P2)

### Goal
Allow authenticated users to perform all CRUD operations (Create, Read, Update, Delete) on their todo items to fully manage their task list.

### Independent Test Criteria
Can be fully tested by performing all CRUD operations on todo items within a single user session and verifying they work correctly with proper HTTP status codes.

- [X] T026 [US2] Implement POST /api/{user_id}/tasks endpoint to create new tasks
- [X] T027 [US2] Implement GET /api/{user_id}/tasks/{id} endpoint to retrieve task details
- [X] T028 [US2] Implement PUT /api/{user_id}/tasks/{id} endpoint to update tasks
- [X] T029 [US2] Implement DELETE /api/{user_id}/tasks/{id} endpoint to delete tasks
- [X] T030 [US2] Create TaskService for task-related operations in `backend/src/services/task_service.py`
- [X] T031 [US2] Add input validation for all task operations
- [X] T032 [US2] Ensure proper HTTP status codes (200, 201, 204, 401, 404, 422) are returned
- [X] T033 [US2] Test CRUD operations with valid data
- [ ] T034 [US2] Test CRUD operations with invalid data to ensure 422 responses
- [X] T035 [US2] Verify that users can only modify their own tasks

## Phase 5: User Story 3 - Todo Completion Operation (Priority: P3)

### Goal
Allow authenticated users to mark their todo items as complete/incomplete to track progress and organize tasks.

### Independent Test Criteria
Can be fully tested by marking todo items as complete/incomplete and verifying the status updates correctly.

- [X] T036 [US3] Implement PATCH /api/{user_id}/tasks/{id}/complete endpoint to toggle completion status
- [X] T037 [US3] Update TaskService to handle completion status changes
- [X] T038 [US3] Add validation to ensure completion status updates work correctly
- [X] T039 [US3] Test completion status changes from pending to complete
- [X] T040 [US3] Test completion status changes from complete to pending
- [X] T041 [US3] Verify that only the task owner can update completion status

## Phase 6: Testing & Debug

### Goal
Validate the complete system with comprehensive tests covering all functionality and edge cases.

- [ ] T042 Test JWT flow with valid and expired tokens
- [ ] T043 Verify user isolation across all endpoints
- [X] T044 Test CRUD functionality for all operations
- [ ] T045 Ensure database persistence works correctly in Neon
- [X] T046 Verify proper HTTP status codes across all endpoints
- [ ] T047 Test edge case: user trying to access another user's todo data
- [ ] T048 Test edge case: system handling malformed JWT tokens
- [ ] T049 Test edge case: user JWT token expiring during a request
- [ ] T050 Test edge case: invalid input sent to todo endpoints
- [ ] T051 Test edge case: user trying to update/delete non-existent todo item
- [ ] T052 Run all tests and ensure they pass
- [ ] T053 Perform integration testing of the complete system

## Phase 7: Polish & Cross-Cutting Concerns

### Goal
Complete the implementation with documentation, error handling, and final quality checks.

- [ ] T054 Add comprehensive error handling and logging
- [X] T055 Document all API endpoints with examples
- [ ] T056 Add rate limiting for security
- [ ] T057 Perform final security review
- [X] T058 Update README with setup and usage instructions
- [ ] T059 Run final tests to ensure all functionality works as expected