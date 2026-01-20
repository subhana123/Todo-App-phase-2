# Implementation Plan: Next.js Frontend with Better Auth Integration

**Feature Branch**: `3-nextjs-frontend-auth`
**Created**: 2026-01-17
**Status**: Draft
**Author**: Qwen Code Assistant

## Technical Context

- **Frontend Framework**: Next.js 16+ with App Router
- **Authentication**: Better Auth frontend SDK
- **Styling**: Tailwind CSS or simple responsive CSS
- **Backend API**: FastAPI backend with JWT authentication (from spec 2)
- **Environment**: Windows OS with Node.js/npm
- **Project Location**: C:\Users\hma\Desktop\Todo app\phase2\Todo app\frontend
- **Current State**: Initial setup phase - frontend directory structure needs to be created
- **Dependencies**:
  - Node.js 18+
  - Next.js 16+
  - Better Auth
  - Tailwind CSS
  - Axios or Fetch API for HTTP requests
  - React Hook Form for form handling
  - Zod for form validation
- **Integration Points**: Connect to FastAPI backend for user authentication and task management

## Constitution Check

- **User-Centric Design**: UI will follow modern design principles with intuitive navigation and clear affordances
- **Data Persistence & Reliability**: UI will provide clear feedback on data operations and handle backend connectivity issues gracefully
- **Test-First (NON-NEGOTIABLE)**: Will implement tests for UI components and authentication flows
- **Responsive Cross-Platform Compatibility**: Will ensure responsive design works across desktop, tablet, and mobile devices
- **Privacy & Security**: Will securely handle JWT tokens and protect user data
- **Performance Optimization**: Will optimize bundle size and implement lazy loading where appropriate

## Gates

- ✅ Technology alignment: Next.js, Better Auth align with requirements
- ✅ Architecture compatibility: Next.js App Router supports required pages and routing
- ✅ Security compliance: Better Auth provides secure JWT handling
- ✅ Performance considerations: Next.js provides good performance out of the box
- ❌ Implementation readiness: Need to verify backend API endpoints are available and documented

## Phase 0: Outline & Research

### Research Tasks

1. **Unknown: Better Auth Integration with Next.js App Router**
   - Research: How to integrate Better Auth with Next.js App Router
   - Best Practices: Standard authentication patterns in Next.js
   - Patterns: Protected route implementations

2. **Unknown: JWT Token Storage Security**
   - Research: Best practices for storing JWT tokens in Next.js applications
   - Best Practices: HTTP-only cookies vs secure localStorage/sessionStorage
   - Patterns: Secure token handling patterns

3. **Unknown: API Client Implementation**
   - Research: Best practices for API clients in Next.js applications
   - Best Practices: Interceptors for JWT token attachment
   - Patterns: Error handling and request/response patterns

4. **Unknown: Responsive Design Implementation**
   - Research: Best practices for responsive design with Tailwind CSS
   - Best Practices: Mobile-first design approach
   - Patterns: Responsive layout patterns for task management UI

## Phase 1: Design & Contracts

### Data Model

#### UserSession Entity
- userId: string (unique identifier from auth system)
- email: string (user's email address)
- name: string (display name)
- accessToken: string (JWT token for API authentication)
- refreshToken: string (token for refreshing access token)
- expiresAt: Date (timestamp when access token expires)

#### TaskItem Entity
- id: string (unique identifier from backend)
- userId: string (foreign key to user)
- title: string (task title)
- description: string (optional task description)
- completed: boolean (completion status)
- createdAt: Date (timestamp when task was created)
- updatedAt: Date (timestamp when task was last updated)

#### APIClient Entity
- baseURL: string (backend API base URL)
- defaultHeaders: object (headers to include with all requests)
- interceptors: array (request/response interceptors for auth and error handling)

### API Contracts

#### Authentication Endpoints
- POST /auth/register → Register new user and return JWT
- POST /auth/login → Authenticate user and return JWT
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
2. Navigate to the frontend directory
3. Install dependencies: `npm install`
4. Set environment variables: `NEXT_PUBLIC_API_BASE_URL`, `NEXT_PUBLIC_BETTER_AUTH_URL`
5. Start the development server: `npm run dev`
6. Access the application at `http://localhost:3000`

## Phase 2: Implementation Plan

### Phase 2A: Project Setup
1. Create frontend folder structure
2. Initialize Next.js project with App Router
3. Install dependencies: Next.js, Better Auth, Tailwind CSS, Axios, React Hook Form, Zod
4. Configure environment variables for API and auth

### Phase 2B: Authentication UI
1. Create /signup page with form for email, name, and password
2. Create /login page with form for email and password
3. Integrate Better Auth flows for signup and login
4. Implement secure JWT token storage
5. Create protected route wrapper for dashboard access

### Phase 2C: Dashboard UI
1. Create /dashboard page layout
2. Implement task list component to display user's tasks
3. Create task form component for adding/editing tasks
4. Implement loading states and empty state UI

### Phase 2D: Task Actions
1. Implement create task functionality via API
2. Implement update task functionality via API
3. Implement delete task functionality via API
4. Implement toggle completion functionality via API
5. Add success/error state feedback

### Phase 2E: UX & Validation
1. Add loading states for all API operations
2. Implement comprehensive error handling
3. Create empty state UI for when no tasks exist
4. Ensure responsive layout across all device sizes
5. Add form validation for all user inputs

## Dependencies & Order

- Backend API (Spec 2) must be ready before frontend implementation
- Authentication system must be functional before protected routes
- Basic layout and routing must be set up before task components

## Exit Criteria

- User can fully manage tasks from browser
- Auth flow works end-to-end
- UI and backend fully integrated
- Ready for hackathon demo
- All tests passing
- Responsive design verified across devices