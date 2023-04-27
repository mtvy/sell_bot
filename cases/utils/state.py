from cases.utils.msg import *
from telebot import TeleBot

# class Categories:
#     season : str = None 
#     niche : str = None 
#     clothes : str = None 
#     clothes_cat : str = None

#     def __init__(self) -> None:
#         self.is_active = True



class State:
    res1 : int = 0 
    res2 : int = 0 
    res3 : int = 0
    res4 : int = 0 
    res5 : int = 0 
    res6 : int = 0 
    res7 : int = 0
    skipped: int = 0

    def __init__(self) -> None:
        self.is_active = True 

    def close(self, log, bot: TeleBot, tid: str|int, categories) -> None:
        #make_res
        self.is_active = False 
        def excel_report(res1, res2, res3, res4, res5, res6, res7):
            my_list = [["Товар",
            "Кол-во товарных карточек",
            "Кол-во товарных карточек с продажами",
            "% товарных карточек с продажами (без учета неактивных SKU)",
            "Кол-во продавцов",
            "Кол-во продавцов с продажами",
            "% продавцов с продажами",
            "% выкупа от заказов",
            "Выручка без учета % выкупов",
            "Выручка с учетом % выкупа",
            "Потенциальная выручка, руб",
            "Упущенная выручка, руб",
            "% упущенной выручки",
            "Оборачиваемость, %",
            "Средняя выручка с учетом выкупов на 1 товар, руб",
            "Средняя цена за единицу товара. руб",
            "Ранг"]]
            #функция формирования и отправки отчета
            send_msg(log, bot, tid, 'hi')


states: dict[int, State] = dict()
state = State()

# categories: dict[int, Categories] = dict()
# category = Categories()