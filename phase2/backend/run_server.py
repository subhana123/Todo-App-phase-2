import uvicorn
import asyncio
from src.config.settings import settings


def run_dev_server():
    """Run the development server"""
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )


if __name__ == "__main__":
    run_dev_server()