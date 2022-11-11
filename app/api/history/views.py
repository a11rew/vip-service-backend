from api.history.schemas import GetHistory
from api.history.services import HistoryService
from db.db import db_session
from db.models.history import History
from fastapi import APIRouter, Depends, Query
from sqlmodel.ext.asyncio.session import AsyncSession
import fastapi_users


current_user = fastapi_users.current_user()

router = APIRouter(
    dependencies= [Depends(current_user)]
)


@router.get("/user/history", response_model=list[GetHistory])
async def get_user_history(offset: int = 0, limit: int = Query(default=20, lte=20), session: AsyncSession = Depends(db_session)) -> list[History]:
    user_history = HistoryService(session=session)
    user = current_user
    return await user_history.get_user_history(user_id= user.id, limit=limit, offset=offset)


# @router.delete("/remove/all", response_model=GetHistory)
# async def remove_all_history(session: AsyncSession = Depends(db_session)):
#     user = current_user
#     all = HistoryService(session=session)
#     return await all.clear_all_history(user_id= user.id)


# @router.delete("/remove/{id}", response_model=GetHistory)
# async def remove_one_item(id: int, session: AsyncSession = Depends(db_session)):
#     user = current_user
#     item = HistoryService(session=session).clear_one_history(history_id =id,  user_id=user.id)
#     return await item
    

# To create the history, there's no need for an endpoint.
# The function can just be called from the services module directly.