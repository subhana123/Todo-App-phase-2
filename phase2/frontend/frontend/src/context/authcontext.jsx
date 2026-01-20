'use client';

import { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true); // Add loading state

  useEffect(() => {
    // Initialize auth state after component mounts
    const initAuth = async () => {
      try {
        // In a real app, you would decode the JWT token to get user info
        const token = localStorage.getItem('jwt');

        if (token) {
          try {
            // Decode JWT token to get user info
            const tokenPayload = token.split('.')[1];
            const decodedPayload = JSON.parse(atob(tokenPayload));

            setUser(decodedPayload.user || { email: 'demo@example.com' });
          } catch (error) {
            console.error('Error decoding token:', error);
            setUser({ email: 'demo@example.com' }); // fallback
          }
        }
      } catch (error) {
        console.error('Error initializing auth:', error);
      } finally {
        setLoading(false); // Set loading to false after initialization
      }
    };

    initAuth();
  }, []);

  const login = (userData, token) => {
    localStorage.setItem('jwt', token);
    setUser(userData);
  };

  const logout = () => {
    localStorage.removeItem('jwt');
    setUser(null);
  };

  // Don't render children until auth is initialized
  if (loading) {
    return <div>Loading...</div>; // Or your preferred loading component
  }

  return (
    <AuthContext.Provider value={{ user, setUser, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
