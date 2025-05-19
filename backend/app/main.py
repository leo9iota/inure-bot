from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
from typing import Dict, Any, AsyncGenerator, List, Annotated
from contextlib import asynccontextmanager

from app.database import create_db_and_tables, get_session
from app.models import User

# Type alias for dependency injection
SessionDep = Annotated[Session, Depends(dependency=get_session)]

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:
    # Startup code
    create_db_and_tables()
    yield
    # Shutdown code (if any)

app: FastAPI = FastAPI(
    title="Inure Bot API",
    description="Crypto Trading Bot",
    version="0.1.0",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Welcome to Inure Bot API"}


@app.get("/health")
async def health_check() -> Dict[str, str]:
    return {"status": "healthy"}


@app.get("/users")
async def get_users(session: SessionDep) -> List[Dict[str, Any]]:
    """Get all users from the database."""
    from sqlmodel import select
    users = session.exec(select(User)).all()
    return [{"id": user.id, "username": user.username, "email": user.email} for user in users]


