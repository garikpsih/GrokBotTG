import os
import random
from telegram.ext import Updater, MessageHandler, Filters

# Берем токен из переменной окружения
TOKEN = os.environ.get("BOT_TOKEN")

def handle_message(update, context):
    # Случайная вероятность ответа (например, 30%)
    import os
import random
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")
response_chance = 30  # начальный шанс ответа в процентах

def handle_message(update, context):
    global response_chance
    if random.randint(1, 100) <= response_chance:
        user_text = update.message.text
        update.message.reply_text(f"Ты сказал: {user_text}")

def set_chance(update, context):
    global response_chance
    try:
        new_chance = int(context.args[0])
        if 0 <= new_chance <= 100:
            response_chance = new_chance
            update.message.reply_text(f"Шанс ответа установлен на {response_chance}%")
        else:
            update.message.reply_text("Введите число от 0 до 100")
    except:
        update.message.reply_text("Используй: /setchance <число от 0 до 100>")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dp.add_handler(CommandHandler("setchance", set_chance))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()  
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
