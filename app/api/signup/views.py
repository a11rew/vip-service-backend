from fastapi import APIRouter
from .schemas import Signup

router = APIRouter()

@router.get("/", response_model= Signup)
async def signup_user(first_name: str,last_name: int, email: str, password: str):
                    show = {
                        "first_name": first_name,
                        "last_name": last_name,
                        "email": email,
                        "password": password
                    }
                    return show