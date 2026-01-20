'use client';

import { useState, useEffect } from 'react';
import { useUserSession } from '@/src/contexts/UserSessionContext';
import ProtectedRoute from '@/src/components/ProtectedRoute';
import { fetchUserTasks, createTask, updateTask, deleteTask, toggleTaskCompletion } from '@/src/services/taskService';
import { Task } from '@/src/services/taskService';
import TaskList from '@/src/components/TaskList';
import TaskForm from '@/src/components/TaskForm';

const DashboardPage = () => {
  const { user } = useUserSession();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [operationLoading, setOperationLoading] = useState(false);

  // Fetch tasks when component mounts or user changes
  useEffect(() => {
    const loadTasks = async () => {
      if (!user) return;

      try {
        setLoading(true);
        setError(null);
        const userTasks = await fetchUserTasks(user.userId);
        setTasks(userTasks);
      } catch (err: any) {
        setError(err.message || 'Failed to load tasks');
      } finally {
        setLoading(false);
      }
    };

    loadTasks();
  }, [user]);

  const handleCreateTask = async (title: string, description?: string) => {
    if (!user) return;

    setOperationLoading(true);
    try {
      const newTask = await createTask(user.userId, { title, description });
      setTasks([...tasks, newTask]);
    } catch (err: any) {
      setError(err.message || 'Failed to create task');
    } finally {
      setOperationLoading(false);
    }
  };

  const handleUpdateTask = async (taskId: string, title: string, description?: string) => {
    if (!user) return;

    setOperationLoading(true);
    try {
      const updatedTask = await updateTask(user.userId, taskId, { title, description });
      setTasks(tasks.map(t => t.id === taskId ? updatedTask : t));
    } catch (err: any) {
      setError(err.message || 'Failed to update task');
    } finally {
      setOperationLoading(false);
    }
  };

  const handleDeleteTask = async (taskId: string) => {
    if (!user) return;

    setOperationLoading(true);
    try {
      await deleteTask(user.userId, taskId);
      setTasks(tasks.filter(t => t.id !== taskId));
    } catch (err: any) {
      setError(err.message || 'Failed to delete task');
    } finally {
      setOperationLoading(false);
    }
  };

  const handleToggleComplete = async (taskId: string, completed: boolean) => {
    if (!user) return;

    setOperationLoading(true);
    try {
      const updatedTask = await toggleTaskCompletion(user.userId, taskId, completed);
      setTasks(tasks.map(t => t.id === taskId ? updatedTask : t));
    } catch (err: any) {
      setError(err.message || 'Failed to update task completion');
    } finally {
      setOperationLoading(false);
    }
  };

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold text-gray-900">Welcome, {user.name || user.email}!</h1>
            <p className="mt-2 text-gray-600">Manage your tasks below</p>
          </div>

          <div className="bg-white shadow overflow-hidden sm:rounded-lg p-6">
            <TaskForm onCreateTask={handleCreateTask} />

            {loading ? (
              <div className="mt-8 text-center">
                <p>Loading tasks...</p>
              </div>
            ) : error ? (
              <div className="mt-8 rounded-md bg-red-50 p-4">
                <div className="flex">
                  <div className="ml-3">
                    <h3 className="text-sm font-medium text-red-800">{error}</h3>
                  </div>
                </div>
              </div>
            ) : tasks.length === 0 ? (
              <div className="mt-8 text-center">
                <p className="text-gray-500">No tasks yet. Add your first task above!</p>
              </div>
            ) : (
              <TaskList
                tasks={tasks}
                onUpdateTask={handleUpdateTask}
                onDeleteTask={handleDeleteTask}
                onToggleComplete={handleToggleComplete}
                loading={operationLoading}
              />
            )}

            {operationLoading && (
              <div className="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50">
                <div className="bg-white p-4 rounded-md shadow-lg">
                  <p>Processing your request...</p>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </ProtectedRoute>
  );
};

export default DashboardPage;