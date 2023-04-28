from telebot import TeleBot  
from telebot.types import (
    CallbackQuery,
    Message
)

import logger, dotenv, os 
from cases.utils.msg import *
from cases.cases import *
from cases.utils.state import *


log = logger.newLogger(__name__, logger.DEBUG)

dotenv.load_dotenv('.env')
token = os.getenv('TOKEN')
admins = os.getenv('ADMINS')

bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def start(msg: Message) -> None:
    tid = str(msg.chat.id)
    uid = msg.from_user.id
    states[tid] = State(tid)
    if tid in admins:
        log.info(f'Bot starting by user:{tid}.')
        send_msg(log, bot, tid, maketxt, get_ikb(log, ADMKB))
    
    else:
        log.info(f'Bot starting by user:{tid}.')
        if is_subscribed(bot, tid)!=True:
            send_msg(log, bot, tid, maketxt, get_ikb(log, DEFAULTKB_1))
        else:
            send_msg(log, bot, tid, substxt, get_ikb(log, CONTINUE))


@bot.message_handler(content_types=['text'])
def answers(msg : Message):
    txt = msg.text
    tid = msg.chat.id
    # state = State(tid)
    # states[tid] = state
    # states[tid]=State(tid)
    if str(tid) in admins:
        send_msg(log, bot, tid, txt1, get_ikb(log, ADKB))
    else:
         if txt.isdigit():
             
             if states[tid].is_active: 
                if states[tid].res1 == 0:
                    states[tid].res1 = int(txt)
                    send_msg(log, bot, tid, txt2, get_ikb(log, QUES2))

                elif states[tid].res2 == 0:
                    states[tid].res2 = int(txt)
                    send_msg(log, bot, tid, txt3, get_ikb(log, QUES3))

                elif states[tid].res3 == 0:
                    states[tid].res3 = int(txt)
                    send_msg(log, bot, tid, txt4, get_ikb(log, QUES4))
                    print(states[tid].res1)
                elif states[tid].res4 == 0:
                    states[tid].res4 = int(txt)
                    send_msg(log, bot, tid, txt5, get_ikb(log, QUES5))

                elif states[tid].res5 == 0:
                    states[tid].res5 = int(txt)
                    send_msg(log, bot, tid, txt6, get_ikb(log, QUES6))

                elif states[tid].res6 == 0:
                    states[tid].res6 = int(txt)
                    send_msg(log, bot, tid, txt7, get_ikb(log, QUES7))
                    
                elif states[tid].res7 == 0:
                    states[tid].res7 = int(txt)
                    states[tid].close(log, bot, tid)
         else:
            send_msg(log, bot, tid, 'Пришлите целое число')
    


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: CallbackQuery):
    cid = call.message.id
    tid = call.message.chat.id
    uid = call.from_user.id
    unid = call.from_user.username
    mid = call.message.message_id
    data = call.data 

    if data == 'continue':
        sub = is_subscribed(bot, tid)
        if sub == True:
            send_msg(log, bot, tid, maketxt, get_ikb(log, DEFAULTKB_1))
        else:
            send_msg(log, bot, tid, pitytxt, get_ikb(log, CONTINUE))

    if data=='cancel':
        #??
        del_msg(log, bot, cid, mid)
        
    if data == 'menu':
        del_msg(log, bot, cid, mid)
        send_msg(log, bot, tid, maketxt, get_ikb(log, DEFAULTKB_1))

    if data == 'calculate':
        del_msg(log, bot, cid, mid)
        send_msg(log, bot, tid, seasontxt, get_ikb(log, SEASONS))
    
    if data in list(SEASONS.values())[:-1]:
        
        del_msg(log, bot, cid, mid)
        send_msg(log, bot, tid, nichestxt, get_ikb(log, NISHES))
    
    if data == 'clothes':
        del_msg(log, bot, cid, mid) 
        send_msg(log, bot, tid, categorytxt, get_ikb(log, CLOTHES))
    
    if data == 'goods' or data == 'all':
        states[tid] = State(tid)
        if states[tid].is_active:
            del_msg(log, bot, cid, mid)
            send_msg(log, bot, tid, txt1, get_ikb(log, QUES_1))
    
    if data in list(CLOTHES.values())[:-1]:
        states[tid] = State(tid)
        if states[tid].is_active:
            del_msg(log, bot, cid, mid)
            send_msg(log, bot, tid, txt1, get_ikb(log, QUES_1))
        


    if Q1 in data:
       # states[tid] = state
        states[tid].res1 = -1
        states[tid].skipped += 1
        send_msg(log, bot, tid, txt2, get_ikb(log, QUES2))
        

    if Q2 in data:
        states[tid].res2 = -1
        states[tid].skipped += 1
        send_msg(log, bot, tid, txt3, get_ikb(log, QUES3))
        
        

    if Q3 in data:
        data = data.split(Q3)
        
        if data[0] != 'skip':
            value = int(data[0])
            states[tid].res3 = value
            send_msg(log, bot, tid, txt4, get_ikb(log, QUES4))
        else:
            states[tid].skipped+=1
            if states[tid].skipped >= 3:
                send_msg(log, bot, tid, MISSERR)
            else:
                states[tid].res3 = -1
                send_msg(log, bot, tid, txt4, get_ikb(log, QUES4))
            
    

    if Q4 in data:
        data = data.split(Q4)
        if data[0] != 'skip':
            value = int(data[0])
            states[tid].res4 = value
            send_msg(log, bot, tid, txt5, get_ikb(log, QUES5))
        else:
            states[tid].skipped+=1
            if states[tid].skipped >= 3:
                send_msg(log, bot, tid, MISSERR)
            else:
                states[tid].res4 = -1
                states[tid].skipped +=1
                send_msg(log, bot, tid, txt5, get_ikb(log, QUES5))

              

    if Q5 in data:
        data = data.split(Q5)
        if data[0] != 'skip':
            value = int(data[0])
            states[tid].res5 = value
            send_msg(log, bot, tid, txt6, get_ikb(log, QUES6))
        else:
            states[tid].skipped+=1
            if states[tid].skipped >= 3:
                send_msg(log, bot, tid, MISSERR)
            else:
                states[tid].res5 = -1
                states[tid].skipped += 1
                send_msg(log, bot, tid, txt6, get_ikb(log, QUES6))
                

    if Q6 in data:
        data = data.split(Q6)
        if data[0] != 'skip':
            value = int(data[0])
            states[tid].res6 = value
            send_msg(log, bot, tid, txt7, get_ikb(log, QUES7))
        else:
            states[tid].skipped+=1
            if states[tid].skipped >= 3:
                send_msg(log, bot, tid, MISSERR)
            else:
                states[tid].res6 = -1
                states[tid].skipped += 1
                send_msg(log, bot, tid, txt7, get_ikb(log, QUES7))
                

    if Q7 in data:
        data = data.split(Q7)
        if data[0] != 'skip':
            value = int(data[0])
            states[tid].res7 = value
            states[tid].close(log, bot, tid)
        else:
            states[tid].skipped+=1
            
            if states[tid].skipped >= 3:
                send_msg(log, bot, tid, MISSERR)
            else:
                states[tid].res7 = -1 
                states[tid].skipped += 1
                states[tid].close(log, bot, tid)



if __name__ == "__main__":
    try:
        log.info(f'Token:{token}')
        log.info(f'Admins:{admins}')
        log.info('Starting...')
        bot.polling(allowed_updates="chat_member")
    except Exception as err:
        log.error(err)







