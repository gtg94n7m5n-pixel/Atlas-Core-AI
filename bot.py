import telebot
from flask import Flask, request
import os

TOKEN = '8363347066:AAGITFGdi2C01-UECPzqG0uQyPTGxoN4_hA'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Mesajları karşılayan kısım
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return 'OK', 200
    return 'Forbidden', 403

# Render'ın sürekli kontrol ettiği "sağlık" rotası
@app.route('/')
def index():
    return 'Bot aktif durumda.', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
