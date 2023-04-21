from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, Message
from resources import messages as mes
from sqlalchemy.ext.asyncio import AsyncSession
from utils import config
from bot.keyboards.inline import start_kb, quest_1_kb, subscribe
from db import UsersRepository, SettingsRepository
from utils.analytics import log


router = Router()
bot = Bot(config.TELEGRAM_TOKEN, parse_mode="HTML")
dp = Dispatcher()


@router.callback_query_handler(lambda c: c.data == 'cancel')
async def send_manager(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):
    await state.clear()
    await q.message.delete()
    

@router.callback_query_handler(lambda c: c.data == 'yes_new')
async def send_manager(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):

    users_repo = UsersRepository(db_session)
    user = await users_repo.get(telegram_id=q.from_user.id)
    
    settings_repo = SettingsRepository(db_session)
    setting = await settings_repo.get(id=1)

    if True:
        user_channel_status = await bot.get_chat_member(chat_id=config.channel_id, user_id=q.from_user.id)

        if user_channel_status.status != 'left':
            user.is_subscribe = True
            await users_repo.update(user)
            await bot.send_message(
                q.from_user.id,
                text=mes.question_season_text,
                reply_markup=quest_1_kb())
            await q.message.delete()

        else:
            user.is_subscribe = False
            await users_repo.update(user)
            await bot.send_message(
                q.from_user.id,
                text='К сожалению, мы не обнаружили Вас в подписчиках канала https://t.me/+IN0lZonOmRk2ZTBi', reply_markup=subscribe())
    else:
        await bot.send_message(
            q.from_user.id,
            text=mes.question_season_text,
            reply_markup=quest_1_kb())
        await q.message.delete()
    await log(user_id=q.from_user.id,
              user_lang_code=q.from_user.language_code,
              action_name='create_new_report')


@router.callback_query_handler(lambda c: c.data == 'no_new')
async def send_manager(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):
    users_repo = UsersRepository(db_session)
    user = await users_repo.get(telegram_id=q.from_user.id)
    await bot.send_message(
        q.from_user.id,
        text=mes.start_text,
        reply_markup=start_kb(user))
    await q.message.delete()
