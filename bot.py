import telebot
from flask import Flask, request
import os

TOKEN = '8363347066:AAGITFGdi2C01-UECPzqG0uQyPTGxoN4_hA'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

@app.route('/')
def index():
    return 'Bot is running!'

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url='https://atlas-core-ai.onrender.com/' + TOKEN)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
