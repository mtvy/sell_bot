from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, Message
from resources import messages as mes
from sqlalchemy.ext.asyncio import AsyncSession
from utils import config
from bot.keyboards.inline import quest_3_kb, quest_4_kb
from bot.fsm_states_groups import FilterCreateForm
from utils.callback_data import CallbackData
from utils.analytics import log


router = Router()
bot = Bot(config.TELEGRAM_TOKEN, parse_mode="HTML")
dp = Dispatcher()

QUESTIONS_QUESTION__CD = CallbackData("questions_question", "action", "question")


@router.callback_query(QUESTIONS_QUESTION__CD.filter(action="3"))
async def seasons_heandler(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):
    await bot.answer_callback_query(q.id)
    callback_data = QUESTIONS_QUESTION__CD.parse(q.data)
    await state.update_data(action=callback_data["action"],
                            max_check=str(callback_data["question"]))
    await bot.send_message(
        q.from_user.id,
        text=mes.question_max_count_text, reply_markup=quest_4_kb())
    await log(user_id=q.from_user.id,
              user_lang_code=q.from_user.language_code,
              action_name='answer_4')
    await state.set_state(FilterCreateForm.max_count)

@router.message(state=FilterCreateForm.max_check)
async def job_delivery_method(m: Message, state: FSMContext, db_session: AsyncSession):
    dt = await state.get_data()
    try:
        max_check = int(m.text)
        if dt['avr_check'] != "False":
            if max_check <= int(dt['avr_check']):
                await m.answer(
                    text=f"Введите число превышающее {int(dt['avr_check'])} Средний чек товара:",
                    reply_markup=quest_3_kb())
                return
        await state.update_data(max_check=m.text)

    except:
        await m.answer(
            text="Введите целое число:",
            reply_markup=quest_3_kb())
        return
    await state.update_data(max_check=m.text)
    await m.answer(
        text=mes.question_max_count_text, reply_markup=quest_4_kb())
    await log(user_id=m.from_user.id,
              user_lang_code=m.from_user.language_code,
              action_name='answer_4')
    await state.set_state(FilterCreateForm.max_count)