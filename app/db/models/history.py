from typing import Optional
from sqlmodel import Field, Relationship, SQLModel
from .common import TimestampModel
from .user import User

class History(SQLModel, table= True):
    __tablename__ = "history"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    input: str
    result: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    user: Optional[User] = Relationship(back_populates="user")
    created_at: Optional[TimestampModel.created_at]
