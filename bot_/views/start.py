from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.router import Router
from aiogram.types import Message
from bot_.keyboards.inline import start_kb, subscribe
from resources import messages as mes
from db import UsersRepository, SettingsRepository
from sqlalchemy.ext.asyncio import AsyncSession
from utils import config
from utils.analytics import log
from utils.services import users_decorator


router = Router()
bot = Bot(config.TELEGRAM_TOKEN, parse_mode="HTML")
dp = Dispatcher()


@router.message_handler(commands=["start"],state="*")
async def start(m: Message, state: FSMContext, db_session: AsyncSession):
    print(m.message_id)
    await state.clear()
    try:
        if m.from_user.username:
            username = m.from_user.username
        else:
            username = 'неизвестно'
    except:
        username = 'неизвестно'
    try:
        language = m.from_user.language_code
    except:
        language = 'неизвестно'

    users_repo = UsersRepository(db_session)
    user_ = await  users_repo.get(telegram_id=m.from_user.id)
    print(user_)
    if not  user_:
       await m.answer(
                text=mes.first_start)
    user = await users_repo.get_or_create(telegram_id=m.from_user.id,
                                          username=username,
                                          language=language)

    
    if config.dbs["subscribe"] =="1" or config.dbs["subscribe"] =="3":
        print(config.dbs["subscribe"])        
        user_channel_status = await bot.get_chat_member(chat_id=config.channel_id, user_id=m.from_user.id)

        if user_channel_status.status != 'left':
            user.is_subscribe = True
            await users_repo.update(user)
            await m.answer(
                text=mes.start_text,
                reply_markup=start_kb(user))
        else:
            user.is_subscribe = False
            await users_repo.update(user)
            await m.answer(
                text=mes.subscribe, reply_markup=subscribe())

        
    else:
        user.is_subscribe = False
        await users_repo.update(user)
        await m.answer(
                text=mes.start_text, reply_markup=start_kb(user))
        
    await log(user_id=m.from_user.id,
              user_lang_code=m.from_user.language_code,
              action_name='start')
