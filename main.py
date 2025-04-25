from telegram.ext import Application, CommandHandler
from bot_config import API_TOKEN

async def start(update, context):
    await update.message.reply_text("Бот активен!")

def main():
    app = Application.builder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
