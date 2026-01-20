'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useUserSession } from '@/src/contexts/UserSessionContext';

interface ProtectedRouteProps {
  children: React.ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children }) => {
  const { isAuthenticated, loading } = useUserSession();
  const router = useRouter();

  useEffect(() => {
    if (!loading && !isAuthenticated) {
      // Redirect to login if not authenticated
      router.push('/login');
    }
  }, [isAuthenticated, loading, router]);

  // Show nothing while checking authentication status
  if (loading) {
    return <div>Loading...</div>;
  }

  // If authenticated, render the child components
  if (isAuthenticated) {
    return <>{children}</>;
  }

  // If not authenticated and not loading, return null (router.push should handle redirection)
  return null;
};

export default ProtectedRoute;