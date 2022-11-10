from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/")
async def search_vips(name: str, gender: str = None,
    occupation: str = None, age: int = None):

    params = {"name": name, "gender": gender,
    "occupation": occupation, "age": age }
    return params
