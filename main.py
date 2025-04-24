import telebot
from flask import Flask, request

API_TOKEN = '7729733399:AAGRQH42MQYrl80VdzfCEWXCkafSR4Z8dvA'
bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Бот запущен. Добро пожаловать!")

@app.route('/', methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route('/', methods=['GET'])
def index():
    return "Сервер и бот запущены!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
