import telebot
import requests

# Initialize your bot with your API token
bot = telebot.TeleBot("6353748543:AAFzBdhiCDFVpqHyL5xVK9pb0KDdAkLZaLc")

# Define a function to handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Music Bot! Send me a command like /get_music to get started.")

# Define a function to handle the /get_music command
@bot.message_handler(commands=['get_music'])
def send_music(message):
    # URL of the website where the music is hosted
    music_url ="https://youtu.be/KSd3bvpH_i0?si=Vd3JIUaLJ_NGn88s"
    
    # Fetch the music file
    response = requests.get(music_url)
    
    if response.status_code == 200:
        # Send the music file to the user
        bot.send_audio(message.chat.id, response.content)
    else:
        bot.reply_to(message, "Sorry, couldn't fetch the music at the moment.")

# Polling to keep the bot running
bot.polling()