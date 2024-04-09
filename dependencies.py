from typing import Annotated
from fastapi import Header
from sqlmodel import Session, create_engine, SQLModel # type: ignore

# Create the database engine
engine = create_engine("sqlite:///database.db")

# Create the table
SQLModel.metadata.create_all(engine)

# Dependency to get database session
def get_session() -> Session:
    with Session(engine) as session:
        yield session

# Dependency to extract User-Agent header
def get_user_agent(user_agent: Annotated[str | None, Header()] = None):
    return user_agent
