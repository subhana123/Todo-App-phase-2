import { useState } from 'react';
import { 
  createTask as createTaskApi, 
  updateTask as updateTaskApi, 
  deleteTask as deleteTaskApi, 
  toggleTaskCompletion as toggleTaskCompletionApi,
  Task 
} from '@/src/services/taskService';

// Custom hook for task operations
export const useTaskOperations = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const createTask = async (userId: string, title: string, description?: string) => {
    setLoading(true);
    setError(null);
    try {
      const newTask = await createTaskApi(userId, { title, description });
      return newTask;
    } catch (err: any) {
      setError(err.message || 'Failed to create task');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const updateTask = async (userId: string, taskId: string, title: string, description?: string) => {
    setLoading(true);
    setError(null);
    try {
      const updatedTask = await updateTaskApi(userId, taskId, { title, description });
      return updatedTask;
    } catch (err: any) {
      setError(err.message || 'Failed to update task');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const deleteTask = async (userId: string, taskId: string) => {
    setLoading(true);
    setError(null);
    try {
      await deleteTaskApi(userId, taskId);
    } catch (err: any) {
      setError(err.message || 'Failed to delete task');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const toggleTaskCompletion = async (userId: string, taskId: string, completed: boolean) => {
    setLoading(true);
    setError(null);
    try {
      const updatedTask = await toggleTaskCompletionApi(userId, taskId, completed);
      return updatedTask;
    } catch (err: any) {
      setError(err.message || 'Failed to toggle task completion');
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return {
    createTask,
    updateTask,
    deleteTask,
    toggleTaskCompletion,
    loading,
    error,
  };
};