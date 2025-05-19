import pytest
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.engine import Engine
from typing import Generator

# Test database URL
TEST_DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/inure_bot_test"

# Create test engine
test_engine: Engine = create_engine(TEST_DATABASE_URL)

# Override the get_session dependency
@pytest.fixture
def db_session() -> Generator[Session, None, None]:
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
    from app.main import app
    from app.database import get_session

    def get_test_db() -> Generator[Session, None, None]:
        SQLModel.metadata.create_all(test_engine)
        with Session(test_engine) as session:
            yield session

    app.dependency_overrides[get_session] = get_test_db