from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
from states.conversation_states import RegisterStates
from services.sheets_service import SheetsService
from handlers.start import MAIN_MENU

from utils.keyboards import YES_NO

JABATAN_MENU = [["Teknisi"], ["Operator"], ["Pengawas"]]
PERAN_MENU = [["PIC"], ["Backup"], ["Shift"]]


def _locations_keyboard():
    svc = SheetsService()
    locs = svc.get_locations()
    return [[f"{r['lokasi_id']} | {r['nama_lokasi']}"] for r in locs]


async def back_to_main_menu(update, text):
    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
    )
    return ConversationHandler.END


async def register_start(update, context: ContextTypes.DEFAULT_TYPE):
    svc = SheetsService()
    existing = svc.get_petugas_by_telegram_id(update.effective_user.id)
    if existing:
        return await back_to_main_menu(
            update,
            f"User Telegram ini sudah terdaftar sebagai {existing.get('nama_petugas','-')} "
            f"di lokasi {existing.get('lokasi_default_id','-')}."
        )

    await update.message.reply_text(
        "Masukkan nama lengkap Anda:",
        reply_markup=ReplyKeyboardRemove()
    )
    return RegisterStates.NAME


async def reg_name(update, context):
    context.user_data["reg_nama"] = update.message.text.strip()
    await update.message.reply_text("Masukkan nomor HP:")
    return RegisterStates.PHONE


async def reg_phone(update, context):
    context.user_data["reg_phone"] = update.message.text.strip()
    await update.message.reply_text(
        "Pilih jabatan:",
        reply_markup=ReplyKeyboardMarkup(JABATAN_MENU, resize_keyboard=True)
    )
    return RegisterStates.POSITION


async def reg_position(update, context):
    context.user_data["reg_jabatan"] = update.message.text.strip()
    await update.message.reply_text(
        "Pilih lokasi tugas:",
        reply_markup=ReplyKeyboardMarkup(_locations_keyboard(), resize_keyboard=True)
    )
    return RegisterStates.LOCATION


async def reg_location(update, context):
    text = update.message.text.strip()
    if "|" not in text:
        await update.message.reply_text(
            "Format lokasi tidak valid. Pilih lokasi dari tombol yang tersedia."
        )
        return RegisterStates.LOCATION

    lokasi_id, lokasi_name = [x.strip() for x in text.split("|", 1)]
    context.user_data["reg_lokasi_id"] = lokasi_id
    context.user_data["reg_lokasi_name"] = lokasi_name

    await update.message.reply_text(
        "Pilih peran di lokasi:",
        reply_markup=ReplyKeyboardMarkup(PERAN_MENU, resize_keyboard=True)
    )
    return RegisterStates.ROLE


async def reg_role(update, context):
    context.user_data["reg_peran"] = update.message.text.strip()

    d = context.user_data

    msg = (
        "📋 KONFIRMASI DATA PROFIL\n\n"
        f"👤 Nama      : {d['reg_nama']}\n"
        f"📱 HP        : {d['reg_phone']}\n"
        f"💼 Jabatan   : {d['reg_jabatan']}\n"
        f"📍 Lokasi    : {d['reg_lokasi_name']}\n"
        f"👥 Peran     : {d['reg_peran']}\n\n"
        "Silakan periksa kembali data di atas.\n"
        "Tekan tombol yang tersedia untuk melanjutkan."
    )

    await update.message.reply_text(
        msg,
        reply_markup=YES_NO
    )

    return RegisterStates.CONFIRM


async def reg_confirm(update, context):
    """
    Konfirmasi penyimpanan profil petugas.
    """

    pilihan = update.message.text.strip()

    # Tombol BATAL
    if pilihan == "❌ BATAL":
        return await back_to_main_menu(
            update,
            "Registrasi profil dibatalkan."
        )

    # Tombol selain YA SIMPAN / BATAL
    if pilihan != "✅ YA SIMPAN":
        await update.message.reply_text(
            "Silakan gunakan tombol yang tersedia.",
            reply_markup=YES_NO
        )
        return RegisterStates.CONFIRM

    d = context.user_data
    user = update.effective_user
    svc = SheetsService()

    petugas_id = svc.upsert_petugas(
        telegram_id=user.id,
        username=user.username or "",
        tg_name=user.full_name or "",
        nama_petugas=d["reg_nama"],
        phone=d["reg_phone"],
        jabatan=d["reg_jabatan"],
        lokasi_id=d["reg_lokasi_id"],
        lokasi_name=d["reg_lokasi_name"],
        peran=d["reg_peran"],
    )

    svc.write_log(
        user.id,
        d["reg_nama"],
        "Registrasi Profil",
        "submit",
        "MASTER_PETUGAS",
        petugas_id,
        "registrasi sukses"
    )

    return await back_to_main_menu(
        update,
        f"✅ Registrasi berhasil.\n\n"
        f"ID Petugas : {petugas_id}"
    )


async def cancel(update, context):
    return await back_to_main_menu(update, "Proses registrasi profil dibatalkan.")