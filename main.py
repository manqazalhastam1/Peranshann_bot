import os
import telebot
from telebot import types

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    settings_btn = types.KeyboardButton("تنظیمات")
    markup.add(settings_btn)
    bot.send_message(message.chat.id, "سلام! به ربات پرنشان خوش اومدی!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "تنظیمات")
def show_settings(message):
    bot.reply_to(message, "دو ستاره داریم که خار چشمتونه...
ما فینالایی دیدیم که توی رویاتونه...")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, "عکست دریافت شد. کارتونی شدنش فعلاً فعال نیست.")

bot.infinity_polling()