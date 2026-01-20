import apiClient from '@/src/lib/apiClient';
import { storeToken, storeRefreshToken } from '@/src/lib/tokenStorage';

interface UserRegistrationData {
  email: string;
  name: string;
  password: string;
}

interface UserLoginData {
  email: string;
  password: string;
}

interface UserResponse {
  access_token: string;
  token_type: string;
  user_id: string;
}

interface UserSessionData {
  userId: string;
  email: string;
  name: string;
  accessToken: string;
  refreshToken?: string;
  expiresAt: string;
}

/**
 * Register a new user
 * @param userData User registration data
 * @returns Promise resolving to user session data
 */
export const registerUser = async (userData: UserRegistrationData): Promise<UserSessionData> => {
  try {
    const response = await apiClient.post<UserResponse>('/auth/register', userData);
    
    // Store the token in secure storage
    storeToken(response.data.access_token);
    // Note: In a real implementation, you might also receive a refresh token
    
    // Return user session data
    return {
      userId: response.data.user_id,
      email: userData.email,
      name: userData.name,
      accessToken: response.data.access_token,
      expiresAt: new Date(Date.now() + 30 * 60 * 1000).toISOString(), // 30 minutes from now
    };
  } catch (error: any) {
    console.error('Registration error:', error);
    throw error;
  }
};

/**
 * Login a user
 * @param loginData User login data
 * @returns Promise resolving to user session data
 */
export const loginUser = async (loginData: UserLoginData): Promise<UserSessionData> => {
  try {
    const response = await apiClient.post<UserResponse>('/auth/login', loginData);
    
    // Store the token in secure storage
    storeToken(response.data.access_token);
    // Note: In a real implementation, you might also receive a refresh token
    
    // Return user session data
    return {
      userId: response.data.user_id,
      email: loginData.email,
      name: '', // Name would typically come from the response
      accessToken: response.data.access_token,
      expiresAt: new Date(Date.now() + 30 * 60 * 1000).toISOString(), // 30 minutes from now
    };
  } catch (error: any) {
    console.error('Login error:', error);
    throw error;
  }
};

/**
 * Logout a user
 * @returns Promise resolving when logout is complete
 */
export const logoutUser = async (): Promise<void> => {
  try {
    // Call the logout endpoint
    await apiClient.post('/auth/logout');
  } catch (error: any) {
    console.error('Logout error:', error);
    // Even if the API call fails, we should clear the local token
  } finally {
    // Clear the token from storage regardless of API call success
    import('@/src/lib/tokenStorage').then(({ clearToken }) => clearToken());
  }
};

/**
 * Get current user profile
 * @returns Promise resolving to user profile data
 */
export const getCurrentUser = async (): Promise<any> => {
  try {
    // This would typically be an endpoint that returns user profile data
    // For now, we'll return a mock implementation
    const token = await import('@/src/lib/tokenStorage').then(mod => mod.getToken());
    if (!token) {
      throw new Error('No token available');
    }
    
    // In a real implementation, you would call an API endpoint to get user data
    // const response = await apiClient.get('/auth/profile');
    // return response.data;
    
    // Mock implementation returning basic user data
    return {
      userId: 'mock-user-id',
      email: 'mock@example.com',
      name: 'Mock User',
    };
  } catch (error: any) {
    console.error('Get user error:', error);
    throw error;
  }
};