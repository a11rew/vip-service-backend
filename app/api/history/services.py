from api.history.schemas import CreateHistory, GetHistory
from db.db import db_session
from db.models.history import History
from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class HistoryService:

    def __init__(self, session: AsyncSession = Depends(db_session)):
        self.session = session

    async def create_history(self, history: CreateHistory, user_id: int) -> History:
        new_history = History(**history.dict(), user_id=user_id)
        self.session.add(new_history)
        await self.session.commit()
        await self.session.refresh(new_history)

        return new_history

    async def get_user_history(self, user_id: int, offset: int, limit: int):
        user_history = await self.session.execute(select(History).where(user_id == user_id).offset(offset).limit(limit))
        if user_history:
            return user_history.scalars().fetchall()

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User has no history"
        )


    # async def clear_one_history(self, history_id: int, user_id: int):

    #     statement = select(History).where(id=history_id, user_id=user_id)
    #     result = self.session.execute(statement)

    #     self.session.delete(result.one())
    #     self.session.commit()

    #     return None

    # async def clear_all_history(self, user_id: int):

    #     statement = select(History).where(user_id=user_id)
    #     user_history = self.session.execute(statement)

    #     self.session.delete(user_history)

    #     self.session.commit()

    #     return None