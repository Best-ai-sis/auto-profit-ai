import telebot
import os
from flask import Flask, request

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я работаю!")

# Обработка слов "привет" и "hi"
@bot.message_handler(func=lambda message: message.text.lower() in ["привет", "hi"])
def reply_to_greeting(message):
    bot.reply_to(message, "Привет! Чем могу помочь?")

# Webhook
@app.route('/', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "ok", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    bot.remove_webhook()
    bot.set_webhook(url=os.environ.get("WEBHOOK_URL"))
    app.run(host="0.0.0.0", port=port)
