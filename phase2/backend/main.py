from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import your routers here
from src.api.todo_router import router as todo_router
from src.api.auth_router import router as auth_router
from src.api.user_router import router as user_router

app = FastAPI(
    title="Todo API",
    description="A simple todo application API",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://todo-app-phase-2-ao63.vercel.app",  # Your Vercel frontend URL
        "http://localhost:3000",  # Local development
        "http://localhost:3001",  # Alternative local dev port
        "http://127.0.0.1:3000", # Alternative local dev URL
        "http://127.0.0.1:3001"  # Alternative local dev URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user_router, prefix="/api/v1", tags=["users"])
app.include_router(auth_router, prefix="/api/v1", tags=["auth"])
app.include_router(todo_router, prefix="/api/v1", tags=["todos"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}