from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from search.schemas import SearchResponseSchema




class HistoryBase(BaseModel):
    input: str
    result: SearchResponseSchema | None = None
    
    class Config:
        orm_mode = True


class CreateHistory(HistoryBase):
    user_id: Optional[int]

class GetHistory(HistoryBase):
    id: int
    created_at: datetime