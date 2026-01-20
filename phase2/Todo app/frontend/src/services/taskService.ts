import apiClient from '@/src/lib/apiClient';

// Define the Task interface based on the API contract
export interface Task {
  id: string;
  user_id: string;
  title: string;
  description?: string;
  completed: boolean;
  created_at: string; // ISO string format
  updated_at: string; // ISO string format
}

// Define interfaces for request bodies
interface CreateTaskRequest {
  title: string;
  description?: string;
  completed?: boolean;
}

interface UpdateTaskRequest {
  title?: string;
  description?: string;
  completed?: boolean;
}

/**
 * Fetch all tasks for a user
 * @param userId The ID of the user whose tasks to fetch
 * @param completed Optional filter for completion status
 * @returns Promise resolving to an array of tasks
 */
export const fetchUserTasks = async (userId: string, completed?: boolean): Promise<Task[]> => {
  try {
    const params: Record<string, any> = {};
    if (completed !== undefined) {
      params.completed = completed;
    }
    
    const response = await apiClient.get<Task[]>(`/api/${userId}/tasks`, { params });
    return response.data;
  } catch (error: any) {
    console.error('Error fetching user tasks:', error);
    throw error;
  }
};

/**
 * Create a new task for a user
 * @param userId The ID of the user creating the task
 * @param taskData The task data to create
 * @returns Promise resolving to the created task
 */
export const createTask = async (userId: string, taskData: CreateTaskRequest): Promise<Task> => {
  try {
    const response = await apiClient.post<Task>(`/api/${userId}/tasks`, taskData);
    return response.data;
  } catch (error: any) {
    console.error('Error creating task:', error);
    throw error;
  }
};

/**
 * Get a specific task by ID
 * @param userId The ID of the user who owns the task
 * @param taskId The ID of the task to retrieve
 * @returns Promise resolving to the task
 */
export const getTaskById = async (userId: string, taskId: string): Promise<Task> => {
  try {
    const response = await apiClient.get<Task>(`/api/${userId}/tasks/${taskId}`);
    return response.data;
  } catch (error: any) {
    console.error('Error fetching task:', error);
    throw error;
  }
};

/**
 * Update a task
 * @param userId The ID of the user who owns the task
 * @param taskId The ID of the task to update
 * @param taskData The updated task data
 * @returns Promise resolving to the updated task
 */
export const updateTask = async (userId: string, taskId: string, taskData: UpdateTaskRequest): Promise<Task> => {
  try {
    const response = await apiClient.put<Task>(`/api/${userId}/tasks/${taskId}`, taskData);
    return response.data;
  } catch (error: any) {
    console.error('Error updating task:', error);
    throw error;
  }
};

/**
 * Delete a task
 * @param userId The ID of the user who owns the task
 * @param taskId The ID of the task to delete
 * @returns Promise resolving when deletion is complete
 */
export const deleteTask = async (userId: string, taskId: string): Promise<void> => {
  try {
    await apiClient.delete(`/api/${userId}/tasks/${taskId}`);
  } catch (error: any) {
    console.error('Error deleting task:', error);
    throw error;
  }
};

/**
 * Toggle task completion status
 * @param userId The ID of the user who owns the task
 * @param taskId The ID of the task to update
 * @param completed The new completion status
 * @returns Promise resolving to the updated task
 */
export const toggleTaskCompletion = async (userId: string, taskId: string, completed: boolean): Promise<Task> => {
  try {
    const response = await apiClient.patch<Task>(`/api/${userId}/tasks/${taskId}/complete`, {
      completed
    });
    return response.data;
  } catch (error: any) {
    console.error('Error toggling task completion:', error);
    throw error;
  }
};