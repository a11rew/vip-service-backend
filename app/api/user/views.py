from uuid import UUID
from fastapi import APIRouter, Depends
from .schemas import APIKey, SearchResponseSchema

router = APIRouter()


@router.get("/{user_id}/key")
async def get_user_api_key(
    user_id: UUID):
    
    # Check Database if User id exist 
    
    # If user exist get user APIkey
    userAPIKey = APIKey(key='3fa85f64-5740-2262-b3fc-2c963f36afa1', user='3fa85f64-5740-2262-b3fc-2c963f36afa1')
    
    # Send key string
    return userAPIKey
