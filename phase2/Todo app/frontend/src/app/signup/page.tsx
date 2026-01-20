'use client';

import { useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { useUserSession } from '@/src/contexts/UserSessionContext';
import { useSignupForm } from '@/src/lib/formValidation';
import SignupForm from '@/src/components/SignupForm';

const SignupPage = () => {
  const { register: registerUser } = useUserSession();
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  const handleSignup = async (data: { email: string; name: string; password: string }) => {
    try {
      setError(null);
      await registerUser(data.email, data.name, data.password);
      // Redirect to dashboard after successful registration
      router.push('/dashboard');
    } catch (err: any) {
      setError(err.message || 'An error occurred during registration');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-md w-full space-y-8">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Create your account
          </h2>
        </div>
        <SignupForm onSubmit={handleSignup} />
        {error && (
          <div className="rounded-md bg-red-50 p-4 mt-4">
            <div className="flex">
              <div className="ml-3">
                <h3 className="text-sm font-medium text-red-800">{error}</h3>
              </div>
            </div>
          </div>
        )}
        <p className="mt-2 text-center text-sm text-gray-600">
          Already have an account?{' '}
          <Link href="/login" className="font-medium text-indigo-600 hover:text-indigo-500">
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
};

export default SignupPage;