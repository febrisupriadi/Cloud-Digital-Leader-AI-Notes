"""
Report Service
Version : V2.3B

Seluruh business logic transaksi laporan
akan dipindahkan ke file ini secara bertahap.
"""

from services.sheets_service import SheetsService


class ReportService:

    def __init__(self):
        self.sheet = SheetsService()

    # ==========================================================
    # BBM
    # ==========================================================

    def save_bbm(
        self,
        lokasi_id,
        lokasi_name,
        tangki_id,
        tangki_name,
        stok,
        petugas_id,
        nama_petugas,
        telegram_id,
    ):
        """
        Menyimpan transaksi stok BBM.
        """

        trx = self.sheet.add_trx_bbm(
            lokasi_id,
            lokasi_name,
            tangki_id,
            tangki_name,
            stok,
            petugas_id,
            nama_petugas,
            telegram_id,
        )

        self.sheet.write_log(
            telegram_id,
            nama_petugas,
            "Laporan Harian",
            "submit_bbm",
            "TRX_STOK_BBM",
            trx,
            "laporan stok bbm",
        )

        return trx

    # ==========================================================
    # HM
    # ==========================================================

    def save_hm(
        self,
        lokasi_id,
        lokasi_name,
        genset_id,
        genset_name,
        hm,
        petugas_id,
        nama_petugas,
        telegram_id,
    ):
        """
        Menyimpan transaksi Hour Meter.
        """

        trx = self.sheet.add_trx_hm(
            lokasi_id,
            lokasi_name,
            genset_id,
            genset_name,
            hm,
            petugas_id,
            nama_petugas,
            telegram_id,
        )

        self.sheet.write_log(
            telegram_id,
            nama_petugas,
            "Laporan Harian",
            "submit_hm",
            "TRX_HM",
            trx,
            "laporan jam jalan genset",
        )

        return trx
    
    def check_duplicate_bbm(
        self,
        lokasi_id,
        tangki_id,
    ):
        return self.sheet.find_today_bbm(
            lokasi_id,
            tangki_id,
        )
    
    def check_duplicate_hour_meter(
        self,
        lokasi_id,
        genset_id,
    ):
        return self.sheet.find_today_hour_meter(
            lokasi_id,
            genset_id,
        )