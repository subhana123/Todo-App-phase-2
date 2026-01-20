from fastapi import Request, HTTPException, status
from ..api.auth import decode_access_token
from ..models.user import User
from sqlmodel import Session
from ..db.database import get_session


async def verify_user_owns_resource(request: Request, call_next):
    """
    Middleware to verify that a user owns the resource they're trying to access.
    This is a simplified version - in practice, you'd implement this more granularly
    depending on the specific endpoint and resource being accessed.
    """
    # Get the path and method
    path = request.url.path
    method = request.method
    
    # For certain paths that require ownership verification
    if path.startswith("/api/v1/todos") and path != "/api/v1/todos" and method in ["GET", "PUT", "DELETE", "PATCH"]:
        # Extract the token from headers
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated"
            )
        
        token = auth_header.split(" ")[1]
        try:
            current_user_id = decode_access_token(token)
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
        
        # Extract the todo_id from the path
        # This assumes the path is in the format /api/v1/todos/{id}
        path_parts = path.strip('/').split('/')
        if len(path_parts) >= 3 and path_parts[-2] == 'todos':
            try:
                todo_id = int(path_parts[-1])
                
                # Verify the user owns this todo item
                # We need to create a database session to check ownership
                for db_session in get_session():
                    # Import here to avoid circular imports
                    from ..models.todo_item import TodoItem
                    
                    # Query the database to check if the todo item belongs to the user
                    todo_item = db_session.get(TodoItem, todo_id)
                    
                    if not todo_item:
                        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail="Todo item not found"
                        )
                    
                    if todo_item.user_id != current_user_id:
                        raise HTTPException(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail="Access denied: You can only access your own todo items"
                        )
                    break  # Exit the generator loop after using the session
        
    # Continue with the request
    response = await call_next(request)
    return response