from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from resources import messages as mes


def skip_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text=mes.skip_quest_btn)
    return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


def quest_4_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    sizes = (2, 2, 1)
    builder.button(text="1000")
    builder.button(text="10 000")
    builder.button(text="50 000")
    builder.button(text="100 000")
    builder.button(text=mes.skip_quest_btn)
    builder.adjust(*sizes)
    return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


def quest_5_6_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    sizes = (2, 2, 1)
    builder.button(text="30%")
    builder.button(text="50%")
    builder.button(text="70%")
    builder.button(text="90%")
    builder.button(text=mes.skip_quest_btn)
    builder.adjust(*sizes)
    return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


def quest_7_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    sizes = (2, 2, 1)
    builder.button(text="10%")
    builder.button(text="30%")
    builder.button(text="50%")
    builder.button(text="70%")
    builder.button(text=mes.skip_quest_btn)
    builder.adjust(*sizes)
    return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


def quest_8_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    sizes = (2, 2, 1)
    builder.button(text="20%")
    builder.button(text="50%")
    builder.button(text="70%")
    builder.button(text="100%")
    builder.button(text=mes.skip_quest_btn)
    builder.adjust(*sizes)
    return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def register_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     builder.button(text=mes.reg_id_btn)
#     # builder.button(text=mes.iknow_id_btn)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def main_menu_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     sizes = (2, 2, 2, 2)
#     builder.button(text=mes.my_order_btn)
#     builder.button(text=mes.calc_delivery_btn)
#     builder.button(text=mes.my_addres_btn)
#     builder.button(text=mes.finance_btn)
#     builder.button(text=mes.settings_btn)
#     builder.button(text=mes.mes_manager_btn)
#     builder.adjust(*sizes)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def my_order_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     sizes = (2, 2)
#     builder.button(text=mes.create_oreder_btn)
#     builder.button(text=mes.status_order_btn)
#     builder.button(text=mes.history_order_btn)
#     builder.button(text=mes.main_menu_btn)
#     builder.adjust(*sizes)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def calc_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     sizes = (2, 2, 1)
#     builder.button(text=mes.hoz_calc_btn)
#     builder.button(text=mes.clothes_calc_btn)
#     builder.button(text=mes.shoes_calc_btn)
#     builder.button(text=mes.dangers_calc_btn)
#     builder.button(text=mes.main_menu_btn)
#     builder.adjust(*sizes)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def var_delivery_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     sizes = (2, 2, 2)
#     builder.button(text=mes.avia_btn)
#     builder.button(text=mes.fast_auto_btn)
#     builder.button(text=mes.auto_btn)
#     builder.button(text=mes.rail_btn)
#     builder.button(text=mes.sea_btn)
#     builder.button(text=mes.main_menu_btn)
#     builder.adjust(*sizes)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def addres_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     sizes = (2, 1)
#     builder.button(text=mes.add_addres_rus_btn)
#     builder.button(text=mes.add_addres_cny_btn)
#     builder.button(text=mes.main_menu_btn)
#     builder.adjust(*sizes)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def mes_manager_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     builder.button(text=mes.send_btn)
#     builder.button(text=mes.main_menu_btn)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def disable_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     builder.button(text=mes.disable_btn)
#     builder.button(text=mes.main_menu_btn)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def enable_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     builder.button(text=mes.enable_btn)
#     builder.button(text=mes.main_menu_btn)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def cancel_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     builder.button(text=mes.main_menu_btn)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def back_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     builder.button(text=mes.back)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def register_manager_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     builder.button(text=mes.mes_reg_btn)
#     builder.button(text=mes.back)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def category_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     sizes = (2, 2, 1, 1)
#     builder.button(text=mes.hoz_calc_btn)
#     builder.button(text=mes.clothes_calc_btn)
#     builder.button(text=mes.shoes_calc_btn)
#     builder.button(text=mes.dangers_calc_btn)
#     builder.button(text=mes.other_btn)
#     builder.button(text=mes.main_menu_btn)
#     builder.adjust(*sizes)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def packaging_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     sizes = (2, 2, 1, 1)
#     builder.button(text="Мешок скотч")
#     builder.button(text="Рёбра жёсткости")
#     builder.button(text="Обрешетка")
#     builder.button(text="Паллет")
#     builder.button(text=mes.other_btn)
#     builder.button(text=mes.main_menu_btn)
#     builder.adjust(*sizes)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def calc_category_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     sizes = (2, 2, 1)
#     builder.button(text=mes.hoz_calc_btn)
#     builder.button(text=mes.clothes_calc_btn)
#     builder.button(text=mes.shoes_calc_btn)
#     builder.button(text=mes.dangers_calc_btn)
#     builder.button(text=mes.main_menu_btn)
#     builder.adjust(*sizes)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)

# def delivery_method_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     sizes = (2, 2, 2, 1)
#     builder.button(text=mes.avia_btn)
#     builder.button(text=mes.fast_auto_btn)
#     builder.button(text=mes.auto_btn)
#     builder.button(text=mes.rail_btn)
#     builder.button(text=mes.sea_btn)
#     builder.button(text=mes.dont_know_btn)
#     builder.button(text=mes.main_menu_btn)
#     builder.adjust(*sizes)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def calc_delivery_method_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     sizes = (2, 2, 2)
#     builder.button(text=mes.avia_btn)
#     builder.button(text=mes.fast_auto_btn)
#     builder.button(text=mes.auto_btn)
#     builder.button(text=mes.rail_btn)
#     builder.button(text=mes.sea_btn)
#     builder.button(text=mes.main_menu_btn)
#     builder.adjust(*sizes)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def status_kb(st) -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     sizes = (2, 2, 2)
#     for s in st:
#         if s.title != 'Создан':
#             builder.button(
#                 text=mes.status_title.format(status=s)
#                 )
#     builder.button(text=mes.main_menu_btn)
#     builder.adjust(*sizes)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def i_dont_know_kb() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     builder.button(text=mes.dont_know_btn)
#     builder.button(text=mes.main_menu_btn)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)


# def mes_manager_kb_2() -> ReplyKeyboardMarkup:
#     builder = ReplyKeyboardBuilder()
#     builder.button(text=mes.mes_manager_btn)
#     builder.button(text=mes.main_menu_btn)
#     return ReplyKeyboardMarkup(keyboard=builder.export(), resize_keyboard=True)