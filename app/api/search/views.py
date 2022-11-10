from fastapi import APIRouter, Depends
from .schemas import SearchResponseSchema

router = APIRouter()


@router.get("/", response_model=SearchResponseSchema)
async def search_vips(
    name: str, gender: str = None, occupation: str = None, age: int = None
):
    resp = {
        "is_vip": True,
        "name": name,
        "gender": gender,
        "occupation": occupation,
        "age": age,
    }

    return resp
