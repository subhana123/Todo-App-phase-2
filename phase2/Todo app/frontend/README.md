# Todo App Frontend

This is the frontend for the Todo application, built with Next.js and integrated with Better Auth for authentication.

## Features

- User authentication (sign up, sign in, sign out)
- Secure JWT-based communication with backend
- Task management (create, read, update, delete, toggle completion)
- Responsive design for all device sizes
- Form validation
- Loading and error states

## Tech Stack

- Next.js 14 with App Router
- React 18
- TypeScript
- Tailwind CSS
- Better Auth for authentication
- Axios for API requests
- React Hook Form + Zod for form validation

## Setup

1. Clone the repository
2. Navigate to the frontend directory
3. Install dependencies:
   ```bash
   npm install
   ```
4. Set environment variables:
   ```bash
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
   NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:8000
   ```
5. Start the development server:
   ```bash
   npm run dev
   ```

## Environment Variables

- `NEXT_PUBLIC_API_BASE_URL` - Base URL for the backend API
- `NEXT_PUBLIC_BETTER_AUTH_URL` - Base URL for the auth service

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run linter

## Project Structure

```
frontend/
├── src/
│   ├── app/                 # Next.js App Router pages
│   │   ├── login/
│   │   ├── signup/
│   │   └── dashboard/
│   ├── components/          # Reusable UI components
│   ├── contexts/            # React contexts (e.g., UserSessionContext)
│   ├── hooks/               # Custom React hooks
│   ├── lib/                 # Utilities and shared functions
│   ├── services/            # API service functions
│   └── validation/          # Form validation schemas
├── public/                  # Static assets
├── package.json
└── tailwind.config.js
```

## Key Components

### Authentication Components
- `UserSessionContext` - Manages authentication state throughout the app
- `ProtectedRoute` - Wrapper for pages requiring authentication
- `LoginForm` - Handles user login
- `SignupForm` - Handles user registration

### Task Management Components
- `TaskList` - Displays user's tasks
- `TaskForm` - Handles task creation and editing
- `TaskItem` - Individual task display with action buttons

### API Client
- `apiClient` - Centralized HTTP client with JWT token management
- Interceptors for adding auth headers and handling errors
- Type-safe API functions for all backend endpoints

## API Integration

The frontend communicates with the backend API through service functions in `src/services/`. All authenticated requests automatically include the JWT token via an Axios interceptor.

## Security

- JWT tokens are stored securely in localStorage
- All API requests include authentication headers
- Protected routes ensure only authenticated users can access certain pages
- Form inputs are validated both client-side and server-side