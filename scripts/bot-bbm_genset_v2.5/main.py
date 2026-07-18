from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
)

from handlers.dashboard import dashboard_today

from config import BOT_TOKEN, validate_config
from services.sheets_service import SheetsService
from states.conversation_states import (
    RegisterStates,
    GensetStates,
    TangkiStates,
    DailyReportStates,
)

from handlers.start import start

# ===== PROFILE / REGISTRASI PETUGAS =====
from handlers.profile import (
    register_start,
    reg_name,
    reg_phone,
    reg_position,
    reg_location,
    reg_role,
    reg_confirm,
    cancel as profile_cancel,
)

# ===== MASTER GENSET =====
from handlers.master_genset import (
    genset_start,
    g_location,
    g_name,
    g_brand,
    g_model,
    g_kva,
    g_serial,
    g_status,
    g_confirm,
    cancel as genset_cancel,
)

# ===== MASTER TANGKI =====
from handlers.master_tangki import (
    tangki_start,
    t_location,
    t_link,
    t_genset,
    t_name,
    t_jenis,
    t_kapasitas,
    t_min,
    t_metode,
    t_status,
    t_confirm,
    cancel as tangki_cancel,
)

# ===== LAPORAN HARIAN =====
from handlers.daily_report import (
    report_start,
    report_menu,
    bbm_tangki,
    bbm_stok,
    bbm_confirm,
    bbm_force_confirm,
    hm_genset,
    hm_value,
    hm_confirm,
    hm_force_confirm,
    cancel as report_cancel,
)


def build_app():
    validate_config()
    from services.dashboard_service import DashboardService

    dashboard = DashboardService()

    print("===== DASHBOARD =====")

    from pprint import pprint
    pprint(dashboard.summary_today())


    SheetsService()  # validasi koneksi sheet saat startup
    
    app = Application.builder().token(BOT_TOKEN).build()

    # =========================================================
    # 1) CONVERSATION: PROFIL SAYA / REGISTRASI PETUGAS
    # =========================================================
    profile_conv = ConversationHandler(
        entry_points=[
            MessageHandler(filters.Regex("^Profil Saya$"), register_start),
        ],
        states={
            RegisterStates.NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, reg_name)
            ],
            RegisterStates.PHONE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, reg_phone)
            ],
            RegisterStates.POSITION: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, reg_position)
            ],
            RegisterStates.LOCATION: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, reg_location)
            ],
            RegisterStates.ROLE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, reg_role)
            ],
            RegisterStates.CONFIRM: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, reg_confirm)
            ],
        },
        fallbacks=[
            CommandHandler("cancel", profile_cancel),
        ],
        name="profile_conversation",
        persistent=False,
    )

    # =========================================================
    # 2) CONVERSATION: INPUT MASTER GENSET
    # =========================================================
    genset_conv = ConversationHandler(
        entry_points=[
            MessageHandler(filters.Regex("^Input Data Genset$"), genset_start),
        ],
        states={
            GensetStates.LOCATION: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, g_location)
            ],
            GensetStates.NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, g_name)
            ],
            GensetStates.BRAND: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, g_brand)
            ],
            GensetStates.MODEL: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, g_model)
            ],
            GensetStates.KVA: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, g_kva)
            ],
            GensetStates.SERIAL: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, g_serial)
            ],
            GensetStates.STATUS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, g_status)
            ],
            GensetStates.CONFIRM: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, g_confirm)
            ],
        },
        fallbacks=[
            CommandHandler("cancel", genset_cancel),
        ],
        name="genset_conversation",
        persistent=False,
    )

    # =========================================================
    # 3) CONVERSATION: INPUT MASTER TANGKI
    # =========================================================
    tangki_conv = ConversationHandler(
        entry_points=[
            MessageHandler(filters.Regex("^Input Data Tangki$"), tangki_start),
        ],
        states={
            TangkiStates.LOCATION: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, t_location)
            ],
            TangkiStates.GENSET_LINK: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, t_link)
            ],
            TangkiStates.GENSET: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, t_genset)
            ],
            TangkiStates.NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, t_name)
            ],
            TangkiStates.JENIS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, t_jenis)
            ],
            TangkiStates.KAPASITAS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, t_kapasitas)
            ],
            TangkiStates.MIN_STOK: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, t_min)
            ],
            TangkiStates.METODE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, t_metode)
            ],
            TangkiStates.STATUS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, t_status)
            ],
            TangkiStates.CONFIRM: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, t_confirm)
            ],
        },
        fallbacks=[
            CommandHandler("cancel", tangki_cancel),
        ],
        name="tangki_conversation",
        persistent=False,
    )

    # =========================================================
    # 4) CONVERSATION: LAPORAN HARIAN
    # =========================================================
    report_conv = ConversationHandler(
        entry_points=[
            MessageHandler(filters.Regex("^Laporan Harian$"), report_start),
        ],
        states={
            DailyReportStates.MENU: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, report_menu)
            ],
            DailyReportStates.BBM_TANGKI: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, bbm_tangki)
            ],
            DailyReportStates.BBM_STOK: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, bbm_stok)
            ],
            DailyReportStates.BBM_CONFIRM: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, bbm_confirm)
            ],
            DailyReportStates.BBM_FORCE_CONFIRM: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND,
                    bbm_force_confirm
                )
            ],
            DailyReportStates.HM_GENSET: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, hm_genset)
            ],
            DailyReportStates.HM_VALUE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, hm_value)
            ],
            DailyReportStates.HM_CONFIRM: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, hm_confirm)
            ],
            DailyReportStates.HM_FORCE_CONFIRM: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, hm_force_confirm)
            ],
        },
        fallbacks=[
            CommandHandler("cancel", report_cancel),
        ],
        name="daily_report_conversation",
        persistent=False,
    )

    # =========================================================
    # REGISTER HANDLERS
    # =========================================================
    app.add_handler(CommandHandler("start", start))

    app.add_handler(profile_conv)
    app.add_handler(genset_conv)
    app.add_handler(tangki_conv)
    app.add_handler(report_conv)
    app.add_handler(
        MessageHandler(
            filters.Regex("^📊 Dashboard$"),
            dashboard_today
        )
    )

    return app


if __name__ == "__main__":
    app = build_app()
    print("Bot is running...")
    app.run_polling()