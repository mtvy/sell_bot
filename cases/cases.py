from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardRemove as rmvKb, CallbackQuery
from .utils.msg import *
from bot import bot 

ADKB = ...
GET_CALC = 'calculate'
DEFAULTKB_1 = {'Сделать расчет' : GET_CALC}
SEASONS = {'Летний сезон' : 'summer', "Прошлый сезон" : 'last_season', 'Отмена': 'cancel'}
SKIP = 'Пропустить вопрос'
SKIP_Q = {"Пропустить вопрос" : 'skip'}
QUES3 = {'1000' : '1000', '10 000' : '10 000', '50 000' : '50 000', '100 000' : '100 000', SKIP:'skip'}
QUES4_5 = {'30%' : '30', '50%':'50', '70%':'70', '90%' : '90', SKIP:'skip'}
QUES6 = {'10%' : '10' , '30%':'30', '50%':'50', '70%':'70',SKIP:'skip'}
QUES7 = {'20%' : '20', '50%' : '50', '70%' : '50', '100%':'100', SKIP:'skip'}
MISSERR = 'Вы пропустили 3 вопроса. Максимальное числов не отвеченных вопросов не должно превышать 2 '
MENU = {'Главное меню' : 'menu'}
NISHES = {'Одежда':'clothes', 'Товары': 'goods', 'Все ниши': 'all', 'Отмена': 'cancel'}
CLOTHES = {'Женская': 'women', 'Мужская': 'men', 'Детская': 'child', 'Вся одежда': 'all_cl', 'Отмена': 'cancel'}

WAITTXT = '''Все данные получены, отчет формируется.

Пожалуйста, подожди минуту и я пришлю его в этот чат'''

txt1 = """1/7

Теперь, определим диапазон цен для подбора товара.
❓Укажи средний минимальный чек товара в рублях, который ты  хотел бы продавать

Пример: 1500"""

txt2 = """2/7

❓Укажи максимальный средний чек товара в рублях, который ты хотел бы продавать

Пример: 3500"""

txt3 = """3/7

❓Выбери по кнопкам ниже или напиши максимальное количество товаров конкурентов в категории

От этого параметра зависит уровень конкуренции в нише, которую подберет бот"""

txt4 = """4/7

❓Выбери  по кнопкам ниже или напиши минимальный % выкупа.

Параметр указывает, какой процент в нише покупатели выкупают с пункта выдачи заказов. Чем больше % выкупа, тем меньше потребуется вложений для захода в нишу."""

txt5 = """5/7

❓ Выбери или напиши % товара с продажами.

Параметр задает процент товаров в нише, которые имеют продажи каждый месяц"""

txt6 = """6/7

❓ Выбери по кнопкам ниже или напиши минимальный % упущенной выручки.

Это выручка, которую не получили продавцы из-за отсутствия товара на складах."""

txt7 = """7/7

❓Выбери по кнопкам ниже или напиши минимальный % оборачиваемости

Параметр определяет, сколько процентов от остатка будет продано за месяц.

100%: весь товар в нише продается за месяц
70%: весь товар в нише продается за 1,4 месяца
50%: весь товар в нише продается за 2 месяца
20%: весь товар в нише продается за 5 месяцев"""

maketxt = """⚠️Чтобы бот подобрал ниши для выхода на маркетплейс,
тебе необходимо задать параметры выборки.

Всего 7 параметров. Чтобы сформировать выборку, необходимо задать минимум 5.

Следуй инструкциям бота и в конце получишь персональную подборку в таблице из 100 подходящих тебе товаров для работы на Wildberries.

👉🏻 Жми кнопку ниже, чтобы начать"""

seasontxt = """❓Для начала, выбери сезон для анализа:

Параметр влияет на то, какой сезон будет анализироваться.
Если рассматриваешь сезонные товары - жми сезон.
Если рассматриваешь товары, которые продаются всегда - жми прошлый месяц"""

nichestxt = """❓Какую нишу будем рассматривать ?

В текущей версии бота можно проанализировать отдельно  товары или сделать анализ по всем нишам сразу."""

categorytxt = 'ℹ️ Выберите категорию одежды.'


def create_ask(log, bot: TeleBot, tid: str|int):
  
    wait_msg(log, bot, tid, qs2, txt1, get_ikb(log, SKIP_Q))

#@bot.callback_query_handler(func=lambda call: True)
def qs2(log, bot:TeleBot, tid, data, msg: Message|None):
   # global cid2
    # cid2 = call.message.id
    # uid = call.from_user.id
    # unid = call.from_user.username
    # mid = call.message.message_id

    # data = call.data 
    msg = msg.text

    if msg:
        if msg.isdigit():
            #save_ans
            qs2 = wait_msg(log, bot, tid, qs3, txt2, get_ikb(log, QUES3))
            
        
    elif data:
        #save_ans
        qs3(log, bot, tid)
    

#@bot.callback_query_handler(func=lambda call: True)
def qs3(log, bot:TeleBot, call: CallbackQuery, data, tid, msg: Message|None):
    #global cid3
    cid3 = call.message.id
    uid = call.from_user.id
    unid = call.from_user.username
    mid = call.message.message_id

    data = call.data 
    msg = msg.text
    if msg:
        if msg.isdigit():
            #save_ans
            qs3 = wait_msg(log, bot, tid, qs4, txt3, get_ikb(log, QUES4_5))
           
    elif data:
        #save_ans
        pass 


#@bot.callback_query_handler(func=lambda call: True)
def qs4(log, bot:TeleBot, call: CallbackQuery|None, tid, msg: Message|None):
    data = call.data 
    msg = msg.text 

    if msg:    
        if msg.isdigit():
            #save_ans
            qs4 = wait_msg(log, bot, tid, qs5, txt4, get_ikb(log, QUES4_5))
            
    elif data:
        #save_ans
        send_msg(log, bot, tid, txt4, get_ikb(log, QUES4_5))


#@bot.callback_query_handler(func=lambda call: True)
def qs5(log, bot:TeleBot, call: CallbackQuery|None, tid, msg: Message|None):
    data = call.data 

    if msg:    
        qs5 = wait_msg(log, bot, tid, qs6, txt5, get_ikb(log, QUES4_5))
        
    elif data:
        send_msg(log, bot, tid, txt6, get_ikb(log, QUES6))


#@bot.callback_query_handler(func=lambda call:True)
def qs6(log, bot:TeleBot, call: CallbackQuery, tid, msg: Message|None):
    data = call.data 
    if msg:
        qs6 = wait_msg(log, bot, tid, qs7, txt6, get_ikb(log, QUES6))
        
    elif data:
        pass

    if msg:
        qs7 = wait_msg(log, bot, tid, make_res, txt7, get_ikb(log, QUES7))
        
    elif data:
        pass 


def qs7(log, bot:TeleBot, call: CallbackQuery|None, tid, msg:Message|None=None):
    data = call.data 
    #save_ans
    send_msg(log, bot, tid, WAITTXT)

        

def make_res(log, bot:TeleBot, tid:str|int):
    pass



