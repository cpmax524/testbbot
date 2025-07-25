import os
from telegram.ext import ApplicationBuilder, CommandHandler
from .handlers import start, score

def main():
    # Get the Telegram bot token from the environment variables.
    token = os.environ.get("TELEGRAM_BOT_TOKEN")

    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("score", score))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
