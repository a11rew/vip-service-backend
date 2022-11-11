# from datetime import datetime
# from typing import Optional
# from uuid import UUID

from pydantic import BaseModel


class Signup(BaseModel):
    # id: Optional[UUID] = None
    first_name: str
    last_name: int
    email: str
    password: str
    
    # class Config:
    #     orm_mode = True


# class ExampleSchema(ExampleCreateSchema):
#     created_at: Optional[datetime]
#     updated_at: Optional[datetime]
