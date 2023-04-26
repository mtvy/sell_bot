from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, Message
from resources import messages as mes
from sqlalchemy.ext.asyncio import AsyncSession
from utils import config
from bot_.keyboards.inline import quest_4_kb,quest_5_kb
from bot_.fsm_states_groups import FilterCreateForm
from utils.callback_data import CallbackData
from utils.analytics import log


router = Router()
bot = Bot(config.TELEGRAM_TOKEN, parse_mode="HTML")
dp = Dispatcher()

QUESTIONS_QUESTION__CD = CallbackData("questions_question", "action", "question")

@router.callback_query(QUESTIONS_QUESTION__CD.filter(action="4"))
async def job_delivery_method(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):
    await bot.answer_callback_query(q.id)
    callback_data = QUESTIONS_QUESTION__CD.parse(q.data)
    await state.update_data(action=callback_data["action"],
                            max_count=str(callback_data["question"]))
    dt = await state.get_data()
    list_item = []
    list_item.append(dt["avr_check"])
    list_item.append(dt["max_check"])
    list_item.append(dt["max_count"])
    a = []
    for l in list_item:
        if l == 'False':
            a.append(l)
    if len(a) >= 3:
        await bot.send_message(
                q.from_user.id,
                text="Вы пропустил 3 вопроса. Максимальное числов не отвеченных вопросов не должно превышать 2"
            )
        return
    await bot.send_message(
        q.from_user.id,
        text=mes.question_min_redemption_text, reply_markup=quest_5_kb())
    await log(user_id=q.from_user.id,
              user_lang_code=q.from_user.language_code,
              action_name='answer_5')
    await  state.set_state(FilterCreateForm.min_redemption)   

@router.message(state=FilterCreateForm.max_count)
async def job_delivery_method(message: Message, state: FSMContext, db_session: AsyncSession):
    if not  message.text.isdigit():
        return await message.answer(
            text="Введите целое число:",
            reply_markup=quest_4_kb())
        
    await state.update_data(
                        max_count=message.text)
    await bot.send_message(
        message.from_user.id,
        text=mes.question_min_redemption_text, reply_markup=quest_5_kb())                   
    await  state.set_state(FilterCreateForm.min_redemption)   