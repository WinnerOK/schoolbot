import os
env = os.environ
token = env['TELEGRAM_BOT_TOKEN']
group_id = -177688323
sql_url = env['MYSQL_SERVICE_HOST']
sql_log = env['MYSQL_USER']  # login
sql_pass = env['MYSQL_PASSWORD']  # pass
sql_db = env['MYSQL_DATABASE']

other_sql_url = env['OTHER_MYSQL_SERVICE_HOST']
other_sql_log = env['OTHER_MYSQL_USER']  # login
other_sql_pass = env['OTHER_MYSQL_PASSWORD']  # pass
other_sql_db = env['OTHER_MYSQL_DATABASE']

main_adm = 182092910
admins = []  #    322526018 - Ирина Анатольевна
rings = "Урок                Перемена\n" \
        "1) 8:05-8:45         10 минут\n" \
        "2) 8:55-9:35         20 минут\n" \
        "3) 9:55-10:35       5  минут\n" \
        "4) 10:40-11:20     20 минут\n" \
        "5) 11:40-12:20     10 минут\n" \
        "6) 12:30-13:10     5 минут\n" \
        "7) 13:15-13:55     5 минут\n" \
        "8) 14:00-14:40"
start = "\U0001F530 Привет, {0} \U0001F530\n" \
       "Я тебе расскажу, что я умею:\n" \
       "\U00002B50 Отправлять тебе сообщение с рассписанием твоего класса или расписанием звонков <b>[</b>/rasp<b>]</b>\n\n\n" \
       "\U0001F393 Чтобы указать свою группу используй команду <b>[</b>/group<b>]</b>\n" \
       "\U0001F30F Чтобы связаться с разработчиком отправь команду (/fb <b>[текст]</b>)\n" \
        "\n" \
        "\U0001F50AИнформацию о появлении расписания и не только можно будет найти на канале @school134_info"
