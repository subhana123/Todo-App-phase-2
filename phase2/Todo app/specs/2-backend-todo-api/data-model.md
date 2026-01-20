# Data Model: Backend Todo API

## User Entity

### Fields
- **id** (UUID, Primary Key)
  - Type: UUID (Universally Unique Identifier)
  - Constraints: Required, Unique, Auto-generated
  - Description: Unique identifier for each user

- **email** (String)
  - Type: String (Email format)
  - Constraints: Required, Unique, Indexed, Valid email format
  - Description: User's email address used for login and identification

- **name** (String)
  - Type: String
  - Constraints: Required
  - Description: User's display name

- **created_at** (DateTime)
  - Type: DateTime (ISO 8601 format)
  - Constraints: Required, Auto-generated
  - Description: Timestamp when the user account was created

### Relationships
- **Tasks**: One-to-Many relationship with Task entity (one user can have many tasks)

### Validation Rules
- Email must be in valid format
- Email must be unique across all users
- Name must not be empty

## Task Entity

### Fields
- **id** (UUID, Primary Key)
  - Type: UUID (Universally Unique Identifier)
  - Constraints: Required, Unique, Auto-generated
  - Description: Unique identifier for each task

- **user_id** (UUID, Foreign Key)
  - Type: UUID
  - Constraints: Required, Indexed, References User.id
  - Description: Links the task to the user who owns it

- **title** (String)
  - Type: String
  - Constraints: Required
  - Description: Brief title or summary of the task

- **description** (String)
  - Type: String
  - Constraints: Optional
  - Description: Detailed description of the task

- **completed** (Boolean)
  - Type: Boolean
  - Constraints: Required, Default: False
  - Description: Indicates whether the task is completed or pending

- **created_at** (DateTime)
  - Type: DateTime (ISO 8601 format)
  - Constraints: Required, Auto-generated
  - Description: Timestamp when the task was created

- **updated_at** (DateTime)
  - Type: DateTime (ISO 8601 format)
  - Constraints: Required, Auto-generated, Updates on modification
  - Description: Timestamp when the task was last updated

### Relationships
- **User**: Many-to-One relationship with User entity (many tasks belong to one user)

### Validation Rules
- Title must not be empty
- user_id must reference an existing user
- completed field must be boolean

### Indexes
- Index on user_id for efficient querying of tasks by user
- Index on completed for filtering completed/pending tasks

## State Transitions

### Task Entity
- **Pending → Completed**: When task is marked as complete via PATCH /api/{user_id}/tasks/{id}/complete
- **Completed → Pending**: When task is marked as incomplete via PATCH /api/{user_id}/tasks/{id}/complete

## Constraints

### Referential Integrity
- Task.user_id must reference an existing User.id
- Deleting a user should cascade delete their tasks (to be configured in the database)

### Data Isolation
- Users can only access tasks where user_id matches their authenticated user ID
- API endpoints must validate that the authenticated user owns the requested task