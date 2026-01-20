'use client';

import { useSession } from 'next-auth/react';
import { ReactNode } from 'react';
import { useRouter } from 'next/navigation';

interface ProtectedRouteProps {
  children: ReactNode;
  fallbackUrl?: string; // URL to redirect to if not authenticated
}

export default function ProtectedRoute({
  children,
  fallbackUrl = '/login'
}: ProtectedRouteProps) {
  const { status } = useSession();
  const router = useRouter();

  // If loading, show a loading indicator
  if (status === 'loading') {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  // If not authenticated, redirect to login
  if (status === 'unauthenticated') {
    router.push(fallbackUrl);
    return null; // Return null to prevent rendering children
  }

  // If authenticated, render children
  return <>{children}</>;
}