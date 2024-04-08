import telebot

# Телеграм бот объектини инициализациялау
bot = telebot.TeleBot("6931462175:AAFLw1D5ObmU9WQlIXfestQkgFKY4ITNf8c")

# /start командасини қабул қилиш функцияси
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Салем! Visual Studio Code магазинига хуш келибсиз. Маҳсулотлар рўйхатини кўрмоқ учун /products командасини киритинг.")

# /products командасини қабул қилиш функцияси
@bot.message_handler(commands=['products'])
def send_products(message):
    product_list = "Маҳсулотлар:\n"
    product_list += "1. Visual Studio Code\n"
    product_list += "2. Visual Studio Code extensions\n"
    product_list += "3. Visual Studio Code themes\n"
    bot.send_message(message.chat.id, product_list)

# Телеграм ботни ишга туширамиз
bot.polling()