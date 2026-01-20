import { Task } from '@/src/services/taskService';
import TaskItem from '@/src/components/TaskItem';

interface TaskListProps {
  tasks: Task[];
  onUpdateTask: (taskId: string, title: string, description?: string) => void;
  onDeleteTask: (taskId: string) => void;
  onToggleComplete: (taskId: string, completed: boolean) => void;
  loading?: boolean;
}

const TaskList = ({ tasks, onUpdateTask, onDeleteTask, onToggleComplete, loading }: TaskListProps) => {
  return (
    <div className="mt-6">
      <h2 className="text-lg font-medium text-gray-900 mb-4">Your Tasks</h2>
      {loading && (
        <div className="text-center py-4">
          <p>Processing tasks...</p>
        </div>
      )}
      <ul className="space-y-3">
        {tasks.map((task) => (
          <TaskItem
            key={task.id}
            task={task}
            onUpdate={onUpdateTask}
            onDelete={onDeleteTask}
            onToggleComplete={onToggleComplete}
          />
        ))}
      </ul>
    </div>
  );
};

export default TaskList;