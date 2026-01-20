from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.models.user_model import UserCreate, UserResponse
from src.services.user_service import UserService
from src.db.database import get_db

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = await UserService.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    existing_email = await UserService.get_user_by_email(db, user.email)
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    new_user = await UserService.create_user(db, user)
    return new_user