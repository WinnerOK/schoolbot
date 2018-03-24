import telebot
import botan

bot = telebot.TeleBot('530489919:AAEf1UYbWmbmb7XD30IFL7nunGhU_tcNyog')
botan_key = "6bbff37b-1910-4d5e-b0cc-7ee7ea093a48"

@bot.message_handler(func=lambda x:True)
def hi(msg):
    print(botan.track(botan_key, msg.from_user.id, msg, "test"))
    bot.reply_to(msg, "proceed")


if __name__ == '__main__':
    bot.polling()
