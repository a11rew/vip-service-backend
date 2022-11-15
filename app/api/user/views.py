
from fastapi import APIRouter, Depends
from typing import Any, List 
from sqlalchemy import Session 
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.models import User
import fastapi_users

router = APIRouter()

current_user = fastapi_users.current_user()

@router.get("/my_details/")
def get_current_user(current_user: User = Depends(current_user)):
    return current_user


from uuid import UUID
from fastapi import APIRouter
from .schemas import APIKey, Signup, SignupResponse, Login, LoginResponse

router = APIRouter()


@router.post("/signup", response_model=SignupResponse)
async def create_user(signup: Signup):
    return signup


@router.post("/login", response_model=LoginResponse)
async def login(login: Login):
    return login


@router.get("/key")
async def get_user_api_key():
    # Check Database if User id exist
    # Depends on session user id

    # If user exist get user APIkey
    userAPIKey = APIKey(
        key="3fa85f64-5740-2262-b3fc-2c963f36afa1",
        user="3fa85f64-5740-2262-b3fc-2c963f36afa1",
    )

    # Send key string
    return userAPIKey

