from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, add_pagination
from api.search.schemas import SearchResponseSchema


router = APIRouter()

# TODO : Add Page to Response Model Schema
@router.get("/", response_model=Page[SearchResponseSchema])
async def get_past_requests():
    res = []
    return paginate(res)


@router.get("/{id}", response_model=SearchResponseSchema)
async def get_one_past_request(id):
    res = {"id": id}
    return res
