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
    bot.send_photo(
    message.chat.id,
    open("andeli_1kva.jpg", "rb"),
    caption="""📦 ANDELI 1 kVA (SDW-1000VA)

Model: ANDELI SDW-1000VA
Turi: 1-Faza Laterli
Quvvati: 1000VA (1 kVA)
Kirish: 110V–250V
Chiqish: 220V ±3%

⚖️ Og'irligi: 6 kg
🔩 O‘rnatilishi: Polga va devorga
🛡 Korpus: Metall

💵 Narxi: 40$
🇺🇿 Narxi: 500 000 so‘m

💳 To‘lov usullari:
• Naxt
• Karta
• Perechesleniya + QQS

🚚 O‘zbekiston bo‘ylab yetkazish xizmati mavjud (kelishilgan holda)

Buyurtma berish uchun yozing yoki qo‘ng‘iroq qiling 📞
"""
)

@bot.message_handler(func=lambda message: message.text == "📞 Aloqa")
def contact(message):
    bot.send_message(message.chat.id,
                     "📲 Tel: +998901234567\n"
                     "✈️ Telegram: @username")

bot.polling()
