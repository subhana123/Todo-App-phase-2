from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional
from sqlmodel import Session
from ..db.database import get_session
from ..models.user import User, UserCreate, UserRead
from ..services.user_service import UserService
from ..config.settings import settings
from ..utils.responses import create_success_response, create_error_response
from ..utils.errors import AuthException


router = APIRouter(prefix="/auth", tags=["authentication"])

# OAuth2 scheme for token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a JWT access token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    """Decode a JWT access token"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise AuthException(detail="Could not validate credentials")
        return user_id
    except JWTError:
        raise AuthException(detail="Could not validate credentials")


@router.post("/register", response_model=UserRead)
def register(user_create: UserCreate, db_session: Session = Depends(get_session)):
    """Register a new user"""
    try:
        user = UserService.create_user(user_create, db_session)
        return create_success_response(data=user, message="User registered successfully")
    except Exception as e:
        return create_error_response(error=str(e), message="Failed to register user")


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_session)):
    """Authenticate user and return access token"""
    user = UserService.authenticate_user(form_data.username, form_data.password, db_session)
    
    if not user:
        raise AuthException(detail="Incorrect email or password")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    
    return create_success_response(
        data={
            "access_token": access_token,
            "token_type": "bearer",
            "user": UserRead.from_orm(user) if hasattr(UserRead, 'from_orm') else UserRead(**user.dict())
        },
        message="Login successful"
    )


@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    """Logout user (invalidate token - in a real app, you'd add to blacklist)"""
    # In a real application, you would add the token to a blacklist
    # For this implementation, we'll just return a success message
    return create_success_response(message="Logged out successfully")


async def get_current_user(token: str = Depends(oauth2_scheme), db_session: Session = Depends(get_session)) -> User:
    """Get the current user based on the token"""
    user_id = decode_access_token(token)
    user = db_session.get(User, user_id)
    
    if user is None:
        raise AuthException(detail="User not found")
    
    return user