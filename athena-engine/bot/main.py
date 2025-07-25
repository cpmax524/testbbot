import telegram
from telegram.ext import Updater, CommandHandler
from decouple import config
from . import handlers

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')

def main():
    """
    Runs the bot.
    """
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", handlers.start))
    dp.add_handler(CommandHandler("add_token", handlers.add_token))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
