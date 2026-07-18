from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from states.conversation_states import DailyReportStates
from services.sheets_service import SheetsService
from services.validation_service import is_number
from handlers.start import MAIN_MENU

from utils.keyboards import YES_NO
from utils import messages

from services.report_service import ReportService



MENU = [
    ["Stok BBM"],
    ["Jam Jalan Genset"]
]


def _to_float(value):
    """
    Normalisasi angka dari input/user/sheet:
    - "123"
    - "123.5"
    - "123,5"
    - "1,234.5" -> tidak direkomendasikan, tapi kita minimal amankan koma desimal
    """
    if value is None:
        raise ValueError("Nilai kosong")
    s = str(value).strip().replace(",", ".")
    return float(s)


async def back_to_main_menu(update, text):
    await update.message.reply_text(
        text,
        reply_markup=ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
    )
    return ConversationHandler.END


def _tangki_keyboard(lokasi_id):
    rows = SheetsService().get_tangki_by_location(lokasi_id)
    if not rows:
        return [["- Tidak ada tangki -"]]
    return [[f"{r['tangki_id']} | {r['nama_tangki']}"] for r in rows]


def _genset_keyboard(lokasi_id):
    rows = SheetsService().get_gensets_by_location(lokasi_id)
    if not rows:
        return [["- Tidak ada genset -"]]
    return [[f"{r['genset_id']} | {r['nama_genset']}"] for r in rows]


async def report_start(update, context):
    svc = SheetsService()
    user = svc.get_petugas_by_telegram_id(update.effective_user.id)

    if not user:
        return await back_to_main_menu(
            update,
            "Anda belum terdaftar.\nSilakan lengkapi Profil Saya terlebih dahulu."
        )

    lokasi_id = str(user.get("lokasi_default_id", "")).strip()
    if not lokasi_id:
        return await back_to_main_menu(
            update,
            "Profil Anda belum memiliki lokasi default.\nSilakan perbarui Profil Saya terlebih dahulu."
        )

    context.user_data["r_petugas_id"] = user.get("petugas_id", "")
    context.user_data["r_nama_petugas"] = user.get("nama_petugas", "")
    context.user_data["r_lokasi_id"] = lokasi_id

    loc_name = ""
    for loc in svc.get_locations():
        if str(loc.get("lokasi_id", "")).strip() == lokasi_id:
            loc_name = loc.get("nama_lokasi", "")
            break

    context.user_data["r_lokasi_name"] = loc_name

    if not svc.has_genset_by_location(lokasi_id):
        return await back_to_main_menu(
            update,
            f"Lokasi {lokasi_id} belum memiliki master genset.\nSilakan lengkapi melalui menu Input Data Genset."
        )

    if not svc.has_tangki_by_location(lokasi_id):
        return await back_to_main_menu(
            update,
            f"Lokasi {lokasi_id} belum memiliki master tangki.\nSilakan lengkapi melalui menu Input Data Tangki."
        )

    await update.message.reply_text(
        f"Lokasi laporan Anda: {loc_name}\nPilih jenis laporan:",
        reply_markup=ReplyKeyboardMarkup(MENU, resize_keyboard=True)
    )
    return DailyReportStates.MENU


async def report_menu(update, context):
    choice = update.message.text.strip().lower()

    if choice == "stok bbm":
        await update.message.reply_text(
            "Pilih tangki:",
            reply_markup=ReplyKeyboardMarkup(
                _tangki_keyboard(context.user_data["r_lokasi_id"]),
                resize_keyboard=True
            )
        )
        return DailyReportStates.BBM_TANGKI

    if choice == "jam jalan genset":
        await update.message.reply_text(
            "Pilih genset:",
            reply_markup=ReplyKeyboardMarkup(
                _genset_keyboard(context.user_data["r_lokasi_id"]),
                resize_keyboard=True
            )
        )
        return DailyReportStates.HM_GENSET

    await update.message.reply_text("Pilih menu yang tersedia.")
    return DailyReportStates.MENU


async def bbm_tangki(update, context):
    text = update.message.text.strip()

    if text.startswith("- Tidak ada"):
        return await back_to_main_menu(update, "Tidak ada tangki aktif di lokasi Anda.")

    if "|" not in text:
        await update.message.reply_text("Format pilihan tangki tidak valid. Silakan pilih dari tombol.")
        return DailyReportStates.BBM_TANGKI

    tangki_id, nama_tangki = [x.strip() for x in text.split("|", 1)]
    context.user_data["bbm_tangki_id"] = tangki_id
    context.user_data["bbm_tangki_name"] = nama_tangki

    await update.message.reply_text(
        "Masukkan stok BBM saat ini (liter):",
        reply_markup=ReplyKeyboardRemove()
    )
    return DailyReportStates.BBM_STOK


async def bbm_stok(update, context):
    text = update.message.text.strip()

    if not is_number(text):
        await update.message.reply_text("Stok harus berupa angka. Contoh: 120 atau 120.5")
        return DailyReportStates.BBM_STOK

    try:
        stok = _to_float(text)
    except Exception:
        await update.message.reply_text("Format stok tidak valid. Gunakan angka, contoh: 120 atau 120.5")
        return DailyReportStates.BBM_STOK

    if stok < 0:
        await update.message.reply_text("Stok BBM tidak boleh negatif.")
        return DailyReportStates.BBM_STOK

    svc = SheetsService()
    tangki = svc.get_tangki_by_id(context.user_data["bbm_tangki_id"])
    if not tangki:
        return await back_to_main_menu(
            update,
            "Master tangki tidak ditemukan. Silakan ulangi dari menu utama."
        )

    kapasitas_raw = tangki.get("kapasitas_liter", tangki.get("kapasitas", ""))
    try:
        kapasitas = _to_float(kapasitas_raw)
    except Exception:
        return await back_to_main_menu(
            update,
            f"Kapasitas tangki {context.user_data['bbm_tangki_name']} belum valid di master. "
            "Silakan perbaiki data master tangki terlebih dahulu."
        )

    if stok > kapasitas:
        await update.message.reply_text(
            f"Stok melebihi kapasitas tangki.\n"
            f"Kapasitas tangki: {kapasitas}\n"
            f"Input stok: {stok}\n\n"
            "Silakan input ulang."
        )
        return DailyReportStates.BBM_STOK

    context.user_data["bbm_stok"] = stok

    await update.message.reply_text(
        "Konfirmasi laporan stok BBM:\n"
        f"Tangki: {context.user_data['bbm_tangki_name']}\n"
        f"Stok: {stok} liter\n\n"
        f"{messages.CONFIRM_SAVE}",
        reply_markup=YES_NO
       
    )
    return DailyReportStates.BBM_CONFIRM


async def bbm_confirm(update, context):
    """
    Konfirmasi penyimpanan laporan stok BBM.
    """

    pilihan = update.message.text.strip()

    if pilihan == "❌ BATAL":
        return await back_to_main_menu(
            update,
            messages.cancelled_message()
        )

    if pilihan != "✅ YA SIMPAN":
        await update.message.reply_text(
            messages.invalid_button_message(),
            reply_markup=YES_NO
        )
        return DailyReportStates.BBM_CONFIRM

    service = ReportService()

    # ==========================================================
    # Cek duplicate
    # ==========================================================
    duplicate = service.check_duplicate_bbm(
        lokasi_id=context.user_data["r_lokasi_id"],
        tangki_id=context.user_data["bbm_tangki_id"],
    )

    if duplicate:

        context.user_data["duplicate_bbm"] = duplicate

        keyboard = ReplyKeyboardMarkup(
            [
                ["✅ TETAP SIMPAN"],
                ["❌ BATAL"],
            ],
            resize_keyboard=True
        )

        await update.message.reply_text(
            "⚠️ Laporan hari ini sudah ada.\n\n"
            f"🆔 ID      : {duplicate['trx_id']}\n"
            f"🕒 Jam     : {duplicate['jam']}\n"
            f"⛽ Stok    : {duplicate['stok_liter']} Liter\n\n"
            "Apakah Anda tetap ingin menyimpan laporan baru?",
            reply_markup=keyboard
        )

        return DailyReportStates.BBM_FORCE_CONFIRM

    # ==========================================================
    # Tidak ada duplicate
    # Simpan seperti biasa
    # ==========================================================

    trx = service.save_bbm(
        lokasi_id=context.user_data["r_lokasi_id"],
        lokasi_name=context.user_data["r_lokasi_name"],
        tangki_id=context.user_data["bbm_tangki_id"],
        tangki_name=context.user_data["bbm_tangki_name"],
        stok=context.user_data["bbm_stok"],
        petugas_id=context.user_data["r_petugas_id"],
        nama_petugas=context.user_data["r_nama_petugas"],
        telegram_id=update.effective_user.id,
    )

    return await back_to_main_menu(
        update,
        messages.success_message(trx)
    )


async def bbm_force_confirm(update, context):
    """
    Konfirmasi penyimpanan jika ditemukan duplicate.
    """

    pilihan = update.message.text.strip()

    if pilihan == "❌ BATAL":

        context.user_data.pop("duplicate_bbm", None)

        return await back_to_main_menu(
            update,
            "Laporan tidak disimpan."
        )

    if pilihan != "✅ TETAP SIMPAN":
        await update.message.reply_text(
            "Silakan gunakan tombol yang tersedia."
        )
        return DailyReportStates.BBM_FORCE_CONFIRM

    service = ReportService()

    trx = service.save_bbm(
        lokasi_id=context.user_data["r_lokasi_id"],
        lokasi_name=context.user_data["r_lokasi_name"],
        tangki_id=context.user_data["bbm_tangki_id"],
        tangki_name=context.user_data["bbm_tangki_name"],
        stok=context.user_data["bbm_stok"],
        petugas_id=context.user_data["r_petugas_id"],
        nama_petugas=context.user_data["r_nama_petugas"],
        telegram_id=update.effective_user.id,
    )

    context.user_data.pop("duplicate_bbm", None)

    return await back_to_main_menu(
        update,
        messages.success_message(trx)
    )

async def hm_genset(update, context):
    text = update.message.text.strip()

    if text.startswith("- Tidak ada"):
        return await back_to_main_menu(update, "Tidak ada genset aktif di lokasi Anda.")

    if "|" not in text:
        await update.message.reply_text("Format pilihan genset tidak valid. Silakan pilih dari tombol.")
        return DailyReportStates.HM_GENSET

    genset_id, nama_genset = [x.strip() for x in text.split("|", 1)]
    context.user_data["hm_genset_id"] = genset_id
    context.user_data["hm_genset_name"] = nama_genset

    await update.message.reply_text(
        "Masukkan hour meter saat ini:",
        reply_markup=ReplyKeyboardRemove()
    )
    return DailyReportStates.HM_VALUE


async def hm_value(update, context):
    text = update.message.text.strip()

    if not is_number(text):
        await update.message.reply_text("Hour meter harus berupa angka. Contoh: 1234 atau 1234.5")
        return DailyReportStates.HM_VALUE

    try:
        hm = _to_float(text)
    except Exception:
        await update.message.reply_text("Format hour meter tidak valid. Gunakan angka, contoh: 1234 atau 1234.5")
        return DailyReportStates.HM_VALUE

    if hm < 0:
        await update.message.reply_text("Hour meter tidak boleh negatif.")
        return DailyReportStates.HM_VALUE

    svc = SheetsService()
    last_row = svc.get_last_hour_meter(context.user_data["hm_genset_id"])

    if last_row:
        last_value_raw = last_row.get("hour_meter", last_row.get("hm_value", ""))
        try:
            last_value = _to_float(last_value_raw)
        except Exception:
            return await back_to_main_menu(
                update,
                "Data hour meter terakhir di sheet tidak valid. "
                "Silakan cek data transaksi sebelumnya terlebih dahulu."
            )

        if hm < last_value:
            await update.message.reply_text(
                f"Hour meter lebih kecil dari laporan terakhir.\n"
                f"HM terakhir: {last_value}\n"
                f"Input sekarang: {hm}\n\n"
                "Silakan input ulang."
            )
            return DailyReportStates.HM_VALUE

    context.user_data["hm_value"] = hm

    await update.message.reply_text(
        "Konfirmasi Laporan Jam Jalan Genset\n\n"
        f"Genset      : {context.user_data['hm_genset_name']}\n"
        f"Hour Meter  : {hm}\n\n"
        f"{messages.CONFIRM_SAVE}",
        reply_markup=YES_NO
    )

    return DailyReportStates.HM_CONFIRM


async def hm_confirm(update, context):
    """
    Konfirmasi penyimpanan Hour Meter.
    """

    pilihan = update.message.text.strip()

    if pilihan == "❌ BATAL":
        return await back_to_main_menu(
            update,
            messages.cancelled_message()
        )

    if pilihan != "✅ YA SIMPAN":
        await update.message.reply_text(
            messages.invalid_button_message(),
            reply_markup=YES_NO
        )
        return DailyReportStates.HM_CONFIRM

    service = ReportService()

    # ==========================================================
    # Cek duplicate
    # ==========================================================
    duplicate = service.check_duplicate_hour_meter(
        lokasi_id=context.user_data["r_lokasi_id"],
        genset_id=context.user_data["hm_genset_id"],
    )

    if duplicate:

        context.user_data["duplicate_hm"] = duplicate

        keyboard = ReplyKeyboardMarkup(
            [
                ["✅ TETAP SIMPAN"],
                ["❌ BATAL"],
            ],
            resize_keyboard=True
        )

        await update.message.reply_text(
            "⚠️ Laporan Hour Meter hari ini sudah ada.\n\n"
            f"🆔 ID      : {duplicate['trx_id']}\n"
            f"🕒 Jam     : {duplicate['jam']}\n"
            f"⏱ HM      : {duplicate['hour_meter']}\n\n"
            "Apakah Anda tetap ingin menyimpan laporan baru?",
            reply_markup=keyboard
        )

        return DailyReportStates.HM_FORCE_CONFIRM

    # ==========================================================
    # Tidak ada duplicate
    # ==========================================================

    trx = service.save_hm(
        lokasi_id=context.user_data["r_lokasi_id"],
        lokasi_name=context.user_data["r_lokasi_name"],
        genset_id=context.user_data["hm_genset_id"],
        genset_name=context.user_data["hm_genset_name"],
        hm=context.user_data["hm_value"],
        petugas_id=context.user_data["r_petugas_id"],
        nama_petugas=context.user_data["r_nama_petugas"],
        telegram_id=update.effective_user.id,
    )

    return await back_to_main_menu(
        update,
        messages.success_message(trx)
    )

async def hm_force_confirm(update, context):
    """
    Konfirmasi penyimpanan Hour Meter jika duplicate ditemukan.
    """

    pilihan = update.message.text.strip()

    if pilihan == "❌ BATAL":

        context.user_data.pop("duplicate_hm", None)

        return await back_to_main_menu(
            update,
            "Laporan Hour Meter tidak disimpan."
        )

    if pilihan != "✅ TETAP SIMPAN":
        await update.message.reply_text(
            "Silakan gunakan tombol yang tersedia."
        )
        return DailyReportStates.HM_FORCE_CONFIRM

    service = ReportService()

    trx = service.save_hm(
        lokasi_id=context.user_data["r_lokasi_id"],
        lokasi_name=context.user_data["r_lokasi_name"],
        genset_id=context.user_data["hm_genset_id"],
        genset_name=context.user_data["hm_genset_name"],
        hm=context.user_data["hm_value"],
        petugas_id=context.user_data["r_petugas_id"],
        nama_petugas=context.user_data["r_nama_petugas"],
        telegram_id=update.effective_user.id,
    )

    context.user_data.pop("duplicate_hm", None)

    return await back_to_main_menu(
        update,
        messages.success_message(trx)
    )

async def cancel(update, context):
    return await back_to_main_menu(update, "Proses dibatalkan.")