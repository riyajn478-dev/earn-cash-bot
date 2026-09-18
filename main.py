from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8472292124:AAE2YWPA1mLeWGySi4lxy5WJYuZqBUSL4mE"
WEB_APP_URL = "https://riyajn478-dev.github.io/earn-cash-bot/"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    web_app = WebAppInfo(url=WEB_APP_URL)
    
    keyboard = [
        [
            InlineKeyboardButton("📅 Daily Check-in", web_app=web_app),
            InlineKeyboardButton("🌀 Spin & Win", web_app=web_app)
        ],
        [
            InlineKeyboardButton("🧮 Math Quiz", web_app=web_app),
            InlineKeyboardButton("🧩 Captcha Task", web_app=web_app)
        ],
        [
            InlineKeyboardButton("📺 Watch Ads", web_app=web_app),
            InlineKeyboardButton("💰 Withdraw", web_app=web_app)
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "✨ **Welcome to Earn Cash Bot!**\n\nSelect an option below to start earning:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    print("Bot is starting...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
