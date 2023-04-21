import os
import xlsxwriter

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.router import Router
from aiogram.types import CallbackQuery, Message, FSInputFile
from resources import messages as mes
from sqlalchemy.ext.asyncio import AsyncSession
from utils import config

from bot.keyboards.inline import new_kb, subscribe
from bot.fsm_states_groups import FilterCreateForm
from utils.callback_data import CallbackData
from db import NextsRepository, LastMonthsRepository
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import License, Workbook, PdfSaveOptions, GridlineType
from asposecells.api import Workbook, SaveFormat, PdfSaveOptions



async def excel_report(season,
                       avr_check,
                       max_check,
                       max_count,
                       min_redemption,
                       proc_sale,
                       proc_missrvenue,
                       proc_turnover,
                       q,
                       db_session,
                       state,
                       is_message=False):

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

    if season == 1:
        next_repo = NextsRepository(db_session)
        filt = await next_repo.get_many()
    elif season == 0:
        last_repo = LastMonthsRepository(db_session)
        filt = await last_repo.get_many()
    else:
        last_repo = LastMonthsRepository(db_session)
        filt = await last_repo.get_many()
    state = await state.get_data()
    print(state)
    for f in filt:
        
        if state["clothes"]=="all":
            pass
        elif state["clothes"]=="clothes":
           is_key = False
         
           if "одежда" not in f.goods.lower() and "белье" not in f.goods.lower() and "бельё" not in f.goods.lower():
               continue
           if state.get("clothes_type")=="all_clothes":
               pass
           elif  state.get("clothes_type"):
               keywords=config.keywords[state.get("clothes_type")]
               for key in keywords:
                   
                   if key.lower()  in f.goods.lower():
                       print(key,f.goods.lower())
                       is_key=True
                     
                       break
                       
               
               if not is_key:
                   continue
        
        elif state["clothes"]=="items":
            
            if "товары" not in f.goods.lower() :
               continue
        
        min_avr_price = 0
        avr_price = 0
        try:
            if f.avr_price >= int(avr_check):
                min_avr_price = f.avr_price
        except:
            min_avr_price = f.avr_price
        try:
            if min_avr_price <= int(max_check):
                avr_price = min_avr_price
        except:
            avr_price = min_avr_price
        count_sku = 0
        try:
            if f.count_sku <= int(max_count):
                count_sku = f.count_sku
        except:
            count_sku = f.count_sku
        percent_repurch_orders = 0.00
        try:
            if f.percent_repurch_orders*100 >= float(min_redemption):
                percent_repurch_orders = f.percent_repurch_orders*100
        except:
            percent_repurch_orders = f.percent_repurch_orders*100       
        percent_sku_sale = 0.00
        try:
            if f.percent_sku_sale*100 >= float(proc_sale):
                percent_sku_sale = f.percent_sku_sale*100
        except:
            percent_sku_sale = f.percent_sku_sale*100
        percent_lost_revenue = 0
        try:
            if f.percent_lost_revenue >= int(proc_missrvenue):
                percent_lost_revenue = f.percent_lost_revenue
        except:
            percent_lost_revenue = f.percent_lost_revenue  
        turnover = 0.00
        try:
            if f.turnover*100 >= float(proc_turnover):
                turnover = f.turnover
        except:
            turnover = f.turnover
        if avr_price !=0 and count_sku!=0 and percent_repurch_orders !=0 and percent_sku_sale != 0 and percent_lost_revenue !=0 and turnover !=0:
            
            my_list.append([
                f.goods,
                count_sku,
                f.count_sku_sale,
                percent_sku_sale/100,
                f.count_sellers,
                f.sellers_sell,
                f.percent_sellers_sell,
                percent_repurch_orders/100,
                int(float(f.revenuy_excluding_repurch)),
                int(float(f.revenuy_including_repurch)),
                int(float(f.potencial_revenue)),
                int(float(f.lost_revenue)),
                percent_lost_revenue/100,
                turnover,
                int(float(f.avr_revenue)),
                avr_price,
                f.rank
            ])
    
    workbook = xlsxwriter.Workbook("gilsell_bot.xlsx")
    worksheet = workbook.add_worksheet()
    my_list = my_list[:101]
    for row_num, row_data in enumerate(my_list):
        for col_num, col_data in enumerate(row_data):
            worksheet.write(row_num, col_num, col_data)

    header = workbook.add_format({'bold': True})
    header.set_align('center')
    header.set_align('vcenter')
    header.set_text_wrap()
    header.set_font_size(9)    
    worksheet.set_column(0, 0, 30)
    worksheet.set_row(0, 80, header)
    proc_format = workbook.add_format({'num_format': '0%'})
    currency_format = workbook.add_format({'num_format': '# ##0'})
    worksheet.set_column('D:D', None, proc_format)
    worksheet.set_column('G:H', None, proc_format)
    worksheet.set_column('M:N', None, proc_format)
    worksheet.conditional_format('C2:C101', {'type': '3_color_scale',
                                        'min_color': "#F8636B",
                                        'mid_color': "#FFEB84",
                                        'max_color': "#63BE7B"})
    worksheet.conditional_format('D2:D101', {'type': '3_color_scale',
                                        'min_color': "#F8636B",
                                        'mid_color': "#FFEB84",
                                        'max_color': "#63BE7B"})
    worksheet.conditional_format('F2:F101', {'type': '3_color_scale',
                                        'min_color': "#F8636B",
                                        'mid_color': "#FFEB84",
                                        'max_color': "#63BE7B"})
    worksheet.conditional_format('H2:H101', {'type': '3_color_scale',
                                        'min_color': "#F8636B",
                                        'mid_color': "#FFEB84",
                                        'max_color': "#63BE7B"})
    worksheet.conditional_format('J2:J101', {'type': '3_color_scale',
                                        'min_color': "#F8636B",
                                        'mid_color': "#FFEB84",
                                        'max_color': "#63BE7B"})
    worksheet.conditional_format('M2:M101', {'type': '3_color_scale',
                                        'min_color': "#F8636B",
                                        'mid_color': "#FFEB84",
                                        'max_color': "#63BE7B"})
    worksheet.conditional_format('O2:O101', {'type': '3_color_scale',
                                        'min_color': "#F8636B",
                                        'mid_color': "#FFEB84",
                                        'max_color': "#63BE7B"})
    worksheet.set_column('I:L', 14, currency_format)
    worksheet.set_column('O:P', 12, currency_format)
    format_turn = workbook.add_format({'bg_color': '#e6e6c9'})
    worksheet.conditional_format('N2:N101', {'type':     'cell',
                                            'criteria': '>=',
                                            'value':    1,
                                            'format':   format_turn})
    workbook.close()
    saveOptions = PdfSaveOptions()
    saveOptions.setGridlineType(GridlineType.HAIR)
    saveOptions.setAllColumnsInOnePagePerSheet(True)
    pdf_book = Workbook("gilsell_bot.xlsx")
    worksheets = pdf_book.getWorksheets()
    worksheet = worksheets.get(0)
    worksheet.getPageSetup().setPrintGridlines(True)
    worksheet.autoFitColumns()
    
    pdf_book.save("gilsell_bot.pdf", saveOptions)
    
    if not is_message:
        await q.message.answer_document(FSInputFile(workbook.filename, "gilsell_bot.xlsx"))
        await q.message.answer_document(FSInputFile("gilsell_bot.pdf", "gilsell_bot.pdf"))
    else:
        await q.answer_document(FSInputFile(workbook.filename, "gilsell_bot.xlsx"))
        await q.answer_document(FSInputFile("gilsell_bot.pdf", "gilsell_bot.pdf"))
    
    os.remove(workbook.filename)