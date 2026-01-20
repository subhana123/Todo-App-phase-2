from contextlib import asynccontextmanager
from sqlmodel import Session, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from typing import AsyncGenerator
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


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(async_engine) as session:
        yield session


def get_sync_session():
    with Session(sync_engine) as session:
        yield session