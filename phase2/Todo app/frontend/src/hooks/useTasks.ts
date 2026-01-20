import { useState, useEffect } from 'react';
import { fetchUserTasks, Task } from '@/src/services/taskService';

// Custom hook for fetching tasks
export const useTasks = (userId: string, completed?: boolean) => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Fetch tasks when userId or completed filter changes
  useEffect(() => {
    const loadTasks = async () => {
      if (!userId) return;
      
      setLoading(true);
      setError(null);
      
      try {
        const userTasks = await fetchUserTasks(userId, completed);
        setTasks(userTasks);
      } catch (err: any) {
        setError(err.message || 'Failed to load tasks');
      } finally {
        setLoading(false);
      }
    };

    loadTasks();
  }, [userId, completed]);

  return {
    tasks,
    loading,
    error,
    refetch: () => {
      // This will trigger the effect again to reload tasks
      const currentCompleted = completed;
      setTasks([]);
      setError(null);
      // Temporarily set completed to opposite and back to trigger reload
      setLoading(true);
      setTimeout(() => {
        // This is a simplified refetch - in a real app you might want to call the API directly
        setTasks([]);
        setLoading(true);
        setTimeout(() => {
          // Actually refetch with original filter
          const loadTasks = async () => {
            try {
              const userTasks = await fetchUserTasks(userId, currentCompleted);
              setTasks(userTasks);
            } catch (err: any) {
              setError(err.message || 'Failed to load tasks');
            } finally {
              setLoading(false);
            }
          };
          loadTasks();
        }, 0);
      }, 0);
    }
  };
};