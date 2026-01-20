from sqlmodel import create_engine, Session
from sqlalchemy.ext.asyncio import create_async_engine
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")

# For async operations with Neon PostgreSQL
async_engine = create_async_engine(DATABASE_URL)

# For sync operations if needed
sync_engine = create_engine(DATABASE_URL)

def get_session():
    with Session(sync_engine) as session:
        yield session