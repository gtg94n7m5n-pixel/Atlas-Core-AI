# Bot nesnesini tanımla
TOKEN = '8363347066:AAGITFGdi2C01-UECPzqG0uQyPTGxoN4_hA'
bot = telebot.TeleBot(TOKEN)

# Webhook'u buraya zorla (linkini düzelttik)
webhook_url = 'https://atlas-core-ai.onrender.com/' + TOKEN
bot.remove_webhook()
bot.set_webhook(url=webhook_url)
