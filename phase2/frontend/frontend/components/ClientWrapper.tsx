'use client';

import { SessionProvider } from 'next-auth/react';
import { AuthProvider } from '@/src/context/authcontext';
import { ReactNode } from 'react';
import Navbar from './auth/Navbar';

export default function ClientWrapper({ children }: { children: ReactNode }) {
  return (
    <SessionProvider>
      <AuthProvider>
        <div className="min-h-screen bg-gray-50">
          <Navbar />
          <main>
            {children}
          </main>
        </div>
      </AuthProvider>
    </SessionProvider>
  );
}