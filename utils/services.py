from db import UsersRepository
from resources import messages as mes
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.types import ReplyKeyboardRemove
from aiogram import Bot, Dispatcher
from utils import config
from resources import messages as mes
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from datetime import datetime
import pytz
from db import UsersRepository, SettingsRepository
from datetime import datetime


bot = Bot(config.TELEGRAM_TOKEN, parse_mode="HTML")


def subscribe() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Подписаться на канал', url='https://t.me/likhopoy')
    return builder.as_markup(resize_keyboard=True)


def get_season(number):
    """Определяем будущий сезон"""

    if number == 9 or number == 10 or number == 11:
        return mes.season_winter_btn
    elif number == 12 or number == 1 or number == 2:
        return mes.season_spring_btn
    elif number == 3 or number == 4 or number == 5:
        return mes.season_summer_btn
    elif number == 6 or number == 7 or number == 8:
        return mes.season_autumn_btn
    else:
        return number


def users_decorator(function_to_decorate):
    
    async def wrapper(m: Message, state: FSMContext, db_session: AsyncSession):
        
        settings_repo = SettingsRepository(db_session)
        setting = await settings_repo.get(id=1)

        if True:
            await function_to_decorate(m, state, db_session)
        else:
            users_repo = UsersRepository(db_session)
            user = await users_repo.get(telegram_id=m.from_user.id)
            
            try:
                user_channel_status = await bot.get_chat_member(chat_id=config.channel_id, user_id=m.from_user.id)

                if user_channel_status.status != 'left':
                    user.is_subscribe = True
                    await users_repo.update(user)
                    await function_to_decorate(m, state, db_session)

                else:
                    user.is_subscribe = False
                    await users_repo.update(user)
                    await m.answer(
                        text=mes.start_text, reply_markup=subscribe())
            except:
                await m.answer(
                    text="Обратитесь к адиминистратору", reply_markup=ReplyKeyboardRemove())
    return wrapper


def users_decorator_call(function_to_decorate):
    async def wrapper(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):
        
        settings_repo = SettingsRepository(db_session)
        setting = await settings_repo.get(id=1)
        
        if  True:
            await function_to_decorate(q, db_session, state)
        else:
            users_repo = UsersRepository(db_session)
            user = await users_repo.get(telegram_id=q.from_user.id)
            
            try:
                user_channel_status = await bot.get_chat_member(chat_id='-1001136057546', user_id=q.from_user.id)

                if user_channel_status.status != 'left':
                    user.is_subscribe = True
                    await users_repo.update(user)
                    await function_to_decorate(q, db_session, state)

                else:
                    user.is_subscribe = False
                    await users_repo.update(user)
                    await bot.send_message(
                        q.from_user.id,
                        text=mes.start_text, reply_markup=subscribe())
            except:
                await bot.send_message(
                    q.from_user.id,
                    text="Обратитесь к адиминистратору", reply_markup=ReplyKeyboardRemove())
    return wrapper



def is_time_to_send(time, max_delivery_gap):
    month, day = str(time[5:10]).split('-')
    hour, minute = str(time[11:16]).split(':')
    current_month, current_day, current_hour, current_minute = datetime.now(pytz.timezone(
        'Europe/Moscow')).strftime("%m-%d-%H-%M").split('-')
    if current_day == day and current_month == month and current_hour == hour:
        delivery_gap = int(minute) - int(current_minute)
        if delivery_gap <= 0 and delivery_gap > -max_delivery_gap:
            return True
    return False


async def push_message_all(message_to_send, session):

    users_repo = UsersRepository(session)
    users = await users_repo.get_many()

    for u in users:
        try:
            await bot.send_message(u.telegram_id, message_to_send)
        except:
            pass
