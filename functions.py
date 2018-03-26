import traceback

import mysql.connector
import requests
import telebot

import constants

bot = telebot.TeleBot(constants.token)


def start_sql():
    conn = mysql.connector.connect(host=constants.sql_url,
                                   database=constants.sql_db,
                                   user=constants.sql_log,
                                   password=constants.sql_pass,
                                   get_warnings=True,
                                   use_unicode=True)
    if conn.is_connected():
        return conn
    else:
        bot.send_message(constants.main_adm, "Can't create SQL connect")


def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def schedule_inline_keyboard(day, klass):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        ('Понедельник', 'mon'),
        ('Вторник', 'tue'),
        ('Среда', 'wed'),
        ('Четверг', 'thu'),
        ('Пятница', 'fri'),
        ('Суббота', 'sat'),
        ('Звонки', 'rings')
    ]

    if day == 'full':
        buttons = [telebot.types.InlineKeyboardButton(text=localized_name, callback_data='s_' + short_name + '_' + klass) for localized_name, short_name in buttons]
    else:
        buttons = [telebot.types.InlineKeyboardButton(text=localized_name, callback_data='s_' + short_name + '_' + klass) for localized_name, short_name in buttons if
                   day != short_name]
    keyboard.add(*buttons)
    return keyboard


def admincheck(message):
    if (str(message.from_user.id) in constants.admins) or (message.from_user.id == constants.main_adm):
        if message.chat.type == "private":
            return True
        else:
            bot.reply_to(message, "Команды администратора доступны только в диалоге.\nНапишите мне в ЛС @school134_bot")
            return False
    else:
        bot.reply_to(message, "Вы не администратор")
        return False


def isprivate(message):
    if message.chat.type == "private":
        return True
    else:
        bot.reply_to(message, "Эта команда доступна лишь в диалоге.\nНапишите мне @school134_bot")
        return False


def select_next_step(message):
    conn = start_sql()
    cursor = conn.cursor()
    cursor.execute("SELECT next_step FROM known_users WHERE id={u_ud}".format(u_ud=message.from_user.id))
    return cursor.fetchone()[0]


def set_next_step(data, u_id):
    try:
        if str(type(data)) == "<class 'str'>":
            if data.lower() != 'null':
                data = '"' + data + '"'
        conn = start_sql()
        cursor = conn.cursor()
        cursor.execute("UPDATE known_users SET next_step = {data} WHERE id={u_id}".format(data=str(data), u_id=str(u_id)))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as err:
        traceback.print_exc()
        bot.send_message(constants.main_adm, "set_next_step: " + str(data) + ' ' + str(u_id) + '\n' + str(err))


def isknown(msg, group_a=None):
    conn = start_sql()
    cursor = conn.cursor()
    cursor.execute("SELECT id, klass FROM known_users WHERE id = {0}".format(msg.from_user.id))
    cb = cursor.fetchone()
    if cb is None:
        insert = "INSERT INTO known_users (id, klass) VALUES (%s, %s)"
        insert_args = (msg.from_user.id, group_a)
        cursor.execute(insert, insert_args)
    else:
        if (group_a is not None) and (cb[1] is None):
            cursor.execute("UPDATE known_users set klass='{group}' WHERE id = {uid}".format(group=group_a, uid=msg.from_user.id))
    conn.commit()
    cursor.close()
    conn.close()

'''
def send_photo_vk(schedule, day, group):
    try:

        api = vk.API(vk.Session(), v=5.63)
        server = api.photos.getUploadServer(access_token=constants.vk_user_token, album_id=243676213, group_id=129500328)
        response = json.loads(requests.post(server['upload_url'], files={'file1': open(photo,'rb')}).text)
        upload = api.photos.save(access_token=constants.vk_user_token, album_id=243676213, group_id=129500328,
                                 server=response["server"], photos_list=response["photos_list"], hash=response["hash"])[0]
        requests.post(constants.vk_bot_server, json={"id": "photo{0}_{1}".format(upload["owner_id"], upload["id"]),
                                                     "day": day, "group": group})

        # response = requests.post(constants.vk_bot_server, json={"schedule": schedule, "day": day, "group": group})
    except Exception as err:
        traceback.print_exc()
        bot.send_message(constants.main_adm, "vk upload: \n" + str(response) + '\n\n' + str(err))



def vote(call, choose):
    conn = start_sql()
    cursor = conn.cursor()
    query = "UPDATE  known_users SET vote = '{0}' WHERE id = {1}".format(choose, call.from_user.id)
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ваш голос учтен")
'''
