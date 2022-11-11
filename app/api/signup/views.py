from fastapi import APIRouter
from .schemas import Signup


router = APIRouter()


@router.post("/", response_model= Signup)
async def create_signup(signup: Signup):
    return signup