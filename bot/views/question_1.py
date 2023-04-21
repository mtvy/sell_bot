from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery
from resources import messages as mes
from sqlalchemy.ext.asyncio import AsyncSession
from utils import config
from bot.keyboards.inline import quest_2_kb,choose_clothes,choose_clothes_type,stats_menu,to_stats,start_kb,sub_settings
from bot.fsm_states_groups import FilterCreateForm
from utils.callback_data import CallbackData
from utils.analytics import log
from langcodes import Language
from db import UsersRepository
from prettytable import PrettyTable
import datetime


router = Router()
bot = Bot(config.TELEGRAM_TOKEN, parse_mode="HTML")
dp = Dispatcher()


QUESTIONS_QUESTION__CD = CallbackData("questions_question", "action", "question")


@router.callback_query(QUESTIONS_QUESTION__CD.filter(action="1"))
async def seasons_heandler(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):
    callback_data = QUESTIONS_QUESTION__CD.parse(q.data)
    await state.update_data(action=callback_data["action"],
                            season=int(callback_data["question"]))
    await q.message.edit_text(
        text=mes.choose_clothes,
        reply_markup=choose_clothes()
    )
    
@router.callback_query(text= ["items","all"])
async def seasons_heandler(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):    
    await state.update_data(clothes=q.data)
    await q.message.edit_text(
        text=mes.question_avr_check_text,
        reply_markup=quest_2_kb()
    )
    await state.set_state(FilterCreateForm.avr_check)
    await log(user_id=q.from_user.id,
              user_lang_code=q.from_user.language_code,
              action_name='answer_2')


@router.callback_query(text= ["clothes"])
async def seasons_heandler(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):    
    await state.update_data(clothes=q.data)
    await q.message.edit_text(
        text=mes.choose_clothes_type,
        reply_markup=choose_clothes_type()
    )

@router.callback_query(text= ["women","children","men","all_clothes"])
async def seasons_heandler(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):    
    await state.update_data(clothes_type=q.data)
    await q.message.edit_text(
        text=mes.question_avr_check_text,
        reply_markup=quest_2_kb()
    )
    await state.set_state(FilterCreateForm.avr_check)
    await log(user_id=q.from_user.id,
              user_lang_code=q.from_user.language_code,
              action_name='answer_2')
              
             
@router.callback_query(text="stats")
async def m(query,db_session,state):
    await query.message.edit_text("Выберите нужный раздел",reply_markup=stats_menu())
    
    
    
    
    
    
    
@router.callback_query(text="languages")
async def m(query,db_session,state):
    user = UsersRepository(db_session)
    users = await user.get_many()
    countrys_lang_count = {}
    today=week=month=0
    for user in users:
        
        language = Language.make(language=user.language).display_name()
        if "Unknown language" in language:
            language="Неизвестных"
        if countrys_lang_count.get(language):
            countrys_lang_count[language]=countrys_lang_count[language]+1
        else:
            countrys_lang_count[language]=1
        
        if user.created_at.date()==datetime.datetime.now().date():
           today+=1
        elif user.created_at.date()>(datetime.datetime.now() - datetime.timedelta(days=7)).date():
            week+=1
        elif user.created_at.date()>(datetime.datetime.now() - datetime.timedelta(days=31)).date():
            month+=1
    x = PrettyTable()
    x.field_names = ["Язык", "Количество"]
    print(today,week,month)
    for i in countrys_lang_count:
        x.add_row([i,countrys_lang_count[i]])
    await query.message.edit_text(f"<code>{x}</code>",reply_markup=to_stats())
    

@router.callback_query(text="by_date")
async def m(query,db_session,state):
    user = UsersRepository(db_session)
    users = await user.get_many()
    banned = 0
    text = """▪️ Общая статистика 
Всего пользователей: {}
Заблокированных: {}

▪️ Количество новых пользователей за последние 30 дней\n<code>{}</code>

▪️ Активность пользователей
за сегодня: {}
за неделю: {}
за месяц: {}
"""
    date_list = {}
    today=week=month=0
    for user in users:
        if user.is_banned:
            banned+=1
        if user.last_active.date()==datetime.datetime.now().date():
           today+=1
        if user.last_active.date()>(datetime.datetime.now() - datetime.timedelta(days=7)).date():
            week+=1
        if user.last_active.date()>(datetime.datetime.now() - datetime.timedelta(days=31)).date():
            month+=1
        if user.created_at.date()<(datetime.datetime.now() - datetime.timedelta(days=31)).date():
            continue
        date = str(user.created_at.date())
        if date_list.get(date):
            date_list[date]=date_list[date]+1
        else:
            date_list[date]=1
    x = PrettyTable()
    x.field_names = ["Дата", "Количество"]
    for i in date_list:
        x.add_row([i,date_list[i]])    
        
    text = text.format(len(users),banned,str(x),today,week,month)
    print(text)
    await query.message.edit_text(text,reply_markup=to_stats())
 
@router.callback_query(text="main_menu")
async def m(query,db_session,state):
    users_repo = UsersRepository(db_session)
    user = await users_repo.get(telegram_id=query.from_user.id)
    await query.message.edit_text(
                    text=mes.start_text,
                    reply_markup=start_kb(user)
                    ) 


@router.callback_query(text = "sub_settings")
async def message(query):
    await query.message.edit_text(text = "Выберите вариант подписки", reply_markup=sub_settings())
    
@router.callback_query(lambda call:"sub:" in call.data)
async def message(query):    
    await query.answer("ℹ️ Режим подписки изменён",show_alert=True)
    config.dbs["subscribe"]=query.data.split(":")[1]
    