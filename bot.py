import os
import telebot

TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Atlas Core AI sistemine hoş geldin. Emlak ve yatırım analizlerine başlamak için hazır.")

bot.polling()
