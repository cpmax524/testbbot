from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    """
    Sends a welcome message when the /start command is issued.
    """
    update.message.reply_text('Welcome to the Athena Bot!')

def add_token(update: Update, context: CallbackContext):
    """
    Adds a token to the user's watchlist.
    """
    # This is a placeholder. In a real application, you would add the token
    # to the user's watchlist in the database.
    token_symbol = context.args[0]
    update.message.reply_text(f'Added {token_symbol} to your watchlist!')
