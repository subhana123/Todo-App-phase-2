// Test to verify the authentication implementation
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { SessionProvider } from 'next-auth/react';
import LoginPage from './app/login/page';
import RegisterPage from './app/register/page';
import ProtectedRoute from './components/auth/ProtectedRoute';

// Mock next-auth
jest.mock('next-auth/react', () => ({
  useSession: jest.fn(() => ({ data: null, status: 'unauthenticated' })),
  signIn: jest.fn(),
}));

describe('Authentication System Tests', () => {
  test('Login page renders correctly', () => {
    render(
      <SessionProvider>
        <LoginPage />
      </SessionProvider>
    );
    
    expect(screen.getByText(/sign in to your account/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/email address/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /sign in/i })).toBeInTheDocument();
  });

  test('Register page renders correctly', () => {
    render(
      <SessionProvider>
        <RegisterPage />
      </SessionProvider>
    );
    
    expect(screen.getByText(/create your account/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/full name/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/email address/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/confirm password/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /create account/i })).toBeInTheDocument();
  });

  test('ProtectedRoute redirects when unauthenticated', () => {
    const { container } = render(
      <SessionProvider>
        <ProtectedRoute fallbackUrl="/login">
          <div>Protected Content</div>
        </ProtectedRoute>
      </SessionProvider>
    );
    
    // When unauthenticated, the protected content shouldn't render
    expect(container.firstChild).not.toHaveTextContent('Protected Content');
  });

  test('Form validation works on login page', async () => {
    render(
      <SessionProvider>
        <LoginPage />
      </SessionProvider>
    );
    
    const emailInput = screen.getByLabelText(/email address/i);
    const passwordInput = screen.getByLabelText(/password/i);
    const submitButton = screen.getByRole('button', { name: /sign in/i });
    
    // Enter invalid email
    fireEvent.change(emailInput, { target: { value: 'invalid-email' } });
    fireEvent.change(passwordInput, { target: { value: '12345' } }); // Too short
    fireEvent.click(submitButton);
    
    await waitFor(() => {
      expect(screen.getByText(/please enter a valid email address/i)).toBeInTheDocument();
      expect(screen.getByText(/password must be at least 6 characters/i)).toBeInTheDocument();
    });
  });
});