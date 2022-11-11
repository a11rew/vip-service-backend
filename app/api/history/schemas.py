from pydantic import BaseModel
from typing import Optional
from datetime import datetime





class HistoryBase(BaseModel):
    input: str
    result: str
    
    class Config:
        orm_mode = True


class CreateHistory(HistoryBase):
    user_id: Optional[int]

class GetHistory(HistoryBase):
    id: int
    created_at: datetime