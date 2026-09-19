import os
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Token and Web App URL setup
TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
WEB_APP_URL = "https://riyajn478-dev.github.io/earn-cash-bot/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Chat Keyboard Buttons
    keyboard = [
        ['📅 Daily Check-in', '🌀 Spin & Win'],
        ['🧮 Math Quiz', '🧩 Captcha Task'],
        ['📺 Watch Ads', '💰 Withdraw']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "✨ Welcome to Earn Cash Bot!\n\nSelect an option below to start earning:",
        reply_markup=reply_markup
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if 'Daily Check-in' in text:
        await update.message.reply_text("✅ **Daily Check-in Successful!**\n\nAapko +10 Coins mil gaye hain! Kal fir aana.")

    elif 'Spin & Win' in text:
        # Spin Button opens the Web Mini App
        inline_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🌀 Open Spin & Win App", web_app=WebAppInfo(url=WEB_APP_URL))]
        ])
        await update.message.reply_text("Below button par click karke Spin Wheel kholo:", reply_markup=inline_keyboard)

    elif 'Math Quiz' in text:
        await update.message.reply_text("🧮 **Math Quiz Task**\n\nSolve: **15 + 25 = ?**\n\nSahi answer message me type karke bhejo!")

    elif 'Captcha Task' in text:
        await update.message.reply_text("🧩 **Captcha Task**\n\nType this code to earn coins: **`EARN2026`**")

    elif 'Watch Ads' in text:
        await update.message.reply_text("📺 **Watch Ads**\n\nIs feature par kaam chal raha hai, jald hi update aayega!")

    elif 'Withdraw' in text:
        await update.message.reply_text("💰 **Withdraw Coins**\n\nAapka balance low hai. Minimum withdrawal: **1000 Coins**.")

    else:
        await update.message.reply_text("Kripya niche diye gaye keyboard buttons me se select karein.")

def main():
    if not TOKEN or TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("Error: BOT_TOKEN Environment Variable set nahi hai!")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    # Handlers Setup
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))

    print("Bot starting...")
    app.run_polling()

if __name__ == '__main__':
    main()
            
