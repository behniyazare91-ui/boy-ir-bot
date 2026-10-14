import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🎵 به Boy.ir خوش آمدی!\nبرای دریافت آهنگ آماده‌ایم."
    )

print("Boy.ir is running!")
bot.infinity_polling()
