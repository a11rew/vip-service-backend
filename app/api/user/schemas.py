from uuid import UUID
from pydantic import BaseModel


class APIKey(BaseModel):
    key: UUID
    user: UUID


class Signup(BaseModel):
    first_name: str
    last_name: int
    email: str
    password: str


class SignupResponse(Signup):
    id: UUID


class Login(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    id: UUID
    first_name: str
    last_name: int
    email: str
