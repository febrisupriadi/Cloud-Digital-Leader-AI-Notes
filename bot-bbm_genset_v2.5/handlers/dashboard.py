from telegram import Update
from telegram.ext import ContextTypes

from services.dashboard_service import DashboardService


async def dashboard_today(update: Update, context: ContextTypes.DEFAULT_TYPE):

    svc = DashboardService()

    data = svc.summary_today()

    text = (
        "📊 DASHBOARD HARI INI\n\n"
        f"🏢 Total Lokasi : {data['total_lokasi']}\n\n"

        "⛽ STOK BBM\n"
        f"✅ Sudah Lapor : {data['bbm_masuk']}\n"
        f"⏳ Belum Lapor : {data['bbm_belum']}\n\n"

        "⚡ HOUR METER\n"
        f"✅ Sudah Lapor : {data['hm_masuk']}\n"
        f"⏳ Belum Lapor : {data['hm_belum']}"
    )

    await update.message.reply_text(text)