
import telebot
from telebot import types

TOKEN = "8246336989:AAGB38DVYI7kxmmzbTcDlE67o4GMHQrsTyE"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🛍 Mahsulotlar")
    btn2 = types.KeyboardButton("📞 Aloqa")
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, 
                     "Assalomu alaykum!\nStabilizator do'koniga xush kelibsiz 👋", 
                     reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🛍 Mahsulotlar")
def products(message):
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("🔹 ANDELI Laterni")
btn2 = types.KeyboardButton("🔹 Stabil Releli")
btn3 = types.KeyboardButton("🔹 Stabil Laterni")
btn4 = types.KeyboardButton("⬅ Ortga")
markup.add(btn1)
markup.add(btn2)
markup.add(btn3)
markup.add(btn4)
bot.send_message(message.chat.id, 
                     "Kerakli bo‘limni tanlang:", 
                     reply_markup=markup)




@bot.message_handler(func=lambda message: message.text == "📞 Aloqa")
def contact(message):
    bot.send_message(message.chat.id,
                     "📲 Tel: +998901234567\n"
                     "✈️ Telegram: @username")

bot.polling()
