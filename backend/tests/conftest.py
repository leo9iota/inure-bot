import pytest
from sqlmodel import SQLModel, create_engine, Session

# Test database URL
TEST_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/inure_bot_test"

# Create test engine
test_engine = create_engine(TEST_DATABASE_URL)

# Override the get_session dependency
@pytest.fixture
def db_session():
    SQLModel.metadata.create_all(test_engine)
    with Session(test_engine) as session:
        yield session
    SQLModel.metadata.drop_all(test_engine)

# Override the FastAPI dependency
@pytest.fixture(autouse=True)
def override_dependency():
    # This replaces the dependency in your FastAPI app
    from app.main import app
    from app.database import get_session
    
    def get_test_db():
        SQLModel.metadata.create_all(test_engine)
        with Session(test_engine) as session:
            yield session
    
    app.dependency_overrides[get_session] = get_test_db