import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    // Forward the request to the backend
    const backendResponse = await fetch('http://localhost:8000/api/v1/auth/logout', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        // You might need to include authentication headers here if the user is logged in
        // Authorization: `Bearer ${token}`, // if using bearer tokens
      },
    });

    // Get the response data from the backend
    const data = await backendResponse.json();

    // Return the response from the backend
    return NextResponse.json(data, {
      status: backendResponse.status,
    });
  } catch (error) {
    console.error('Logout API route error:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}