# Data Model: Next.js Frontend with Better Auth Integration

## UserSession Entity

### Properties
- **userId** (string)
  - Type: String
  - Constraints: Required, Unique
  - Description: Unique identifier for the authenticated user from the auth system

- **email** (string)
  - Type: String (Email format)
  - Constraints: Required, Valid email format
  - Description: User's email address used for login and identification

- **name** (string)
  - Type: String
  - Constraints: Required
  - Description: User's display name

- **accessToken** (string)
  - Type: String (JWT format)
  - Constraints: Required when authenticated
  - Description: JWT token for API authentication

- **refreshToken** (string)
  - Type: String (JWT format)
  - Constraints: Optional, depends on auth strategy
  - Description: Token for refreshing the access token

- **expiresAt** (Date)
  - Type: Date/Unix timestamp
  - Constraints: Required when authenticated
  - Description: Timestamp when the access token expires

### Validation Rules
- Email must be in valid format
- userId must be present when authenticated
- accessToken must be present when authenticated
- expiresAt must be in the future when authenticated

## TaskItem Entity

### Properties
- **id** (string)
  - Type: String (UUID format)
  - Constraints: Required, Unique
  - Description: Unique identifier for the task from the backend

- **userId** (string)
  - Type: String
  - Constraints: Required, References UserSession.userId
  - Description: Links the task to the user who owns it

- **title** (string)
  - Type: String
  - Constraints: Required, Min length 1, Max length 255
  - Description: Brief title or summary of the task

- **description** (string)
  - Type: String
  - Constraints: Optional, Max length 1000
  - Description: Detailed description of the task

- **completed** (boolean)
  - Type: Boolean
  - Constraints: Required, Default: false
  - Description: Indicates whether the task is completed or pending

- **createdAt** (Date)
  - Type: Date/Unix timestamp
  - Constraints: Required
  - Description: Timestamp when the task was created

- **updatedAt** (Date)
  - Type: Date/Unix timestamp
  - Constraints: Required
  - Description: Timestamp when the task was last updated

### Validation Rules
- Title must not be empty
- userId must reference an existing user
- completed field must be boolean
- createdAt and updatedAt must be valid timestamps

### State Transitions
- **Pending → Completed**: When task is marked as complete via UI toggle
- **Completed → Pending**: When task is marked as incomplete via UI toggle

## APIClient Entity

### Properties
- **baseURL** (string)
  - Type: String (URL format)
  - Constraints: Required
  - Description: Base URL for the backend API

- **defaultHeaders** (object)
  - Type: Object with key-value pairs
  - Constraints: Optional
  - Description: Headers to include with all requests (e.g., Content-Type)

- **interceptors** (array)
  - Type: Array of interceptor functions
  - Constraints: Optional
  - Description: Functions to process requests/responses (e.g., attach JWT, handle errors)

### Methods
- **request(config)**: Makes an HTTP request with the provided configuration
- **get(url, config)**: Makes a GET request to the specified URL
- **post(url, data, config)**: Makes a POST request to the specified URL with data
- **put(url, data, config)**: Makes a PUT request to the specified URL with data
- **delete(url, config)**: Makes a DELETE request to the specified URL
- **patch(url, data, config)**: Makes a PATCH request to the specified URL with data

### Validation Rules
- baseURL must be a valid URL
- defaultHeaders must be a valid object
- interceptors must be an array of valid functions