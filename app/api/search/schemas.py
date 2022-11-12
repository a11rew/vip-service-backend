from pydantic import BaseModel
from typing import Optional


class SearchResponseSchema(BaseModel):
    name: str
    gender: Optional[str] = None
    occupation: Optional[str] = None
    age: Optional[int] = None
    is_vip: Optional[bool] = None
    vip_score: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
