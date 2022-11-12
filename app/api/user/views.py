from uuid import UUID
from fastapi import APIRouter, Depends
from .schemas import APIKey

router = APIRouter()


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
