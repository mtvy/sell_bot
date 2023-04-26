from typing import Callable, Dict, Any, Awaitable

from aiogram.types import Update

from db.core import DBSession
from db import UsersRepository
import datetime

async def database_session_middleware(
    handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
    event: Update,
    data: Dict[str, Any]
) -> Any:
    async with DBSession() as db_session:
        
        data["db_session"] = db_session
        
        try:
            if event.message:
                chat_id=event.message.from_user.id
            else:
                chat_id=event.callback_query.from_user.id
            user_repo = UsersRepository(db_session)
            user = await user_repo.get(telegram_id=chat_id)
            if user:
                user.last_active=datetime.datetime.now()
                await user_repo.update(user)
        except Exception  as e:
            print(e)
        
       
        return await handler(event, data)
