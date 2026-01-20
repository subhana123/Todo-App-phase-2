import { z } from 'zod';

// Define Zod schema for login form validation
export const loginSchema = z.object({
  email: z.string().email({ message: 'Invalid email address' }),
  password: z.string().min(1, { message: 'Password is required' }),
});

// Export the type for use in components
export type LoginFormData = z.infer<typeof loginSchema>;