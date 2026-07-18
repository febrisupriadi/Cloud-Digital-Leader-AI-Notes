"""
BOT BBM Monitoring
Version : V2.3B

Semua ReplyKeyboard Telegram disimpan di sini.
Jangan membuat keyboard langsung di handler.
"""

from telegram import ReplyKeyboardMarkup

# ==========================
# MAIN MENU
# ==========================

MAIN_MENU = ReplyKeyboardMarkup(
    [
        ["📝 Registrasi"],
        ["⛽ Laporan Harian"],
        ["📊 Laporan Mingguan"],
        ["📅 Laporan Bulanan"],
    ],
    resize_keyboard=True,
)

# ==========================
# YES / NO
# ==========================

YES_NO = ReplyKeyboardMarkup(
    [
        ["✅ YA SIMPAN"],
        ["❌ BATAL"],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

# ==========================
# BACK
# ==========================

BACK = ReplyKeyboardMarkup(
    [
        ["⬅ Kembali"],
    ],
    resize_keyboard=True,
)

# ==========================
# CANCEL
# ==========================

CANCEL = ReplyKeyboardMarkup(
    [
        ["❌ BATAL"],
    ],
    resize_keyboard=True,
)

# ==========================
# Helper
# ==========================

def keyboard_from_rows(rows):
    """
    Mengubah list menjadi ReplyKeyboardMarkup.

    Contoh
    -------
    rows = [
        ["Tangki A"],
        ["Tangki B"],
        ["Tangki C"],
    ]
    """
    return ReplyKeyboardMarkup(
        rows,
        resize_keyboard=True,
        one_time_keyboard=True,
    )