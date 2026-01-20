'use client';

import { useAuth } from '../context/AuthContext';
import TaskList from '../components/TaskList';

export default function Page() {
  const { user } = useAuth();

  if (!user) return <div>Please log in</div>;

  return (
    <div style={{ padding: '20px' }}>
      <h1>Welcome, {user.email}</h1>
      <TaskList />
    </div>
  );
}
