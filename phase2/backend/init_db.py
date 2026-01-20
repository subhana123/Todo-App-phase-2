"""
Database initialization script
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.database import Base, settings
from src.db.todo_db_model import Todo

def init_db():
    # Create database tables
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db()