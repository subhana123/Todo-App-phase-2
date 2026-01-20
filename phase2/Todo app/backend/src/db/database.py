from sqlmodel import create_engine, Session
from sqlalchemy import event
from sqlalchemy.engine import Engine
import os
from typing import Generator
from .models import User, TodoItem  # Import all models here


# Use environment variable for database URL, with a default for development
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://user:password@localhost/todo_db"
)


# Create the engine
engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    """Create database tables"""
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Get database session"""
    with Session(engine) as session:
        yield session


# Enable foreign key constraints for SQLite (if used)
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if engine.url.drivername.startswith("sqlite"):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()