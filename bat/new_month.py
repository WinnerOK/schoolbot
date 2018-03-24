import os
import sys
import traceback

import mysql.connector
import telebot

bot = telebot.TeleBot('167826419:AAGSp1AEFUtJsni5hAqXswB6hUCu0pIcJss')

try:
    conn = mysql.connector.connect(host='localhost',
                                   database='winnerok',
                                   user='root',
                                   password='1D2a3n4i5i6l',
                                   get_warnings=True,
                                   use_unicode=True)
    cursor = conn.cursor()
    cursor.execute("SET @t = (SELECT `data` FROM `switch` WHERE `field` = 'month_this'), "
                   "@n =(SELECT `data` FROM `switch` WHERE `field` = 'month_next');"
                   "UPDATE `switch` SET `data` = @t WHERE `field` = 'month_past';"
                   "UPDATE `switch` SET `data` = @n WHERE `field` = 'month_this';"
                   "UPDATE `switch` SET `data` = NULL WHERE `field` = 'month_next';", multi=True)
    conn.commit()
    bot.send_message(182092910, "Новая фотография установлена в базу")
except Exception:
    traceback.print_exc()
    ei = "".join(traceback.format_exception(*sys.exc_info()))
    bot.send_message(182092910, 'task: new_month.py\n' + ei)
