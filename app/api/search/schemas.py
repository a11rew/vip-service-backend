from pydantic import BaseModel
from typing import Optional


class SearchResponseSchema(BaseModel):
    is_vip: bool
    name: str
    gender: Optional[str] = None
    occupation: Optional[str] = None
    age: Optional[int] = None
