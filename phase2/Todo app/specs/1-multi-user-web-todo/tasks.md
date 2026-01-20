---

description: "Task list template for feature implementation"
---

# Tasks: Multi-User Web Todo Application

**Input**: Design documents from `/specs/1-multi-user-web-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure with backend and frontend directories
- [X] T002 [P] Initialize backend with FastAPI dependencies
- [X] T003 [P] Initialize frontend with Next.js dependencies
- [X] T004 [P] Configure linting and formatting tools for both backend and frontend

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T005 Setup database schema and migrations framework with SQLModel
- [X] T006 [P] Configure Neon PostgreSQL connection pool
- [X] T007 [P] Setup Better Auth for JWT-based authentication
- [X] T008 Create base models/entities that all stories depend on
- [X] T009 Configure error handling and logging infrastructure
- [X] T010 Setup environment configuration management
- [X] T011 Create API response utility functions

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Multi-User Todo Management (Priority: P1) 🎯 MVP

**Goal**: Enable registered users to securely log into the todo application and manage their personal todo list with data isolation

**Independent Test**: Can be fully tested by registering a new user account, logging in, creating todo items, viewing them, updating them, marking them as complete, and deleting them - all while ensuring another user cannot access these items.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T012 [P] [US1] Contract test for /auth/register endpoint in backend/tests/contract/test_auth.py
- [ ] T013 [P] [US1] Contract test for /auth/login endpoint in backend/tests/contract/test_auth.py
- [ ] T014 [P] [US1] Integration test for user registration flow in backend/tests/integration/test_user_flow.py

### Implementation for User Story 1

- [X] T015 [P] [US1] Create User model in backend/src/models/user.py
- [X] T016 [P] [US1] Create TodoItem model in backend/src/models/todo_item.py
- [X] T017 [US1] Implement UserService in backend/src/services/user_service.py (depends on T015)
- [X] T018 [US1] Implement TodoService in backend/src/services/todo_service.py (depends on T015, T016)
- [X] T019 [US1] Implement authentication endpoints in backend/src/api/auth.py
- [X] T020 [US1] Implement authorization middleware to ensure data isolation in backend/src/middleware/auth.py
- [ ] T021 [US1] Add user registration and login pages in frontend/src/pages/auth/
- [ ] T022 [US1] Create user profile/dashboard page in frontend/src/pages/dashboard.js
- [ ] T023 [US1] Add authentication context/state management in frontend/src/context/auth.js

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Todo Operations (Priority: P2)

**Goal**: Allow logged-in users to perform all five core todo operations (Add, View, Update, Delete, Complete)

**Independent Test**: Can be fully tested by performing all five operations on todo items within a single user session and verifying they work correctly.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T024 [P] [US2] Contract test for /todos GET endpoint in backend/tests/contract/test_todos.py
- [ ] T025 [P] [US2] Contract test for /todos POST endpoint in backend/tests/contract/test_todos.py
- [ ] T026 [P] [US2] Integration test for full todo CRUD operations in backend/tests/integration/test_todo_crud.py

### Implementation for User Story 2

- [X] T027 [P] [US2] Implement /todos GET endpoint in backend/src/api/todos.py (depends on T015, T016)
- [X] T028 [P] [US2] Implement /todos POST endpoint in backend/src/api/todos.py (depends on T015, T016)
- [X] T029 [US2] Implement /todos/{id} PUT endpoint in backend/src/api/todos.py (depends on T015, T016)
- [X] T030 [US2] Implement /todos/{id} DELETE endpoint in backend/src/api/todos.py (depends on T015, T016)
- [X] T031 [US2] Implement /todos/{id}/complete PATCH endpoint in backend/src/api/todos.py (depends on T015, T016)
- [ ] T032 [US2] Create TodoForm component in frontend/src/components/TodoForm.js
- [ ] T033 [US2] Create TodoList component in frontend/src/components/TodoList.js
- [ ] T034 [US2] Create TodoItem component in frontend/src/components/TodoItem.js
- [ ] T035 [US2] Integrate todo operations with backend API in frontend/src/services/todoApi.js

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Secure Authentication & Authorization (Priority: P3)

**Goal**: Ensure JWT-based authentication is secure and user data remains private

**Independent Test**: Can be fully tested by verifying that JWT tokens are issued upon login, validated on protected routes, and that unauthorized access attempts are rejected.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T036 [P] [US3] Contract test for /auth/logout endpoint in backend/tests/contract/test_auth.py
- [ ] T037 [P] [US3] Integration test for JWT token validation in backend/tests/integration/test_auth.py
- [ ] T038 [P] [US3] Security test for data isolation in backend/tests/security/test_data_isolation.py

### Implementation for User Story 3

- [X] T039 [P] [US3] Implement logout endpoint in backend/src/api/auth.py
- [X] T040 [US3] Enhance JWT token validation middleware in backend/src/middleware/auth.py
- [ ] T041 [US3] Implement refresh token functionality in backend/src/auth/token_manager.py
- [ ] T042 [US3] Add token expiration handling in frontend/src/services/authApi.js
- [ ] T043 [US3] Implement automatic token refresh in frontend/src/hooks/useAuth.js
- [X] T044 [US3] Add security headers to API responses in backend/src/main.py
- [ ] T045 [US3] Implement rate limiting for auth endpoints in backend/src/middleware/rate_limit.py

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T046 [P] Documentation updates in docs/
- [ ] T047 Code cleanup and refactoring
- [ ] T048 Performance optimization across all stories
- [ ] T049 [P] Additional unit tests (if requested) in backend/tests/unit/ and frontend/tests/
- [ ] T050 Security hardening
- [ ] T051 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for /auth/register endpoint in backend/tests/contract/test_auth.py"
Task: "Contract test for /auth/login endpoint in backend/tests/contract/test_auth.py"
Task: "Integration test for user registration flow in backend/tests/integration/test_user_flow.py"

# Launch all models for User Story 1 together:
Task: "Create User model in backend/src/models/user.py"
Task: "Create TodoItem model in backend/src/models/todo_item.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence