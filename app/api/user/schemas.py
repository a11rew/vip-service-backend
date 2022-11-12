from uuid import UUID
from pydantic import BaseModel


class APIKey(BaseModel):
    key: UUID
    user: UUID
