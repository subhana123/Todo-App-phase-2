# Quickstart Guide: Next.js Frontend with Better Auth Integration

## Prerequisites

- Node.js 18+ installed
- npm or yarn package manager
- Access to the FastAPI backend (from spec 2)
- Git for version control

## Setup Instructions

### 1. Clone and Navigate to Project Directory

```bash
git clone <repository-url>
cd frontend
```

### 2. Install Dependencies

```bash
npm install
# or
yarn install
```

### 3. Environment Configuration

Create a `.env.local` file in the project root with the following variables:

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:8000
```

Replace the URLs with your actual backend API and auth server URLs.

### 4. Run Development Server

```bash
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:3000`.

## Available Pages

- `/` - Home page (redirects to login if not authenticated)
- `/login` - User login page
- `/signup` - User registration page
- `/dashboard` - Task management dashboard (protected route)

## Building for Production

```bash
npm run build
npm run start
```

## Testing

Run the test suite:

```bash
npm run test
```

Or run tests in watch mode:

```bash
npm run test:watch
```

## Key Components

### Authentication Components
- `AuthProvider` - Manages authentication state throughout the app
- `ProtectedRoute` - Wrapper for pages requiring authentication
- `LoginForm` - Handles user login
- `SignupForm` - Handles user registration

### Task Management Components
- `TaskList` - Displays user's tasks
- `TaskForm` - Handles task creation and editing
- `TaskItem` - Individual task display with action buttons

### API Client
- `ApiClient` - Centralized HTTP client with JWT token management
- Interceptors for adding auth headers and handling errors
- Type-safe API functions for all backend endpoints