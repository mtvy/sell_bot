from telebot import TeleBot  
from telebot.types import (
    ReplyKeyboardRemove as rmvKb,
    CallbackQuery,
    Message
)

import logger, traceback as tb 
import environ 
import cases
from cases.utils.msg import *
from cases.cases import *


log = logger.newLogger(__name__, logger.DEBUG)
env = environ.Env()
environ.Env.read_env()

token = env("TOKEN")
admins = env("ADMINS")

bot = TeleBot(token)




@bot.message_handler(commands=['start'])
def start(msg: Message) -> None:

    tid = str(msg.chat.id)
    if tid in admins:
        log.info(f'Bot starting by user:{tid}.')
        send_msg(log, bot, tid, get_ikb(log, ADKB))
    
    else:
        log.info(f'Bot starting by user:{tid}.')
        send_msg(log, bot, tid, get_ikb(log, DEFAULTKB_1))


@bot.message_handler(content_types=['text'])
def answers(msg : Message):
    msg_ = msg.text
    tid = str(msg.chat.id)
    if tid in admins:
        send_msg(log, bot, tid, get_ikb(log, ADKB))
    else:
        if msg_.isdigit():
            #здесь пропишу функцию сохранения ответов
            create_ask(log, bot, tid)
    


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: CallbackQuery, msg: Message):
    skipped = 0
    cid = call.message.id
    uid = call.from_user.id
    unid = call.from_user.username
    mid = call.message.message_id

    data = call.data 
    msg = msg.text
    tid = msg.chat.id
    
    if data=='cancel':
        #здесь пропишу функцию сохранения ответов
        del_msg(log, bot, cid, mid)

    if data == 'menu':
        del_msg(log, bot, cid, mid)
        send_msg(log, bot, tid, maketxt, get_ikb(log, DEFAULTKB_1))

    if data == 'calculate':
        del_msg(log, bot, cid, mid)
        send_msg(log, bot, tid, seasontxt, get_ikb(log, SEASONS))
    
    if data in SEASONS.values():
        send_msg(log, bot, tid, nichestxt, get_ikb(log, NISHES))
    
    if data == 'clothes':
        del_msg(log, bot, cid, mid) 
        send_msg(log, bot, tid, categorytxt, get_ikb(log, CLOTHES))
    
    if data == 'goods' or data == 'all':
        del_msg(log, bot, cid, mid)
        create_ask(log, bot, uid)
    
    if data in CLOTHES.values():
        del_msg(log, bot, cid, mid)
        create_ask(log, bot, uid, data)
    
    if data=='skip':
        create_ask(log, bot, uid)
        skipped+=1

        if skipped == 3:
            send_msg(log, bot, MISSERR)
    


if __name__ == "__main__":
    try:
        log.info('Starting...')
        bot.polling(allowed_updates="chat_member")
    except Exception as err:
        log.error(f'Get polling error.\n\n{err}\n\n{tb.format_exc()}')







