'use client';

import { signOut } from 'next-auth/react';
import { useRouter } from 'next/navigation';

interface LogoutButtonProps {
  children: React.ReactNode;
  redirectUrl?: string;
}

export default function LogoutButton({ 
  children, 
  redirectUrl = '/login' 
}: LogoutButtonProps) {
  const router = useRouter();

  const handleSignOut = async () => {
    await signOut({ redirect: false }); // Don't redirect immediately
    router.push(redirectUrl); // Redirect after signing out
    router.refresh(); // Refresh to update session state
  };

  return (
    <button onClick={handleSignOut}>
      {children}
    </button>
  );
}