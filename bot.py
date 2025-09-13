import os
import random
from telegram.ext import Updater, MessageHandler, Filters

# Берем токен из переменной окружения
TOKEN = os.environ.get("BOT_TOKEN")

def handle_message(update, context):
    # Случайная вероятность ответа (например, 30%)
    chance = 100  
    if random.randint(1, 100) <= chance:
        user_text = update.message.text
        update.message.reply_text(f"Ты сказал: {user_text}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
