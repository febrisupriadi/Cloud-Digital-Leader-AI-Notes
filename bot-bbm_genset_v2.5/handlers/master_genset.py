from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
from states.conversation_states import GensetStates
from services.sheets_service import SheetsService
from services.validation_service import is_number
from handlers.start import MAIN_MENU

from utils.keyboards import YES_NO

STATUS_MENU = [["Aktif"], ["Standby"], ["Rusak"], ["Maintenance"]]


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


async def genset_start(update, context):
    await update.message.reply_text(
        "Pilih lokasi untuk input genset:",
        reply_markup=ReplyKeyboardMarkup(_locations_keyboard(), resize_keyboard=True)
    )
    return GensetStates.LOCATION


async def g_location(update, context):
    text = update.message.text.strip()
    if "|" not in text:
        await update.message.reply_text("Format lokasi tidak valid. Pilih lokasi dari tombol.")
        return GensetStates.LOCATION

    lokasi_id, lokasi_name = [x.strip() for x in text.split("|", 1)]
    context.user_data["g_lokasi_id"] = lokasi_id
    context.user_data["g_lokasi_name"] = lokasi_name

    await update.message.reply_text(
        "Masukkan nama/label genset:",
        reply_markup=ReplyKeyboardRemove()
    )
    return GensetStates.NAME


async def g_name(update, context):
    context.user_data["g_nama"] = update.message.text.strip()
    await update.message.reply_text("Masukkan merek genset:")
    return GensetStates.BRAND


async def g_brand(update, context):
    context.user_data["g_merek"] = update.message.text.strip()
    await update.message.reply_text("Masukkan model genset:")
    return GensetStates.MODEL


async def g_model(update, context):
    context.user_data["g_model"] = update.message.text.strip()
    await update.message.reply_text("Masukkan kapasitas KVA:")
    return GensetStates.KVA


async def g_kva(update, context):
    text = update.message.text.strip()
    if not is_number(text):
        await update.message.reply_text("Kapasitas harus angka. Masukkan ulang:")
        return GensetStates.KVA

    context.user_data["g_kva"] = text
    await update.message.reply_text("Masukkan nomor seri (boleh - jika kosong):")
    return GensetStates.SERIAL


async def g_serial(update, context):
    context.user_data["g_serial"] = update.message.text.strip()
    await update.message.reply_text(
        "Pilih status genset:",
        reply_markup=ReplyKeyboardMarkup(STATUS_MENU, resize_keyboard=True)
    )
    return GensetStates.STATUS


async def g_status(update, context):
    context.user_data["g_status"] = update.message.text.strip()

    d = context.user_data

    msg = (
        "📋 KONFIRMASI DATA GENSET\n\n"
        f"📍 Lokasi      : {d['g_lokasi_name']}\n"
        f"⚡ Nama        : {d['g_nama']}\n"
        f"🏷️ Merek       : {d['g_merek']}\n"
        f"🛠️ Model       : {d['g_model']}\n"
        f"🔋 KVA         : {d['g_kva']}\n"
        f"🔢 Serial      : {d['g_serial']}\n"
        f"📌 Status      : {d['g_status']}\n\n"
        "Silakan periksa kembali data di atas.\n"
        "Tekan tombol yang tersedia untuk melanjutkan."
    )

    await update.message.reply_text(
        msg,
        reply_markup=YES_NO
    )

    return GensetStates.CONFIRM


async def g_confirm(update, context):
    """
    Konfirmasi penyimpanan data genset.
    """

    pilihan = update.message.text.strip()

    # Tombol BATAL
    if pilihan == "❌ BATAL":
        return await back_to_main_menu(
            update,
            "Input data genset dibatalkan."
        )

    # Tombol selain YA SIMPAN / BATAL
    if pilihan != "✅ YA SIMPAN":
        await update.message.reply_text(
            "Silakan gunakan tombol yang tersedia.",
            reply_markup=YES_NO
        )
        return GensetStates.CONFIRM

    d = context.user_data
    svc = SheetsService()

    genset_id = svc.add_genset(
        d["g_lokasi_id"],
        d["g_lokasi_name"],
        d["g_nama"],
        d["g_merek"],
        d["g_model"],
        d["g_kva"],
        d["g_serial"],
        d["g_status"]
    )

    svc.write_log(
        update.effective_user.id,
        "",
        "Input Data Genset",
        "submit",
        "MASTER_GENSET",
        genset_id,
        "sukses"
    )

    return await back_to_main_menu(
        update,
        f"✅ Data genset berhasil disimpan.\n\n"
        f"ID Genset : {genset_id}"
    )


async def cancel(update, context):
    return await back_to_main_menu(update, "Input data genset dibatalkan.")