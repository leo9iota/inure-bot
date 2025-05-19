import sys
from collections.abc import Generator
from pathlib import Path

import pytest
from sqlalchemy.engine import Engine
from sqlmodel import SQLModel, create_engine, Session
from main import app
from app.database import get_session

# Add the parent directory to sys.path to allow importing from main and app
backend_dir = Path(__file__).parent.parent
sys.path.insert(0, str(backend_dir))

# Test database URL
TEST_DATABASE_URL: str = (
    "postgresql://postgres:postgres@localhost:5432/inure_bot_test"
)

# Create test engine
test_engine: Engine = create_engine(TEST_DATABASE_URL)


# Override the get_session dependency
@pytest.fixture(scope="function")
def db_session():
    """Provide a test database session."""
    SQLModel.metadata.create_all(test_engine)
    with Session(test_engine) as session:
        yield session
    SQLModel.metadata.drop_all(test_engine)


# Override the FastAPI dependency
@pytest.fixture(autouse=True)
def override_dependency() -> None:
    """Override the database session dependency for tests."""
    # This replaces the dependency in your FastAPI app
    def get_test_db() -> Generator[Session]:
        SQLModel.metadata.create_all(test_engine)
        with Session(test_engine) as session:
            yield session

    app.dependency_overrides[get_session] = get_test_db

