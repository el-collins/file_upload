from typing import Annotated
from sqlmodel import SQLModel, Field # type: ignore

# Define the SQLModel for the UserProfile table
class UserProfile(SQLModel, table=True):
    id: Annotated[int, Field(default=None, primary_key=True)]
    # id: int = Field(default=None, primary_key=True)
    username: str
    phone_number: str
    email: str
    profile_picture: str  # This will store the path to the profile picture