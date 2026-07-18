"""
BOT BBM Monitoring
Version : V2.3B

Seluruh text bot diletakkan di sini.
"""

# ==========================
# SUCCESS
# ==========================

SAVE_SUCCESS = "✅ Data berhasil disimpan."

REGISTER_SUCCESS = "✅ Registrasi berhasil."

# ==========================
# CANCEL
# ==========================

INPUT_CANCELLED = "❌ Proses dibatalkan."

# ==========================
# VALIDATION
# ==========================

INVALID_NUMBER = "Masukkan angka yang benar."

INVALID_CAPACITY = "Stok melebihi kapasitas tangki."

INVALID_HM = "Hour Meter tidak boleh lebih kecil dari laporan terakhir."

# ==========================
# DUPLICATE
# ==========================

DUPLICATE_WARNING = (
    "⚠ Hari ini sudah ada laporan.\n\n"
    "Apakah tetap ingin menyimpan data?"
)

# ==========================
# CONFIRM
# ==========================

CONFIRM_SAVE = (
    "Silakan periksa kembali data.\n\n"
    "Tekan ✅ YA SIMPAN untuk menyimpan."
)



# =========30 Juni 2026=================
# Patch ID : V2.3B-03
# Target   : utils/messages.py
# Impact   : Sangat Rendah
# Database : Tidak berubah
# Rollback : Sangat mudah


# ==========================
# Helper Function
# ==========================

def success_message(trx_id: str) -> str:
    """
    Pesan standar setelah transaksi berhasil disimpan.
    """
    return (
        f"{SAVE_SUCCESS}\n"
        f"ID : {trx_id}\n\n"
        "Silakan pilih menu berikutnya."
    )


def cancelled_message() -> str:
    """
    Pesan standar ketika user membatalkan proses.
    """
    return INPUT_CANCELLED


def invalid_button_message() -> str:
    """
    Pesan jika user mengetik manual saat seharusnya
    menggunakan tombol keyboard.
    """
    return "Silakan gunakan tombol yang tersedia."