import telebot

# Телеграм бот объектини инициализациялау
bot = telebot.TeleBot("6931462175:AAFLw1D5ObmU9WQlIXfestQkgFKY4ITNf8c")

# Касса суммасни сақлаш учун перемент
total_sales = 0

# /start командасини қабул қилиш функцияси
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Салем! Visual Studio Code магазинига хуш келибсиз. Маҳсулотлар рўйхатини кўрмоқ учун /products киритинг.")
# /products командасини қабул қилиш функцияси
@bot.message_handler(commands=['products'])
def send_products(message):
    product_list = "Маҳсулотлар:\n"
    product_list += "11. Visual Studio Code - $50\n"
    product_list += "22. Visual Studio Code extensions - $10\n"
    product_list += "33. Visual Studio Code themes - $5\n"
    bot.send_message(message.chat.id, product_list)
    bot.reply_to(message, "Салем! Visual Studio Code магазинига хуш келибсиз. Маҳсулотлар рўйхатини кўрмоқ учун /buy киритинг.")

# /buy командасини қабул қилиш функцияси
@bot.message_handler(commands=['buy'])
def buy_product(message):
    global total_sales
    bot.reply_to(message, "Маҳсулот ID-сини киритинг:")
    bot.register_next_step_handler(message, process_product_id)

# Маҳсулот ID-сини қабул қилиш функцияси
def process_product_id(message):
    product_id = int(message.text)
    if product_id in [11, 22, 33]:
        product_prices = {11: 50, 22: 10, 33: 5} 
        product_prices [product_id] += total_sales
        bot.send_message(message.chat.id, f"Маҳсулот сотиб олинди. Жами касса суммаси: ${total_sales}")
    else:
        bot.send_message(message.chat.id, "Нотўғри маҳсулот ID-си. Илтимос, қайтадан киритинг.")

# Телеграм ботни ишга туширамиз
bot.polling()