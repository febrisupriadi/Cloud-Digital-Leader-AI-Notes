from telegram import ReplyKeyboardMarkup

MAIN_MENU = [
    ["Profil Saya", "📊 Dashboard"],
    ["Input Data Genset", "Input Data Tangki"],
    ["Laporan Harian"],
]


async def start(update, context):
    text = (
        "Selamat datang di Bot Monitoring BBM & Genset\n\n"
        "Menu utama:\n"
        "1. Profil Saya\n"
        "2. Dashboard\n"
        "3. Input Data Genset\n"
        "4. Input Data Tangki\n"
        "5. Laporan Harian"
    )

    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
    )