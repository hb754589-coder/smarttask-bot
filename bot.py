import os
import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to SmartTask Bot!\n\n"
        "SmartTask Bot is online.\n"
        "📋 Tasks\n"
        "💰 Balance\n"
        "👥 Refer & Earn"
    )


def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not configured.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("SmartTask Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()# smarttask-bot
