from typing import Optional, List
from sqlmodel import Field, Relationship, JSON, Column
from .common import TimestampModel, UUIDModel
from .user import User

class History(TimestampModel, UUIDModel, table= True):
    __tablename__ = "history"
    
    input: str
    result: List[str] = Field(sa_column=Column(JSON))
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    user: Optional[User] = Relationship(back_populates="user")

    class Config:
        arbitrary_types_allowed = True
        
    def __repr__(self):
        return f"<History (id: {self.id})>"

    
