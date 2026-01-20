import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  try {
    // Get the request body
    const body = await request.json();

    // Forward the request to the backend using the environment variable
    const backendResponse = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/v1/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    });

    // Get the response data from the backend
    const data = await backendResponse.json();

    // Return the response from the backend
    return NextResponse.json(data, {
      status: backendResponse.status,
    });
  } catch (error) {
    console.error('Register API route error:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}