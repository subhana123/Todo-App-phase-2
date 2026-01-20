'use client';

import Link from 'next/link';
import { useSession, signOut } from 'next-auth/react';
import { useAuth } from '@/src/context/authcontext';

export default function Navbar() {
  const { data: session } = useSession();
  const { user } = useAuth();

  return (
    <nav className="bg-indigo-600 text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        <Link href="/" className="text-xl font-bold">
          Todo App
        </Link>

        <div>
          {session ? (
            <div className="flex items-center space-x-4">
              <span>Hello, {session.user?.name || session.user?.email}</span>
              <button
                onClick={() => signOut()}
                className="bg-red-500 hover:bg-red-600 px-4 py-2 rounded"
              >
                Sign Out
              </button>
            </div>
          ) : (
            <div className="flex space-x-4">
              <Link href="/login" className="hover:underline">
                Login
              </Link>
              <Link href="/register" className="hover:underline">
                Register
              </Link>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
}