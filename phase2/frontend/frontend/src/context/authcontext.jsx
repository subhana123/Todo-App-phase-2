'use client';

import { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // In a real app, you would decode the JWT token to get user info
    const token = localStorage.getItem('jwt');

    if (token) {
      try {
        // Decode JWT token to get user info
        const tokenPayload = token.split('.')[1];
        const decodedPayload = JSON.parse(atob(tokenPayload));

        // Using setTimeout to defer the state update to the next tick
        // This avoids the synchronous setState warning
        const timer = setTimeout(() => {
          setUser(decodedPayload.user || { email: 'demo@example.com' });
        }, 0);

        return () => clearTimeout(timer);
      } catch (error) {
        console.error('Error decoding token:', error);

        // Using setTimeout to defer the state update to the next tick
        // This avoids the synchronous setState warning
        const timer = setTimeout(() => {
          setUser({ email: 'demo@example.com' }); // fallback
        }, 0);

        return () => clearTimeout(timer);
      }
    }
  }, []);

  const login = (userData, token) => {
    localStorage.setItem('jwt', token);
    setUser(userData);
  };

  const logout = () => {
    localStorage.removeItem('jwt');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, setUser, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
