import os
import sys
import traceback

import mysql.connector
import telebot

import datetime

bot = telebot.TeleBot('167826419:AAGSp1AEFUtJsni5hAqXswB6hUCu0pIcJss')

# в 4 часа ставить
try:
    day = datetime.datetime.now().isoweekday()
    dic = {1: 'mon', 2: 'tue', 3: 'wed', 4: 'thu', 5: 'fri', 6: 'sat', 7: 'mon', 8: 'mon'}
    conn = mysql.connector.connect(host='localhost',
                                   database='winnerok',
                                   user='root',
                                   password='1D2a3n4i5i6l',
                                   get_warnings=True,
                                   use_unicode=True)
    cursor = conn.cursor()
    cursor.execute("UPDATE switch SET data='{day}' WHERE field='today'".format(day=dic[day + 1]))
    conn.commit()
    cursor.close()
    conn.close()
except Exception:
    traceback.print_exc()
    ei = "".join(traceback.format_exception(*sys.exc_info()))
    bot.send_message(182092910, 'task: today.py\n' + ei)
