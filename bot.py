import telebot
from telebot import types

TOKEN = "BU_YERGA_TOKENINGIZNI_YOZING"

bot = telebot.TeleBot("8246336989:AAGB38DVYI7kxmmzbTcDlE67o4GMHQrsTyE")

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
    bot.send_message(message.chat.id,
                     "Mavjud mahsulotlar:\n\n"
                     "1️⃣ ANDELI 1 kVA\n"
                     "2️⃣ ANDELI 2 kVA\n"
                     "3️⃣ ANDELI 3 kVA\n\n"
                     "Buyurtma uchun yozing yoki qo'ng'iroq qiling.")

@bot.message_handler(func=lambda message: message.text == "📞 Aloqa")
def contact(message):
    bot.send_message(message.chat.id,
                     "📲 Tel: +998901234567\n"
                     "✈️ Telegram: @username")

bot.polling()
