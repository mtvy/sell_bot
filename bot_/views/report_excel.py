import os
import xlsxwriter

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, Message, FSInputFile
from resources import messages as mes
from sqlalchemy.ext.asyncio import AsyncSession
from utils import config
from bot_.keyboards.inline import new_kb, subscribe
from bot_.fsm_states_groups import FilterCreateForm
from utils.callback_data import CallbackData
from db import UsersRepository, SettingsRepository
from utils.analytics import log
from utils.excel_report import excel_report


router = Router()
bot = Bot(config.TELEGRAM_TOKEN, parse_mode="HTML")
dp = Dispatcher()

QUESTIONS_QUESTION__CD = CallbackData("questions_question", "action", "question")


@router.callback_query(QUESTIONS_QUESTION__CD.filter(action="8"))
async def job_delivery_method(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):
    await bot.answer_callback_query(q.id)
    callback_data = QUESTIONS_QUESTION__CD.parse(q.data)
    await state.update_data(action=callback_data["action"],
                            proc_turnover=str(callback_data["question"]))
    dt = await state.get_data()
    list_item = []
    list_item.append(dt["avr_check"])
    list_item.append(dt["max_check"])
    list_item.append(dt["max_count"])
    list_item.append(dt["min_redemption"])
    list_item.append(dt["proc_sale"])
    list_item.append(dt["proc_missrvenue"])
    list_item.append(dt["proc_turnover"])
    a = []
    for l in list_item:
        if l == 'False':
            a.append(l)
    if len(a) >= 3:
        await bot.send_message(
                q.from_user.id,
                text=mes.question_skip
            )
        return

    await bot.send_message(
            q.from_user.id,
            text=mes.report_wait
        )


    season = dt["season"]
    avr_check = dt["avr_check"]
    max_check = dt["max_check"]
    max_count = dt["max_count"]
    min_redemption = dt["min_redemption"]
    proc_sale = dt["proc_sale"]
    proc_missrvenue = dt["proc_missrvenue"]
    proc_turnover = dt["proc_turnover"]
    
    await excel_report(season,
                       avr_check,
                       max_check,
                       max_count,
                       min_redemption,
                       proc_sale,
                       proc_missrvenue,
                       proc_turnover,
                       q,
                       db_session,
                       state,
                       )
    await state.clear()
    #await q.message.delete()

    await bot.send_message(
        q.from_user.id,
        text=mes.report_text)

    users_repo = UsersRepository(db_session)
    user = await users_repo.get(telegram_id=q.from_user.id)
    
    settings_repo = SettingsRepository(db_session)
    setting = await settings_repo.get(id=1)

    if config.dbs["subscribe"] == "2" or config.dbs["subscribe"] == "3":
        user_channel_status = await bot.get_chat_member(chat_id=config.channel_id,user_id=q.from_user.id)

        if user_channel_status.status != 'left':
            user.is_subscribe = True
            await users_repo.update(user)
            await bot.send_message(
                q.from_user.id,
                text="Сделать подбор ещё раз?",
                reply_markup=new_kb(user))

        else:
            user.is_subscribe = False
            await users_repo.update(user)
            await bot.send_message(
                q.from_user.id,
                text=mes.subscribe, reply_markup=subscribe())
    else:
        await bot.send_message(
            q.from_user.id,
            text="Сделать подбор ещё раз?",
            reply_markup=new_kb(user)
        )
    await log(user_id=q.from_user.id,
              user_lang_code=q.from_user.language_code,
              action_name='create_report')

@router.message_handler(state = FilterCreateForm.proc_turnover)
async def job_delivery_method(message: CallbackQuery, db_session: AsyncSession, state: FSMContext):
    await state.update_data(proc_turnover=message.text)
    dt = await state.get_data()
    list_item = []
    list_item.append(dt["avr_check"])
    list_item.append(dt["max_check"])
    list_item.append(dt["max_count"])
    list_item.append(dt["min_redemption"])
    list_item.append(dt["proc_sale"])
    list_item.append(dt["proc_missrvenue"])
    list_item.append(dt["proc_turnover"])
    a = []
    for l in list_item:
        if l == 'False':
            a.append(l)
    if len(a) >= 3:
        await bot.send_message(
                message.from_user.id,
                text=mes.question_skip
            )
        return

    await bot.send_message(
            message.from_user.id,
            text=mes.report_wait
        )


    season = dt["season"]
    avr_check = dt["avr_check"]
    max_check = dt["max_check"]
    max_count = dt["max_count"]
    min_redemption = dt["min_redemption"]
    proc_sale = dt["proc_sale"]
    proc_missrvenue = dt["proc_missrvenue"]
    proc_turnover = dt["proc_turnover"]
    
    await excel_report(season,
                       avr_check,
                       max_check,
                       max_count,
                       min_redemption,
                       proc_sale,
                       proc_missrvenue,
                       proc_turnover,
                       message,
                       db_session,
                       state,
                       is_message = True)
    await state.clear()

    await bot.send_message(
        message.from_user.id,
        text=mes.report_text)

    users_repo = UsersRepository(db_session)
    user = await users_repo.get(telegram_id=message.from_user.id)
    
    settings_repo = SettingsRepository(db_session)
    setting = await settings_repo.get(id=1)

    if config.dbs["subscribe"] == "2" or config.dbs["subscribe"] == "3":
        user_channel_status = await bot.get_chat_member(chat_id=config.channel_id,user_id=message.from_user.id)

        if user_channel_status.status != 'left':
            user.is_subscribe = True
            await users_repo.update(user)
            await bot.send_message(
                message.from_user.id,
                text="Сделать подбор ещё раз?",
                reply_markup=new_kb(user))

        else:
            user.is_subscribe = False
            await users_repo.update(user)
            await bot.send_message(
                message.from_user.id,
                text=mes.subscribe, reply_markup=subscribe())
    else:
        await bot.send_message(
            message.from_user.id,
            text="Сделать подбор ещё раз?",
            reply_markup=new_kb(user)
        )
    