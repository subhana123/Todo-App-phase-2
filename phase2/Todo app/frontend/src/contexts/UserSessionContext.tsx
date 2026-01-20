'use client';

import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { getUser, signIn, signOut } from '../lib/auth';

// Define the shape of our user session
interface UserSession {
  userId: string;
  email: string;
  name: string;
  accessToken: string;
  refreshToken?: string;
  expiresAt: Date;
}

// Define the context type
interface UserSessionContextType {
  user: UserSession | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, name: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  isAuthenticated: boolean;
}

// Create the context with default values
const UserSessionContext = createContext<UserSessionContextType | undefined>(undefined);

// Provider component
export const UserSessionProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<UserSession | null>(null);
  const [loading, setLoading] = useState(true);

  // Check if user is already logged in on initial load
  useEffect(() => {
    const checkAuthStatus = async () => {
      try {
        const userData = await getUser();
        if (userData) {
          setUser({
            userId: userData.userId,
            email: userData.email,
            name: userData.name,
            accessToken: userData.accessToken,
            refreshToken: userData.refreshToken,
            expiresAt: new Date(userData.expiresAt),
          });
        }
      } catch (error) {
        console.error('Error checking auth status:', error);
      } finally {
        setLoading(false);
      }
    };

    checkAuthStatus();
  }, []);

  const login = async (email: string, password: string) => {
    try {
      const userData = await signIn(email, password);
      setUser({
        userId: userData.userId,
        email: userData.email,
        name: userData.name,
        accessToken: userData.accessToken,
        refreshToken: userData.refreshToken,
        expiresAt: new Date(userData.expiresAt),
      });
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  };

  const register = async (email: string, name: string, password: string) => {
    try {
      // In a real implementation, this would call the register API
      // For now, we'll simulate a successful registration and login
      const userData = await signIn(email, password); // Assuming sign in after registration
      setUser({
        userId: userData.userId,
        email: userData.email,
        name: userData.name,
        accessToken: userData.accessToken,
        refreshToken: userData.refreshToken,
        expiresAt: new Date(userData.expiresAt),
      });
    } catch (error) {
      console.error('Registration error:', error);
      throw error;
    }
  };

  const logout = async () => {
    try {
      await signOut();
      setUser(null);
    } catch (error) {
      console.error('Logout error:', error);
      throw error;
    }
  };

  const isAuthenticated = !!user;

  return (
    <UserSessionContext.Provider
      value={{
        user,
        loading,
        login,
        register,
        logout,
        isAuthenticated,
      }}
    >
      {children}
    </UserSessionContext.Provider>
  );
};

// Custom hook to use the UserSession context
export const useUserSession = () => {
  const context = useContext(UserSessionContext);
  if (context === undefined) {
    throw new Error('useUserSession must be used within a UserSessionProvider');
  }
  return context;
};