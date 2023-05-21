from telebot import TeleBot 
from telebot.types import (
    ReplyKeyboardRemove as rmvKb,
    CallbackQuery,
    Message,
)
from prettytable import PrettyTable
from texttable import Texttable
from tabulate import tabulate

import pandas as pd
import logger, dotenv, os
import cases

REPLY = "reply"
LOAD_LAST_MONTH_DATA = "Загрузить данные за прошлый месяц"


log = logger.newLogger(__name__, logger.DEBUG)

dotenv.load_dotenv('.env')
token = os.getenv('TOKEN')
admins = os.getenv('ADMINS')
dev = os.getenv('DEV')

bot = TeleBot(token)

def is_user_exist(users: dict[str, list], tid: int) -> bool:
    if not len(users):
        return
    
    for user in users.values():
        if user[1] == tid:
            log.debug(f'tid:{tid} at user:{user}')
            return True
    return False

@bot.message_handler(commands=['start'])
def start(msg: Message) -> None:
    tid = msg.chat.id
    username = msg.chat.username
    cases.states[tid] = cases.State(tid)
    if str(tid) in admins:
        log.info(f'Bot starting by user:{tid}.')
        cases.send_msg(log, bot, tid, cases.maketxt, cases.get_ikb(log, cases.ADMKB))
    
    else:
        log.info(f'Bot starting by user:{tid}.')

        data, stat = cases.db.get('*', 'user_tb', '')
        if stat != 'ok':
            log.error(f'stat:{stat} data:{data}')
            cases.send_msg(log, bot, dev, cases.DBERR, cases.get_kb(log, cases.DEFALTKB))
            return
        
        is_subed = cases.is_subscribed(bot, tid)
        if not is_user_exist(data, tid) and (stat := cases.db.insert('user_tb', 'tid, username, is_subscribe', f"({tid}, '{username}', {is_subed})").status) != 'ok':
            log.error(stat)
            cases.send_msg(log, bot, dev, 'Ошибка.', rmvKb())
        
        if is_subed:
            cases.send_msg(log, bot, tid, cases.maketxt, cases.get_ikb(log, cases.DEFAULTKB_1))
        else:
            cases.send_msg(log, bot, tid, cases.substxt, cases.get_ikb(log, cases.CONTINUE))


@bot.message_handler(content_types=['text'])
def answers(msg : Message):
    txt = msg.text
    tid = msg.chat.id
    mid = msg.message_id
    # state = cases.State(tid)
    # cases.states[tid] = state
    # cases.states[tid]=cases.State(tid)
    # if str(tid) in admins:
    #     cases.send_msg(log, bot, tid, "Вы админ!")
    #     cases.send_msg(log, bot, tid, cases.txt1, cases.get_ikb(log, ADKB))
    # else:
    if txt.isdigit():
        if is_state_valid(log, bot, tid): 
            cases.del_msg(log, bot, tid, cases.states[tid].last_mid)
            if cases.states[tid].res1 == 0:
                cases.states[tid].res1 = int(txt)
                msg = cases.send_msg(log, bot, tid, cases.txt2, cases.get_ikb(log, cases.QUES2))
                cases.states[tid].last_mid = msg.message_id

            elif cases.states[tid].res2 == 0:
                cases.states[tid].res2 = int(txt)
                msg = cases.send_msg(log, bot, tid, cases.txt3, cases.get_ikb(log, cases.QUES3))
                cases.states[tid].last_mid = msg.message_id

            elif cases.states[tid].res3 == 0:
                cases.states[tid].res3 = int(txt)
                msg = cases.send_msg(log, bot, tid, cases.txt4, cases.get_ikb(log, cases.QUES4))
                cases.states[tid].last_mid = msg.message_id

            elif cases.states[tid].res4 == 0:
                cases.states[tid].res4 = int(txt)
                msg = cases.send_msg(log, bot, tid, cases.txt5, cases.get_ikb(log, cases.QUES5))
                cases.states[tid].last_mid = msg.message_id

            elif cases.states[tid].res5 == 0:
                cases.states[tid].res5 = int(txt)
                msg = cases.send_msg(log, bot, tid, cases.txt6, cases.get_ikb(log, cases.QUES6))
                cases.states[tid].last_mid = msg.message_id

            elif cases.states[tid].res6 == 0:
                cases.states[tid].res6 = int(txt)
                msg = cases.send_msg(log, bot, tid, cases.txt7, cases.get_ikb(log, cases.QUES7))
                cases.states[tid].last_mid = msg.message_id
                    
            elif cases.states[tid].res7 == 0:
                cases.states[tid].res7 = int(txt)
                cases.states[tid].close(log, bot, tid)
                msg = cases.send_msg(log, bot, 281321076, f"Новый опрос: {cases.states[tid]}", cases.get_ikb(log, {'Ответить': f'{tid}reply'}))
                cases.states[tid].last_mid = msg.message_id
    else:
        cases.send_msg(log, bot, tid, 'Нет такой функции.', rmvKb())
    
def is_state_valid(log, bot, tid) -> bool:
    if tid not in cases.states.keys() or not cases.states[tid].is_active:
        cases.send_msg(log, bot, tid, "Перезапустите опрос. /start")
        return False
    return True

def load_doc(msg: Message, log, bot: TeleBot, tid: int, mid: int, file_name: str) -> None:
    if msg.text == 'Отмена':
        cases.send_msg(log, bot, tid, 'Отмена.', rmvKb())
        return
    try:
        file_info = bot.get_file(msg.document.file_id)
        doc = bot.download_file(file_info.file_path)
        log.debug("Got doc")
        with open(f'docs/{file_name}.xlsx', 'wb') as f:
            f.write(doc)
        cases.send_msg(log, bot, tid, "Файл загружен.", rmvKb())
    except Exception as err:
        log.error(err)
        cases.wait_msg(log, bot, tid, load_doc, 'Отправьте таблицу в формате xlsx:', 
                 cases.get_kb(log, ["Отмена"]), [log, bot, tid, mid, file_name])

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: CallbackQuery):
    # cid = call.message.id
    tid = call.message.chat.id
    uid = call.from_user.id
    unid = call.from_user.username
    mid = call.message.message_id
    data = call.data 

    # if str(tid) in admins:
    #     cases.send_msg(log, bot, tid, "Вы администратор!")
    #     return

    if data == 'continue':
        if not cases.is_subscribed(bot, tid):
            cases.send_msg(log, bot, tid, cases.pitytxt, cases.get_ikb(log, cases.CONTINUE))
            return
        cases.send_msg(log, bot, tid, cases.maketxt, cases.get_ikb(log, cases.DEFAULTKB_1))
        return

    if data == 'cancel':
        cases.del_msg(log, bot, tid, mid)
        cases.send_msg(log, bot, tid, 'Отмена.')
        return

    if data in ("last_month", "next_month"):
        cases.del_msg(log, bot, tid, mid)
        cases.wait_msg(log, bot, tid, load_doc, 'Отправьте таблицу в формате xlsx:', 
                 cases.get_kb(log, ["Отмена"]), [log, bot, tid, mid, data])
        return
    
    if data == "last_month":
        cases.del_msg(log, bot, tid, mid)
        cases.wait_msg(log, bot, tid, load_doc, 'Отправьте таблицу в формате xlsx:', 
                 cases.get_kb(log, ["Отмена"]), [log, bot, tid, mid, "last_month"])
        return
        
    if data == 'menu':
        cases.del_msg(log, bot, tid, mid)
        cases.send_msg(log, bot, tid, cases.maketxt, cases.get_ikb(log, cases.DEFAULTKB_1))
        return

    if data == 'calculate':
        cases.del_msg(log, bot, tid, mid)
        cases.send_msg(log, bot, tid, cases.seasontxt, cases.get_ikb(log, cases.SEASONS))
        return
    
    if data in list(cases.SEASONS.values())[:-1]:
        if is_state_valid(log, bot, tid):
            cases.del_msg(log, bot, tid, mid)
            msg = cases.send_msg(log, bot, tid, cases.nichestxt, cases.get_ikb(log, cases.NISHES))
            cases.states[tid].season = data
            cases.states[tid].last_mid = msg.message_id
        return
    
    if data == 'clothes':
        if is_state_valid(log, bot, tid):
            cases.del_msg(log, bot, tid, mid) 
            msg = cases.send_msg(log, bot, tid, cases.categorytxt, cases.get_ikb(log, cases.CLOTHES))
            cases.states[tid].sphere = data
            cases.states[tid].last_mid = msg.message_id
        return
    
    if data == 'goods' or data == 'all':
        if is_state_valid(log, bot, tid):
            cases.del_msg(log, bot, tid, mid)
            msg = cases.send_msg(log, bot, tid, cases.txt1, cases.get_ikb(log, cases.QUES_1))
            cases.states[tid].sphere = data
            cases.states[tid].last_mid = msg.message_id
        return

    if data == 'stats':
        """
        SELECT date_trunc('day', created_at) AS "Дата входа", COUNT(*) AS "Количество"
            FROM user_tb
        GROUP BY created_at;
        """
        cases.del_msg(log, bot, tid, mid)
        data, stat = cases.db.get("date_trunc('day', created_at), COUNT(*)", 'user_tb', 'GROUP BY created_at')
        if stat != 'ok':
            log.error(f'stat:{stat} data:{data}')
            cases.send_msg(log, bot, dev, cases.DBERR, cases.get_kb(log, cases.DEFALTKB))
            return
        # df = pd.DataFrame(list(data.values()), columns=["Дата входа", "Количество"])
        # cases.send_msg(log, bot, tid, df.to_string(index=False), rmvKb())
        # table = PrettyTable(["Дата входа", "Кол-во"])
        # for row in data.values():
        #     table.add_row([row[0][:10], row[1]])
        # table = Texttable()
        # table.add_rows([["Дата входа", "Кол-во"], *list(data.values())])
        stats = []
        for row in data.values():
            stats.append([row[0][:10], row[1]])
        table = tabulate(stats, headers=["Дата входа", "N"])
        cases.send_msg(log, bot, tid, table, rmvKb())
        return
    
    if data in list(cases.CLOTHES.values())[:-1]:
        if is_state_valid(log, bot, tid):
            cases.del_msg(log, bot, tid, mid)
            msg = cases.send_msg(log, bot, tid, cases.txt1, cases.get_ikb(log, cases.QUES_1))
            cases.states[tid].type = data
            cases.states[tid].last_mid = msg.message_id
        return
        
    if not is_state_valid(log, bot, tid):
        cases.del_msg(log, bot, tid, mid)
        return

    if cases.Q1 in data:
        cases.del_msg(log, bot, tid, cases.states[tid].last_mid)
        cases.states[tid].res1 = -1
        cases.states[tid].skipped += 1
        msg = cases.send_msg(log, bot, tid, cases.txt2, cases.get_ikb(log, cases.QUES2))
        cases.states[tid].last_mid = msg.message_id
        return
        

    if cases.Q2 in data:
        cases.del_msg(log, bot, tid, cases.states[tid].last_mid)
        cases.states[tid].res2 = -1
        cases.states[tid].skipped += 1
        msg = cases.send_msg(log, bot, tid, cases.txt3, cases.get_ikb(log, cases.QUES3))
        cases.states[tid].last_mid = msg.message_id
        return
        
        

    if cases.Q3 in data:
        cases.del_msg(log, bot, tid, cases.states[tid].last_mid)
        data = data.split(cases.Q3)
        
        if data[0] != 'skip':
            value = int(data[0])
            cases.states[tid].res3 = value
            msg = cases.send_msg(log, bot, tid, cases.txt4, cases.get_ikb(log, cases.QUES4))
        else:
            cases.states[tid].skipped+=1
            if cases.states[tid].skipped >= 3:
                msg = cases.send_msg(log, bot, tid, cases.MISSERR)
            else:
                cases.states[tid].res3 = -1
                msg = cases.send_msg(log, bot, tid, cases.txt4, cases.get_ikb(log, cases.QUES4))
        cases.states[tid].last_mid = msg.message_id
        return
            
    

    if cases.Q4 in data:
        cases.del_msg(log, bot, tid, cases.states[tid].last_mid)
        data = data.split(cases.Q4)
        if data[0] != 'skip':
            value = int(data[0])
            cases.states[tid].res4 = value
            msg = cases.send_msg(log, bot, tid, cases.txt5, cases.get_ikb(log, cases.QUES5))
        else:
            cases.states[tid].skipped+=1
            if cases.states[tid].skipped >= 3:
                msg = cases.send_msg(log, bot, tid, cases.MISSERR)
            else:
                cases.states[tid].res4 = -1
                cases.states[tid].skipped +=1
                msg = cases.send_msg(log, bot, tid, cases.txt5, cases.get_ikb(log, cases.QUES5))
        cases.states[tid].last_mid = msg.message_id
        return
              

    if cases.Q5 in data:
        cases.del_msg(log, bot, tid, cases.states[tid].last_mid)
        data = data.split(cases.Q5)
        if data[0] != 'skip':
            value = int(data[0])
            cases.states[tid].res5 = value
            msg = cases.send_msg(log, bot, tid, cases.txt6, cases.get_ikb(log, cases.QUES6))
        else:
            cases.states[tid].skipped+=1
            if cases.states[tid].skipped >= 3:
                msg = cases.send_msg(log, bot, tid, cases.MISSERR)
            else:
                cases.states[tid].res5 = -1
                cases.states[tid].skipped += 1
                msg = cases.send_msg(log, bot, tid, cases.txt6, cases.get_ikb(log, cases.QUES6))
        cases.states[tid].last_mid = msg.message_id
        return
         

    if cases.Q6 in data:
        cases.del_msg(log, bot, tid, cases.states[tid].last_mid)
        data = data.split(cases.Q6)
        if data[0] != 'skip':
            value = int(data[0])
            cases.states[tid].res6 = value
            msg = cases.send_msg(log, bot, tid, cases.txt7, cases.get_ikb(log, cases.QUES7))
        else:
            cases.states[tid].skipped+=1
            if cases.states[tid].skipped >= 3:
                msg = cases.send_msg(log, bot, tid, cases.MISSERR)
            else:
                cases.states[tid].res6 = -1
                cases.states[tid].skipped += 1
                msg = cases.send_msg(log, bot, tid, cases.txt7, cases.get_ikb(log, cases.QUES7))
        cases.states[tid].last_mid = msg.message_id
        return
         

    if cases.Q7 in data:
        cases.del_msg(log, bot, tid, cases.states[tid].last_mid)
        data = data.split(cases.Q7)
        if data[0] != 'skip':
            value = int(data[0])
            cases.states[tid].res7 = value
        else:
            cases.states[tid].skipped+=1
            
            if cases.states[tid].skipped >= 3:
                msg = cases.send_msg(log, bot, tid, cases.MISSERR)
                return
            cases.states[tid].res7 = -1 
            cases.states[tid].skipped += 1
        cases.states[tid].close(log, bot, tid)
        msg = cases.send_msg(log, bot, 281321076, f"Новый опрос: {cases.states[tid]}", cases.get_ikb(log, {'Ответить': f'{tid}{REPLY}'}))
        cases.states[tid].last_mid = msg.message_id
        return


if __name__ == "__main__":
    try:
        log.info(f'Token:{token}')
        log.info(f'Admins:{admins}')
        log.info('Starting...')
        bot.polling(allowed_updates="chat_member")
    except Exception as err:
        log.error(err)







