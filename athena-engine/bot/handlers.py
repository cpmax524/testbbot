from telegram import Update
from telegram.ext import ContextTypes
from tasks.scoring_tasks import calculate_score_for_token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when the command /start is issued."""
    await update.message.reply_text("Welcome to the Athena Bot!")

async def score(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Calculates the Athena Score for a given token.
    """
    # Get the token address from the command arguments.
    try:
        token_address = context.args[0]
    except (IndexError, ValueError):
        await update.message.reply_text("Please provide a token address.")
        return

    # Call the scoring task.
    result = calculate_score_for_token.delay(token_address)

    # Send the result to the user.
    await update.message.reply_text(f"Calculating score for {token_address}...")
    await update.message.reply_text(f"Score: {result.get()}")
