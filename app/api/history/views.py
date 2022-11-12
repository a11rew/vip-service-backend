from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate, add_pagination


router = APIRouter()

# TODO : Add Page to Response Model Schema
@router.get("/", response_model={})
async def historys():
    res = []
    return paginate(res)


@router.get("/{id}")
async def historys(id):
    res = {
        'id' : id
    }
    return res
