from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler
from states.conversation_states import TangkiStates
from services.sheets_service import SheetsService
from services.validation_service import is_number
from handlers.start import MAIN_MENU

from utils.keyboards import YES_NO

LINK_MENU = [["Ya"], ["Tidak"]]
JENIS_MENU = [["Harian"], ["Bulanan"]]
METODE_MENU = [["sounding"], ["gauge"], ["estimasi"]]
STATUS_MENU = [["Aktif"], ["Nonaktif"], ["Bocor"], ["Maintenance"]]


def _locations_keyboard():
    svc = SheetsService()
    locs = svc.get_locations()
    return [[f"{r['lokasi_id']} | {r['nama_lokasi']}"] for r in locs]


def _genset_keyboard(lokasi_id):
    svc = SheetsService()
    gensets = svc.get_gensets_by_location(lokasi_id)
    return [[f"{r['genset_id']} | {r['nama_genset']}"] for r in gensets] if gensets else [["- Tidak ada genset -"]]


async def back_to_main_menu(update, text):
    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
    )
    return ConversationHandler.END


async def tangki_start(update, context):
    await update.message.reply_text(
        "Pilih lokasi untuk input tangki:",
        reply_markup=ReplyKeyboardMarkup(_locations_keyboard(), resize_keyboard=True)
    )
    return TangkiStates.LOCATION


async def t_location(update, context):
    text = update.message.text.strip()
    if "|" not in text:
        await update.message.reply_text("Format lokasi tidak valid. Pilih lokasi dari tombol.")
        return TangkiStates.LOCATION

    lokasi_id, lokasi_name = [x.strip() for x in text.split("|", 1)]
    context.user_data["t_lokasi_id"] = lokasi_id
    context.user_data["t_lokasi_name"] = lokasi_name

    await update.message.reply_text(
        "Apakah tangki ini terkait genset tertentu?",
        reply_markup=ReplyKeyboardMarkup(LINK_MENU, resize_keyboard=True)
    )
    return TangkiStates.GENSET_LINK


async def t_link(update, context):
    ans = update.message.text.strip().lower()

    if ans == "ya":
        kb = _genset_keyboard(context.user_data["t_lokasi_id"])
        await update.message.reply_text(
            "Pilih genset terkait:",
            reply_markup=ReplyKeyboardMarkup(kb, resize_keyboard=True)
        )
        return TangkiStates.GENSET

    context.user_data["t_genset_id"] = ""
    context.user_data["t_genset_name"] = ""
    await update.message.reply_text(
        "Masukkan nama tangki:",
        reply_markup=ReplyKeyboardRemove()
    )
    return TangkiStates.NAME


async def t_genset(update, context):
    text = update.message.text.strip()

    if text.startswith("- Tidak ada"):
        context.user_data["t_genset_id"] = ""
        context.user_data["t_genset_name"] = ""
    else:
        if "|" not in text:
            await update.message.reply_text("Format genset tidak valid. Pilih genset dari tombol.")
            return TangkiStates.GENSET
        gid, gname = [x.strip() for x in text.split("|", 1)]
        context.user_data["t_genset_id"] = gid
        context.user_data["t_genset_name"] = gname

    await update.message.reply_text(
        "Masukkan nama tangki:",
        reply_markup=ReplyKeyboardRemove()
    )
    return TangkiStates.NAME


async def t_name(update, context):
    context.user_data["t_nama"] = update.message.text.strip()
    await update.message.reply_text(
        "Pilih jenis tangki:",
        reply_markup=ReplyKeyboardMarkup(JENIS_MENU, resize_keyboard=True)
    )
    return TangkiStates.JENIS


async def t_jenis(update, context):
    context.user_data["t_jenis"] = update.message.text.strip()
    await update.message.reply_text(
        "Masukkan kapasitas tangki (liter):",
        reply_markup=ReplyKeyboardRemove()
    )
    return TangkiStates.KAPASITAS


async def t_kapasitas(update, context):
    text = update.message.text.strip()
    if not is_number(text):
        await update.message.reply_text("Kapasitas harus angka. Masukkan ulang:")
        return TangkiStates.KAPASITAS

    context.user_data["t_kapasitas"] = text
    await update.message.reply_text("Masukkan minimum stok (liter), boleh 0:")
    return TangkiStates.MIN_STOK


async def t_min(update, context):
    text = update.message.text.strip()
    if not is_number(text):
        await update.message.reply_text("Minimum stok harus angka. Masukkan ulang:")
        return TangkiStates.MIN_STOK

    if float(text) > float(context.user_data["t_kapasitas"]):
        await update.message.reply_text(
            "Minimum stok tidak boleh lebih besar dari kapasitas. Masukkan ulang:"
        )
        return TangkiStates.MIN_STOK

    context.user_data["t_min"] = text
    await update.message.reply_text(
        "Pilih metode pengukuran:",
        reply_markup=ReplyKeyboardMarkup(METODE_MENU, resize_keyboard=True)
    )
    return TangkiStates.METODE


async def t_metode(update, context):
    context.user_data["t_metode"] = update.message.text.strip()
    await update.message.reply_text(
        "Pilih status tangki:",
        reply_markup=ReplyKeyboardMarkup(STATUS_MENU, resize_keyboard=True)
    )
    return TangkiStates.STATUS


async def t_status(update, context):
    context.user_data["t_status"] = update.message.text.strip()

    d = context.user_data

    msg = (
        "📋 KONFIRMASI DATA TANGKI\n\n"
        f"📍 Lokasi        : {d['t_lokasi_name']}\n"
        f"⚡ Genset        : {d.get('t_genset_name', '-') or '-'}\n"
        f"🛢️ Nama Tangki   : {d['t_nama']}\n"
        f"📦 Jenis         : {d['t_jenis']}\n"
        f"💧 Kapasitas     : {d['t_kapasitas']} Liter\n"
        f"⚠️ Minimum Stok  : {d['t_min']} Liter\n"
        f"📏 Metode Ukur   : {d['t_metode']}\n"
        f"📌 Status        : {d['t_status']}\n\n"
        "Silakan periksa kembali data di atas.\n"
        "Tekan tombol yang tersedia untuk melanjutkan."
    )

    await update.message.reply_text(
        msg,
        reply_markup=YES_NO
    )

    return TangkiStates.CONFIRM


async def t_confirm(update, context):
    """
    Konfirmasi penyimpanan data tangki.
    """

    pilihan = update.message.text.strip()

    # Tombol BATAL
    if pilihan == "❌ BATAL":
        return await back_to_main_menu(
            update,
            "Input data tangki dibatalkan."
        )

    # Tombol selain YA SIMPAN / BATAL
    if pilihan != "✅ YA SIMPAN":
        await update.message.reply_text(
            "Silakan gunakan tombol yang tersedia.",
            reply_markup=YES_NO
        )
        return TangkiStates.CONFIRM

    d = context.user_data
    svc = SheetsService()

    tangki_id = svc.add_tangki(
        d["t_lokasi_id"],
        d["t_lokasi_name"],
        d.get("t_genset_id", ""),
        d.get("t_genset_name", ""),
        d["t_nama"],
        d["t_jenis"],
        d["t_kapasitas"],
        d["t_min"],
        d["t_metode"],
        d["t_status"]
    )

    svc.write_log(
        update.effective_user.id,
        "",
        "Input Data Tangki",
        "submit",
        "MASTER_TANGKI",
        tangki_id,
        "sukses"
    )

    return await back_to_main_menu(
        update,
        f"✅ Data tangki berhasil disimpan.\n\n"
        f"ID Tangki : {tangki_id}"
    )


async def cancel(update, context):
    return await back_to_main_menu(update, "Input data tangki dibatalkan.")