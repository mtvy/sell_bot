import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.redis import RedisStorage

from bot_.middlewares import database_session_middleware
from db.utils import wait_for_mysql
from utils import config
from utils.redis import async_redis


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(config.TELEGRAM_TOKEN, parse_mode="HTML")
    dp = Dispatcher(storage=RedisStorage(async_redis))
    dp.update.middleware(database_session_middleware)
    dp.include_router("bot.views.start:router")
    dp.include_router("bot.views.other:router")
    dp.include_router("bot.views.add_data:router")
    dp.include_router("bot.views.question_1:router")
    dp.include_router("bot.views.question_2:router")
    dp.include_router("bot.views.question_3:router")
    dp.include_router("bot.views.question_4:router")
    dp.include_router("bot.views.question_5:router")
    dp.include_router("bot.views.question_6:router")
    dp.include_router("bot.views.question_7:router")
    dp.include_router("bot.views.report_excel:router")
    await dp.start_polling(bot)
    
