from fastapi import Request, HTTPException, status
from typing import Awaitable, Callable
from starlette.responses import Response
from .jwt_handler import verify_token


async def jwt_middleware(request: Request, call_next: Callable[[Request], Awaitable[Response]]):
    # Skip authentication for auth endpoints
    if request.url.path.startswith("/auth"):
        response = await call_next(request)
        return response

    # Check for JWT token in Authorization header for API endpoints
    if request.url.path.startswith("/api"):
        authorization = request.headers.get("Authorization")
        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )

        token = authorization.split(" ")[1]
        payload = verify_token(token)

        # Add user info to request state for use in endpoints
        request.state.user_id = payload.get("sub")
        request.state.user_email = payload.get("email")

    response = await call_next(request)
    return response