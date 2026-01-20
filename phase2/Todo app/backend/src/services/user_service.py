from sqlmodel import Session, select
from typing import Optional
from ..models.user import User, UserBase
from passlib.context import CryptContext
import uuid


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, user_data: UserBase) -> User:
        # Hash the password
        hashed_password = pwd_context.hash(user_data.password)

        db_user = User(
            email=user_data.email,
            name=user_data.name,
            hashed_password=hashed_password
        )
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def get_user_by_email(self, email: str) -> Optional[User]:
        statement = select(User).where(User.email == email)
        user = self.session.exec(statement).first()
        return user

    def get_user_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        statement = select(User).where(User.id == user_id)
        user = self.session.exec(statement).first()
        return user

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email(email)
        if not user:
            return None
        if not self.verify_password(password, user.hashed_password):
            return None
        return user