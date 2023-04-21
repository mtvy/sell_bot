import pandas as pd
import json

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
from utils import config
from bot.keyboards.inline import cancel_kb, accept_kb, start_kb
from utils.callback_data import CallbackData
from sqlalchemy import create_engine
from utils import config
from utils.services import users_decorator
from pandas import json_normalize
from bot.fsm_states_groups import FilterCreateForm
from db import UsersRepository


FILE_CD = CallbackData("file", "action", "file_path")

router = Router()
bot = Bot(config.TELEGRAM_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# # настраиваем доступ к Google Sheets и Googli Drive
# scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
# # Подключаем ключи доступа
# creds = ServiceAccountCredentials.from_json_keyfile_name("testpython-353519-60e571fd76e4.json", scope)
# client = gspread.authorize(creds)
# # Указываем имя выгружаемой таблицы и её страницу
# sheet = client.open("test").sheet1
# # В data записываем все записи из таблицы и листа
# data = sheet.get_all_records()
# df = pd.DataFrame.from_dict(data)


@router.callback_query_handler(lambda c: c.data == 'add_data_month')
async def send_manager(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):
    await bot.send_message(
        q.from_user.id,
        text="Вставьте таблицу в формате xlsx:",
        reply_markup=cancel_kb())
    await q.message.delete()
    await state.set_state(FilterCreateForm.add_data_month)


@router.callback_query_handler(lambda c: c.data == 'add_data_next')
async def send_manager(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):
    await bot.send_message(
        q.from_user.id,
        text="Вставьте таблицу в формате xlsx:",
        reply_markup=cancel_kb())
    await q.message.delete()
    await state.set_state(FilterCreateForm.add_data_next)


@router.message(state=FilterCreateForm.add_data_month)
@users_decorator
async def unknown_message(m: Message, state: FSMContext, db_session: AsyncSession):
    # src = f'{m.document.file_name}' # путь до файла
    users_repo = UsersRepository(db_session)
    user = await users_repo.get(telegram_id=m.from_user.id)
    file_id = m.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    period = 'accept_last'
    await m.answer(text='Данные за прошлый месяц загружены', reply_markup=accept_kb(user, period, file_path))


@router.message(state=FilterCreateForm.add_data_next)
@users_decorator
async def unknown_message(m: Message, state: FSMContext, db_session: AsyncSession):
    # src = f'{m.document.file_name}' # путь до файла
    users_repo = UsersRepository(db_session)
    user = await users_repo.get(telegram_id=m.from_user.id)
    file_id = m.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    period = 'add_data_next'
    await m.answer(text='Данные за будущий период загружены', reply_markup=accept_kb(user, period, file_path))


@router.callback_query(FILE_CD.filter(action="accept_last"))
async def job_delivery_method(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):

    callback_data = FILE_CD.parse(q.data)
    await state.update_data(action=callback_data["action"],
                            file_path=str(callback_data["file_path"]))
    
    dt = await state.get_data()

    fpath=dt['file_path']
    file_path = f'https://api.telegram.org/file/bot{config.TELEGRAM_TOKEN}/{fpath}'

    excel_data_df = pd.read_excel(file_path, header=2)
    thisisjson = excel_data_df.to_json(orient='records')

    df_json = json.loads(thisisjson)
    df_request = json_normalize(df_json)
    df = pd.DataFrame()
    df = pd.concat([df, df_request])
    df.rename(columns={'Товар':'goods',
                    'Кол-во SKU':'count_sku',
                    'Кол-во  SKU с движением':'count_sku_mov',
                    'Кол-во  SKU с продажами':'count_sku_sale',
                    '% SKU с продажами (без учета неактивных SKU)':'percent_sku_sale',
                    'Кол-во Sellers':'count_sellers',
                    'Sellers с продажами ':'sellers_sell',
                    '% Sellers с продажами ':'percent_sellers_sell',
                    '% выкупа от заказов':'percent_repurch_orders',
                    'Выручка без учета % выкупов':'revenuy_excluding_repurch',
                    'Выручка с учетом % выкупа':'revenuy_including_repurch',
                    'Потенциальная выручка':'potencial_revenue',
                    'Упущенная выручка ':'lost_revenue',
                    '% упущенной выручки':'percent_lost_revenue',
                    'Заказы без учета выкупов, шт':'order_without_revenue',
                    'Продажи с учетом выкупов, шт':'sales_with_revenue',
                    'Остатки, шт':'remains',
                    'Оборачиваемость ':'turnover',
                    'Средняя выручка с учетом выкупов на 1 товар, руб':'avr_revenue',
                    'Средняя цена за единицу товара. руб':'avr_price',
                    'Себестоимость продаж ':'cost_of_sale',
                    'Комиссия ВБ с учетом выкупов, руб':'commiss_wb_with_repurch',
                    'Налоги ':'taxes',
                    'Прибыль ':'profit',
                    '% Прибыли от выручки ':'percent_profit_revenue',
                    '% Прибыли от себестоимости':'percent_profit_cost_of_sale',
                    '% Прибыли от себестоимости вложений':'percent_profit_cost_of_sale_in',
                    'Комиссия ':'commission',
                    'Среднее кол-во комментариев ':'avr_count_comments',
                    'Средний Рейтинг Оценок':'avr_rates_evalution',
                    'Вес % Прибыли от себестоимости продаж ':'weight_percent_profit_cost_of_sale',
                    ' Вес % Прибыли от себестоимости вложений ':'weight_percent_profit_cost_of_attach',
                    'Вес % Прибыли от выручки ':'weight_percent_profit_revenue',
                    'Вес Выручка ниши с учетом % выкупа ':'weight_revenue',
                    'Вес % SKU с  продажами  ':'weight_percent_sku',
                    'Вес % Sellers с продажами  ':'weight_percent_sellers',
                    'Вес ранга оценок ':'weight_ranks',
                    'Вес кол-ва комментариев ':'weight_count_comments',
                    ' Вес Оборачиваемости':'weight_turnover',
                    'Вес упущенной выручки ':'weight_lost_revenue',
                    'Вес Итоговая сумма рангов ':'weight_total_sum',
                    'Ранг ':'rank'},
                    inplace=True)
    newdf = df.fillna(0)
    sortnewdf = sortnewdf = newdf.sort_values(by='rank')
    print(newdf,df)
    engine = create_engine('mysql+pymysql://myuser:mypass@127.0.0.1:8880/dbwild')
    try:
        pd.read_sql_table("data_last_month", con=engine)
        sortnewdf.to_sql("data_last_month", con=engine, if_exists='replace', index=True)
    except:
        sortnewdf.to_sql("data_last_month", con=engine, if_exists='replace', index=True)

    users_repo = UsersRepository(db_session)
    user = await users_repo.get(telegram_id=q.from_user.id)

    await bot.send_message(
        q.from_user.id,
        text="Данные в базе обновлены",
        reply_markup=start_kb(user))


@router.callback_query(FILE_CD.filter(action="add_data_next"))
async def job_delivery_method(q: CallbackQuery, db_session: AsyncSession, state: FSMContext):
    callback_data = FILE_CD.parse(q.data)
    await state.update_data(action=callback_data["action"],
                            file_path=str(callback_data["file_path"]))
    
    dt = await state.get_data()

    fpath=dt['file_path']
    file_path = f'https://api.telegram.org/file/bot{config.TELEGRAM_TOKEN}/{fpath}'

    excel_data_df = pd.read_excel(file_path, header=2)
    print()
    thisisjson = excel_data_df.to_json(orient='records')

    df_json = json.loads(thisisjson)
    df_request = json_normalize(df_json)
    df = pd.DataFrame()
    
    df = pd.concat([df, df_request])
    print(df)
    df.rename(columns={'Товар':'goods',
                    'Кол-во SKU':'count_sku',
                    'Кол-во  SKU с движением':'count_sku_mov',
                    'Кол-во  SKU с продажами':'count_sku_sale',
                    '% SKU с продажами (без учета неактивных SKU)':'percent_sku_sale',
                    'Кол-во Sellers':'count_sellers',
                    'Sellers с продажами ':'sellers_sell',
                    '% Sellers с продажами ':'percent_sellers_sell',
                    '% выкупа от заказов':'percent_repurch_orders',
                    'Выручка без учета % выкупов':'revenuy_excluding_repurch',
                    'Выручка с учетом % выкупа':'revenuy_including_repurch',
                    'Потенциальная выручка':'potencial_revenue',
                    'Упущенная выручка ':'lost_revenue',
                    '% упущенной выручки':'percent_lost_revenue',
                    'Заказы без учета выкупов, шт':'order_without_revenue',
                    'Продажи с учетом выкупов, шт':'sales_with_revenue',
                    'Остатки, шт':'remains',
                    'Оборачиваемость ':'turnover',
                    'Средняя выручка с учетом выкупов на 1 товар, руб':'avr_revenue',
                    'Средняя цена за единицу товара. руб':'avr_price',
                    'Себестоимость продаж ':'cost_of_sale',
                    'Комиссия ВБ с учетом выкупов, руб':'commiss_wb_with_repurch',
                    'Налоги ':'taxes',
                    'Прибыль ':'profit',
                    '% Прибыли от выручки ':'percent_profit_revenue',
                    '% Прибыли от себестоимости':'percent_profit_cost_of_sale',
                    '% Прибыли от себестоимости вложений':'percent_profit_cost_of_sale_in',
                    'Комиссия ':'commission',
                    'Среднее кол-во комментариев ':'avr_count_comments',
                    'Средний Рейтинг Оценок':'avr_rates_evalution',
                    'Вес % Прибыли от себестоимости продаж ':'weight_percent_profit_cost_of_sale',
                    ' Вес % Прибыли от себестоимости вложений ':'weight_percent_profit_cost_of_attach',
                    'Вес % Прибыли от выручки ':'weight_percent_profit_revenue',
                    'Вес Выручка ниши с учетом % выкупа ':'weight_revenue',
                    'Вес % SKU с  продажами  ':'weight_percent_sku',
                    'Вес % Sellers с продажами  ':'weight_percent_sellers',
                    'Вес ранга оценок ':'weight_ranks',
                    'Вес кол-ва комментариев ':'weight_count_comments',
                    ' Вес Оборачиваемости':'weight_turnover',
                    'Вес упущенной выручки ':'weight_lost_revenue',
                    'Вес Итоговая сумма рангов ':'weight_total_sum',
                    'Ранг ':'rank'},
                    inplace=True)
    newdf = df.fillna(0)
    print(newdf,df)
    sortnewdf = sortnewdf = newdf.sort_values(by='rank')
    engine = create_engine('mysql+pymysql://myuser:mypass@127.0.0.1:8880/dbwild')
    try:
        pd.read_sql_table("data_next", con=engine)
        sql = sortnewdf.to_sql("data_next", con=engine, if_exists='replace', index=True)
    except:
        sql = sortnewdf.to_sql("data_next", con=engine, if_exists='replace', index=True)
    print(sql)
    users_repo = UsersRepository(db_session)
    user = await users_repo.get(telegram_id=q.from_user.id)
    
    await bot.send_message(
        q.from_user.id,
        text="Данные в базе обновлены",
        reply_markup=start_kb(user))
