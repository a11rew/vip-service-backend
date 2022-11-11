from uuid import UUID
from pydantic import BaseModel
from typing import Optional


class APIKey(BaseModel):
    key: UUID
    user: UUID
