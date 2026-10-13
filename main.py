import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalam o Alaikum! 🇦🇪\n\n"
        "Main DubaiBot hoon!\n\n"
        "Commands:\n"
        "/visa - Dubai Visa Info\n"
        "/jobs - Dubai Jobs Info\n"
        "/help - Madad"
    )

async def visa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🇦🇪 Dubai Visa Info:\n\n"
        "1. Visit Visa - 30/60 din\n"
        "2. Work Visa - Company degi\n"
        "3. Documents - Passport, Photo, Ticket\n\n"
        "Mazeed maloomat ke liye /help"
    )

async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💼 Dubai Jobs:\n\n"
        "CV tayar rakho, Indeed, LinkedIn par apply karo.\n"
        "Kisi ko paisa na do!"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kisi bhi sawal ke liye /start dabao.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("visa", visa))
    app.add_handler(CommandHandler("jobs", jobs))
    app.add_handler(CommandHandler("help", help_cmd))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
