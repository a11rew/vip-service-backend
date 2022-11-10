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


