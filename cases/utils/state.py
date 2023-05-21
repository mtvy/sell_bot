from cases.utils.msg import *
from telebot import TeleBot

from telebot.types import (
    ReplyKeyboardRemove as rmvKb,
)

import pandas as pd

# class Categories:
#     season : str = None 
#     niche : str = None 
#     clothes : str = None 
#     clothes_cat : str = None

#     def __init__(self) -> None:
#         self.is_active = True



class State:
    season: str = ""
    sphere: str = ""
    type: str = ""

    res1: int = 0 
    res2: int = 0 
    res3: int = 0
    res4: int = 0 
    res5: int = 0 
    res6: int = 0 
    res7: int = 0
    skipped: int = 0

    last_mid: int = 0

    def __init__(self, tid) -> None:
        self.is_active = True
        self.tid = tid 
        self.type = ""

    def close(self, log, bot: TeleBot, tid: int|str) -> None:
        
        def send_default() -> None:
            df = pd.read_excel('docs/last_month.xlsx' if self.season=='last_season' else 'docs/next_month.xlsx') #, usecols=[0, 1, 2], nrows=10)
            tb = df.to_dict()
            keys = list(tb.keys())
            if len(keys) > 10:
                indexes_to_drop = []
                if self.sphere != 'all':
                    if self.sphere == 'goods':
                        for ind, i in tb[keys[0]].items():
                            if "товар" not in i.lower():
                                indexes_to_drop.append(ind)
                    elif self.sphere == 'clothes':
                        for ind, i in tb[keys[0]].items():
                            if "одежда" not in i.lower():
                                indexes_to_drop.append(ind)
                    for ind in indexes_to_drop:
                        df = df.drop(index=ind)
                    indexes_to_drop = []
                    tb = df.to_dict()

                if self.type != "" and self.type != 'all_cl':
                    if self.type == 'women':
                        for ind, i in tb[keys[0]].items():
                            if "женская" not in i.lower():
                                indexes_to_drop.append(ind)
                    elif self.type == 'men':
                        for ind, i in tb[keys[0]].items():
                            if "мужская" not in i.lower():
                                indexes_to_drop.append(ind)
                    elif self.type == 'child':
                        for ind, i in tb[keys[0]].items():
                            if "детская" not in i.lower():
                                indexes_to_drop.append(ind)
                    for ind in indexes_to_drop:
                        df = df.drop(index=ind)
                    indexes_to_drop = []
                    tb = df.to_dict()
                
                if self.res1 > 0:
                    for ind, i in tb[keys[15]].items():
                        if isinstance(i, int) or i.isdigit():
                            if self.res1 >= int(i):
                                indexes_to_drop.append(ind)
                    for ind in indexes_to_drop:
                        df = df.drop(index=ind)
                    indexes_to_drop = []
                    tb = df.to_dict()

                if self.res2 > 0:
                    for ind, i in tb[keys[15]].items():
                        if isinstance(i, int) or i.isdigit():
                            if self.res2 <= int(i):
                                indexes_to_drop.append(ind)
                    for ind in indexes_to_drop:
                        df = df.drop(index=ind)
                    indexes_to_drop = []
                    tb = df.to_dict()

                if self.res3 > 0:
                    for ind, i in tb[keys[1]].items():
                        if isinstance(i, int) or i.isdigit():
                            if self.res3 <= int(i):
                                indexes_to_drop.append(ind)
                    for ind in indexes_to_drop:
                        df = df.drop(index=ind)
                    indexes_to_drop = []
                    tb = df.to_dict()
                
                if self.res4 > 0:
                    for ind, i in tb[keys[7]].items():
                        x=0
                        if isinstance(i, float):
                           x = i*100
                        elif isinstance(i, str):
                            x = i[:-1]
                            if x.isdigit():
                                x = int(x)
                            else:
                                continue
                        if self.res4 >= x:
                            indexes_to_drop.append(ind)
                    for ind in indexes_to_drop:
                        df = df.drop(index=ind)
                    indexes_to_drop = []
                    tb = df.to_dict()

                if self.res5 > 0:
                    for ind, i in tb[keys[3]].items():
                        x=0
                        if isinstance(i, float):
                           x = i*100
                        elif isinstance(i, str):
                            x = i[:-1]
                            if x.isdigit():
                                x = int(x)
                            else:
                                continue
                        if self.res5 >= int(x):
                            indexes_to_drop.append(ind)
                    for ind in indexes_to_drop:
                        df = df.drop(index=ind)
                    indexes_to_drop = []
                    tb = df.to_dict()

                if self.res6 > 0:
                    for ind, i in tb[keys[3]].items():
                        x=0
                        if isinstance(i, float):
                           x = i*100
                        elif isinstance(i, str):
                            x = i[:-1]
                            if x.isdigit():
                                x = int(x)
                            else:
                                continue
                        if self.res6 <= int(x):
                            indexes_to_drop.append(ind)
                    for ind in indexes_to_drop:
                        df = df.drop(index=ind)
                    indexes_to_drop = []
                    tb = df.to_dict()

                if self.res7 > 0:
                    for ind, i in tb[keys[13]].items():
                        x=0
                        if isinstance(i, float):
                           x = i*100
                        elif isinstance(i, str):
                            x = i[:-1]
                            if x.isdigit():
                                x = int(x)
                            else:
                                continue
                        if self.res7 >= int(x):
                            indexes_to_drop.append(ind)
                    for ind in indexes_to_drop:
                        df = df.drop(index=ind)
                    indexes_to_drop = []
                    tb = df.to_dict()

            bytes_io = io.BytesIO()
            with pd.ExcelWriter(bytes_io) as writer:
                df.to_excel(writer, index=False)

            doc = bytes_io.getvalue()

            # with open(f'docs/last_month.xlsx', 'rb') as f:
                # doc = f.read()
            # doc = str(doc)
            # df.to_csv(index=False).encode('utf-8')
            send_doc(log, bot, tid, '', doc, name='data.xlsx')
            send_msg(log, bot, tid, 'Если у вас возникли вопросы или нужна помощь с таблицей, напишите мне @ilyalikhopoy', rmvKb())
            send_msg(log, bot, tid, 'Сделать подбор ещё раз?', get_ikb(log, {'Главное меню': 'menu'}))
        
        self.is_active = False 
        send_msg(log, bot, tid, "Все данные получены, отчет формируется. Пожалуйста, подожди минуту и я пришлю его в этот чат.")
        send_default()
    
    def __str__(self) -> str:
        return f"""
        Активный: {self.is_active}
        Сезон: {self.season}
        Ниша: {self.sphere}
        Тип: {self.type}
        Опрос #1: {self.res1}
        Опрос #2: {self.res2}
        Опрос #3: {self.res3}
        Опрос #4: {self.res4}
        Опрос #5: {self.res5}
        Опрос #6: {self.res6}
        Опрос #7: {self.res7}
        Пропуски: {self.skipped}
        """


states: dict[int, State] = dict()



# categories: dict[int, Categories] = dict()
# category = Categories()