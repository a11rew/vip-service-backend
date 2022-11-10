from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: Optional[UUID] = None
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True