import { z } from 'zod';

// Define Zod schema for signup form validation
export const signupSchema = z.object({
  email: z.string().email({ message: 'Invalid email address' }),
  name: z.string().min(2, { message: 'Name must be at least 2 characters' }).max(50, { message: 'Name must be at most 50 characters' }),
  password: z.string().min(8, { message: 'Password must be at least 8 characters' })
    .regex(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/, { message: 'Password must contain at least one uppercase letter, one lowercase letter, and one number' }),
});

// Export the type for use in components
export type SignupFormData = z.infer<typeof signupSchema>;