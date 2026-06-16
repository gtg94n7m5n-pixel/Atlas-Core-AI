import telebot
import os

TOKEN = '8363347066:AAGITFGdi2C01-UECPzqG0uQyPTGxoN4_hA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bot aktif, mesajın ulaştı!")

# Webhook'u devre dışı bırakıp, botun doğrudan Telegram'a bağlanmasını sağla
bot.remove_webhook()
bot.polling(none_stop=True)
