import { useState } from 'react';
import { Task } from '@/src/services/taskService';

interface TaskItemProps {
  task: Task;
  onUpdate: (taskId: string, title: string, description?: string) => void;
  onDelete: (taskId: string) => void;
  onToggleComplete: (taskId: string, completed: boolean) => void;
}

const TaskItem = ({ task, onUpdate, onDelete, onToggleComplete }: TaskItemProps) => {
  const [isEditing, setIsEditing] = useState(false);
  const [title, setTitle] = useState(task.title);
  const [description, setDescription] = useState(task.description || '');

  const handleSave = () => {
    onUpdate(task.id, title, description);
    setIsEditing(false);
  };

  const handleCancel = () => {
    setTitle(task.title);
    setDescription(task.description || '');
    setIsEditing(false);
  };

  const handleToggleComplete = () => {
    onToggleComplete(task.id, !task.completed);
  };

  return (
    <li className="bg-white px-4 py-3 border border-gray-200 rounded-md shadow-sm">
      {isEditing ? (
        <div className="space-y-3">
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            placeholder="Task title"
          />
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            placeholder="Task description (optional)"
            rows={2}
          />
          <div className="flex space-x-2">
            <button
              onClick={handleSave}
              className="inline-flex items-center px-3 py-1 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-green-600 hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500"
            >
              Save
            </button>
            <button
              onClick={handleCancel}
              className="inline-flex items-center px-3 py-1 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Cancel
            </button>
          </div>
        </div>
      ) : (
        <div className="flex items-start">
          <div className="flex items-start h-5">
            <input
              id={`task-${task.id}`}
              type="checkbox"
              checked={task.completed}
              onChange={handleToggleComplete}
              className="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
            />
          </div>
          <div className="ml-3 min-w-0 flex-1">
            <label htmlFor={`task-${task.id}`} className="font-medium text-gray-900">
              <span className={task.completed ? 'line-through text-gray-500' : ''}>
                {task.title}
              </span>
            </label>
            {task.description && (
              <p className={`text-sm ${task.completed ? 'line-through text-gray-500' : 'text-gray-500'}`}>
                {task.description}
              </p>
            )}
            <p className="text-xs text-gray-400 mt-1">
              Created: {new Date(task.created_at).toLocaleDateString()}
              {task.updated_at !== task.created_at && ` | Updated: ${new Date(task.updated_at).toLocaleDateString()}`}
            </p>
          </div>
          <div className="flex space-x-2">
            <button
              onClick={() => setIsEditing(true)}
              className="inline-flex items-center p-1 border border-transparent text-sm font-medium rounded-md text-indigo-600 hover:text-indigo-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              Edit
            </button>
            <button
              onClick={() => onDelete(task.id)}
              className="inline-flex items-center p-1 border border-transparent text-sm font-medium rounded-md text-red-600 hover:text-red-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
            >
              Delete
            </button>
          </div>
        </div>
      )}
    </li>
  );
};

export default TaskItem;