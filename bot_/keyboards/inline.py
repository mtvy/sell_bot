import datetime
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.callback_data import CallbackData
from utils.services import get_season
from resources import messages as mes


QUESTIONS_QUESTION__CD = CallbackData("questions_question", "action", "question")
FILE_CD = CallbackData("file", "action", "file_path")


def start_kb(user) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (1, 1, 1,2)
    builder.button(text='Сделать расчет', callback_data='yes_new')
    if user.is_admin is True:
        builder.button(text='Загрузить данные за прошлый месяц', callback_data='add_data_month')
        builder.button(text='Загрузить данные за будущий период', callback_data='add_data_next')
        builder.button(text='📊 Статистика',callback_data='stats')
        builder.button(text='Подписка',callback_data='sub_settings')
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)
    

def subscribe() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Продолжить', callback_data='yes_new')
    return builder.as_markup(resize_keyboard=True)


def excel_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Выгрузить данные в Excel', callback_data='excel')
    return builder.as_markup(resize_keyboard=True)


def new_kb(user) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Главное меню', callback_data='no_new')
    if user.is_admin is True:
        builder.button(text='Сделать расчет', callback_data='yes_new')
    return builder.as_markup(resize_keyboard=True)


def cancel_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Отмена', callback_data='cancel')
    return builder.as_markup(resize_keyboard=True)


def accept_kb(user, period, file_path) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='Отмена', callback_data='cancel')
    if user.is_admin is True:
        builder.button(text='Обновить данные', callback_data=FILE_CD.new(action=period, file_path=file_path))
    return builder.as_markup(resize_keyboard=True)



def choose_clothes() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (2, 2)
    builder.button(text="👚 Одежда", callback_data="clothes")
    builder.button(text="👛 Товары", callback_data="items")
    builder.button(text="🌟 Все ниши", callback_data="all")
    builder.button(text="Отмена", callback_data="cancel")
    #builder.button(text=mes.skip_quest_btn, callback_data=QUESTIONS_QUESTION__CD.new(action="4", question=False))
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)

def choose_clothes_type() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (2, 2,2)
    builder.button(text="👩 Женская", callback_data="women")
    builder.button(text="🤵‍♂ Мужская", callback_data="men")
    builder.button(text="👶 Детская", callback_data="children")
    builder.button(text="🌟 Вся одежда", callback_data="all_clothes")
    builder.button(text="Отмена", callback_data="cancel")
    #builder.button(text=mes.skip_quest_btn, callback_data=QUESTIONS_QUESTION__CD.new(action="4", question=False))
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)




def quest_1_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (1, 1, 1, 1)
    current_date = datetime.datetime.now()
    number = int(current_date.strftime("%m"))
    text = get_season(number)
    builder.button(text=text, callback_data=QUESTIONS_QUESTION__CD.new(action="1",question=1))
    builder.button(text=mes.last_month_btn, callback_data=QUESTIONS_QUESTION__CD.new(action="1",question=0))
    # builder.button(text=mes.last_year_btn, callback_data=QUESTIONS_QUESTION__CD.new(action="1",question=mes.last_year_btn))
    builder.button(text='Отмена', callback_data='cancel')
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)


def quest_2_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=mes.skip_quest_btn, callback_data=QUESTIONS_QUESTION__CD.new(action="2", question=False))
    return builder.as_markup(resize_keyboard=True)


def quest_3_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=mes.skip_quest_btn, callback_data=QUESTIONS_QUESTION__CD.new(action="3", question=False))
    return builder.as_markup(resize_keyboard=True)

def quest_4_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (2, 2, 1)
    builder.button(text="1000", callback_data=QUESTIONS_QUESTION__CD.new(action="4", question='1000'))
    builder.button(text="10 000", callback_data=QUESTIONS_QUESTION__CD.new(action="4", question='10000'))
    builder.button(text="50 000", callback_data=QUESTIONS_QUESTION__CD.new(action="4", question='50000'))
    builder.button(text="100 000", callback_data=QUESTIONS_QUESTION__CD.new(action="4", question='10000'))
    builder.button(text=mes.skip_quest_btn, callback_data=QUESTIONS_QUESTION__CD.new(action="4", question=False))
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)


def quest_5_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (2, 2, 1)
    builder.button(text="30%", callback_data=QUESTIONS_QUESTION__CD.new(action="5", question='30'))
    builder.button(text="50%", callback_data=QUESTIONS_QUESTION__CD.new(action="5", question='50'))
    builder.button(text="70%", callback_data=QUESTIONS_QUESTION__CD.new(action="5", question='70'))
    builder.button(text="90%", callback_data=QUESTIONS_QUESTION__CD.new(action="5", question='90'))
    builder.button(text=mes.skip_quest_btn, callback_data=QUESTIONS_QUESTION__CD.new(action="5", question=False))
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)


def quest_6_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (2, 2, 1)
    builder.button(text="30%", callback_data=QUESTIONS_QUESTION__CD.new(action="6", question='30'))
    builder.button(text="50%", callback_data=QUESTIONS_QUESTION__CD.new(action="6", question='50'))
    builder.button(text="70%", callback_data=QUESTIONS_QUESTION__CD.new(action="6", question='70'))
    builder.button(text="90%", callback_data=QUESTIONS_QUESTION__CD.new(action="6", question='90'))
    builder.button(text=mes.skip_quest_btn, callback_data=QUESTIONS_QUESTION__CD.new(action="6", question=False))
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)


def quest_7_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (2, 2, 1)
    builder.button(text="10%", callback_data=QUESTIONS_QUESTION__CD.new(action="7", question='10'))
    builder.button(text="30%", callback_data=QUESTIONS_QUESTION__CD.new(action="7", question='30'))
    builder.button(text="50%", callback_data=QUESTIONS_QUESTION__CD.new(action="7", question='50'))
    builder.button(text="70%", callback_data=QUESTIONS_QUESTION__CD.new(action="7", question='70'))
    builder.button(text=mes.skip_quest_btn, callback_data=QUESTIONS_QUESTION__CD.new(action="7", question=False))
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)


def quest_8_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (2, 2, 1)
    builder.button(text="20%", callback_data=QUESTIONS_QUESTION__CD.new(action="8", question='20'))
    builder.button(text="50%", callback_data=QUESTIONS_QUESTION__CD.new(action="8", question='50'))
    builder.button(text="70%", callback_data=QUESTIONS_QUESTION__CD.new(action="8", question='70'))
    builder.button(text="100%", callback_data=QUESTIONS_QUESTION__CD.new(action="8", question='100'))
    builder.button(text=mes.skip_quest_btn, callback_data=QUESTIONS_QUESTION__CD.new(action="8", question=False))
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)


def stats_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (2, 2)
    builder.button(text="По языкам", callback_data="languages")
    builder.button(text="По датам", callback_data="by_date")
    builder.button(text="Назад", callback_data="main_menu")
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)


def to_stats() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (2, 2)
    builder.button(text="Назад", callback_data="stats")
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)

def sub_settings() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sizes = (2, 2,1)
    builder.button(text="/start", callback_data="sub:1")
    builder.button(text="Получения расчета", callback_data="sub:2")
    builder.button(text="Оба варианта", callback_data="sub:3")
    builder.button(text="Убрать", callback_data="sub:0")
    builder.button(text="Назад", callback_data="main_menu")
    builder.adjust(*sizes)
    return builder.as_markup(resize_keyboard=True)
