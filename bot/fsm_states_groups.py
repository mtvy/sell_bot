from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterForm(StatesGroup):
    register = State()


class FilterCreateForm(StatesGroup):
    action = State()
    season = State()
    cloth = State()
    cloth_type = State()
    avr_check = State()
    max_check = State()
    max_count = State()
    min_redemption = State()
    proc_sale = State()
    proc_missrvenue = State()
    proc_turnover = State()
    add_data_month = State()
    add_data_next = State()
