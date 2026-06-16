import os
import telebot
from flask import Flask, request

# TOKEN değişkenini Render'daki Environment Variables kısmından çekiyoruz
TOKEN = os.environ.get('API_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Atlas_Core_Al botu için webhook rotası
@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

if __name__ == "__main__":
    # Önceki webhook'u temizle ve yenisini kur
    bot.remove_webhook()
    bot.set_webhook(url='https://atlas-core-ai.onrender.com/' + TOKEN)
    
    # Sunucuyu başlat
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
