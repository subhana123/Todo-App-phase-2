# Data Model: Multi-User Web Todo Application

## Overview
This document defines the data models for the multi-user todo application, including entities, their attributes, relationships, and validation rules.

## Entities

### User
Represents a registered user of the system with unique identifier, authentication credentials (hashed), profile information, and associated todo items.

**Fields:**
- `id` (UUID/Integer): Unique identifier for the user (Primary Key)
- `email` (String): User's email address (Unique, Required, Validated)
- `username` (String): User's chosen username (Unique, Required, 3-30 characters)
- `hashed_password` (String): Securely hashed password (Required, Stored securely)
- `first_name` (String, Optional): User's first name (Max 50 characters)
- `last_name` (String, Optional): User's last name (Max 50 characters)
- `created_at` (DateTime): Timestamp when user account was created
- `updated_at` (DateTime): Timestamp when user account was last updated
- `is_active` (Boolean): Whether the account is active (Default: True)

**Validation Rules:**
- Email must be a valid email format
- Username must be 3-30 alphanumeric characters plus underscores/hyphens
- Password must meet minimum strength requirements (handled by auth system)
- Email and username must be unique across all users

**Relationships:**
- One-to-Many: A user has many TodoItems

### TodoItem
Represents a single todo task with properties including title, description, completion status, creation timestamp, update timestamp, and association to a specific user.

**Fields:**
- `id` (UUID/Integer): Unique identifier for the todo item (Primary Key)
- `title` (String): Title of the todo item (Required, Max 200 characters)
- `description` (Text, Optional): Detailed description of the todo item (Max 1000 characters)
- `is_completed` (Boolean): Whether the todo item is completed (Default: False)
- `due_date` (DateTime, Optional): When the todo item is due
- `priority` (Enum): Priority level (Low, Medium, High) (Default: Medium)
- `created_at` (DateTime): Timestamp when todo item was created
- `updated_at` (DateTime): Timestamp when todo item was last updated
- `user_id` (UUID/Integer): Foreign key linking to the owning user (Required)

**Validation Rules:**
- Title must be 1-200 characters
- Description, if provided, must be 1-1000 characters
- Due date, if provided, must be a future date
- Priority must be one of the allowed values
- User_id must reference an existing user

**Relationships:**
- Many-to-One: A todo item belongs to one User

### AuthToken (Conceptual - handled by Better Auth)
Represents a JWT authentication token containing user identity information and validity period for maintaining user sessions.

**Fields:**
- `token` (String): The JWT token string (Stored in httpOnly cookie)
- `user_id` (UUID/Integer): Reference to the user the token belongs to
- `expires_at` (DateTime): When the token expires
- `created_at` (DateTime): When the token was issued
- `type` (String): Token type (access/refresh)

**Validation Rules:**
- Token must be a valid JWT format
- Expires_at must be in the future
- User_id must reference an existing user

## State Transitions

### TodoItem State Transitions
- `Pending` → `Completed`: When user marks item as complete
- `Completed` → `Pending`: When user unmarks item as complete

### User Account States
- `Inactive` → `Active`: After email verification (if implemented)
- `Active` → `Suspended`: If account violates terms (future feature)
- `Suspended` → `Active`: If suspension is lifted (future feature)

## Indexes

### Performance Indexes
- User.email: For fast login lookups
- User.username: For fast username lookups
- TodoItem.user_id: For fast user todo retrieval
- TodoItem.is_completed: For filtering completed items
- TodoItem.created_at: For chronological sorting
- TodoItem.due_date: For due date filtering (if not null)

## Constraints

### Referential Integrity
- TodoItem.user_id must reference an existing User.id
- Prevent orphaned todo items

### Data Consistency
- Prevent duplicate emails
- Prevent duplicate usernames
- Ensure all timestamps are in UTC

## Future Extensions
- Categories/Tags for TodoItems
- Recurring todo items
- Sharing/todo collaboration
- Attachments to todo items