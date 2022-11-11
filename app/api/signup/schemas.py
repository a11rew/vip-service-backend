from pydantic import BaseModel


class Signup(BaseModel):
    first_name: str
    last_name: int
    email: str
    password: str