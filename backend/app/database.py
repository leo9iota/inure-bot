import os
from typing import Generator
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.engine import Engine

# Database configuration
DB_USER: str = os.getenv(key="DB_USER", default="postgres")
DB_PASSWORD: str = os.getenv(key="DB_PASSWORD", default="postgres")
DB_HOST: str = os.getenv(key="DB_HOST", default="localhost")
DB_PORT: str = os.getenv(key="DB_PORT", default="5432")
DB_NAME: str = os.getenv(key="DB_NAME", default="inure_bot")

DATABASE_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create engine
engine: Engine = create_engine(url=DATABASE_URL, echo=True)

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(bind=engine)

def get_session() -> Generator[Session, None, None]:
    with Session(bind=engine) as session:
        yield session

