import { z } from 'zod';

// Define Zod schema for task form validation
export const taskSchema = z.object({
  title: z.string().min(1, { message: 'Title is required' }).max(255, { message: 'Title must be at most 255 characters' }),
  description: z.string().max(1000, { message: 'Description must be at most 1000 characters' }).optional(),
  completed: z.boolean().optional(),
});

// Export the type for use in components
export type TaskFormData = z.infer<typeof taskSchema>;