import os
import threading
from flask import Flask
from telegram.ext import Application, CommandHandler

# Dummy Web Server (Render ke port error ko fix karne ke liye)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Alive!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# Web server ko background thread mein start karna
threading.Thread(target=run_web, daemon=True).start()

# Telegram Bot Functions
async def start(update, context):
    await update.message.reply_text("Hello! Welcome to Earn Cash Bot. Bot is fully online!")

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("BOT_TOKEN missing!")
        return

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    
    print("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
    
        
