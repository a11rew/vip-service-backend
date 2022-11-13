from sqlmodel import Field, JSON, Column
from .common import TimestampModel, UUIDModel


class History(TimestampModel, UUIDModel, table=True):
    __tablename__ = "history"

    input: str = Field(sa_column=Column(JSON))
    result_id: int = Field(foreign_key="people.id")
    user_id: int = Field(foreign_key="user.id")

    class Config:
        arbitrary_types_allowed = True

    def __repr__(self):
        return f"<History (id: {self.id})>"
