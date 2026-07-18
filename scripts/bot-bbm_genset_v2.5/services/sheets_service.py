import gspread
from google.oauth2.service_account import Credentials
from config import GOOGLE_CREDENTIALS_FILE, GOOGLE_SHEET_ID, REQUIRED_SHEETS
from services.period_service import now_str

from datetime import date

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


class SheetsService:
    def __init__(self):
        creds = Credentials.from_service_account_file(
            GOOGLE_CREDENTIALS_FILE,
            scopes=SCOPES
        )
        client = gspread.authorize(creds)
        self.sh = client.open_by_key(GOOGLE_SHEET_ID)
        self._validate_required_sheets()

    def _validate_required_sheets(self):
        existing = [ws.title for ws in self.sh.worksheets()]
        missing = [s for s in REQUIRED_SHEETS if s not in existing]
        if missing:
            raise RuntimeError(
                "Spreadsheet belum lengkap. Sheet berikut belum ada: " + ", ".join(missing)
            )

    def ws(self, sheet_name):
        return self.sh.worksheet(sheet_name)

    def get_all_records(self, sheet_name):
        return self.ws(sheet_name).get_all_records()

    def append_row(self, sheet_name, row):
        self.ws(sheet_name).append_row(row, value_input_option="USER_ENTERED")

    # =========================
    # MASTER DATA
    # =========================
    def get_locations(self):
        return self.get_all_records("MASTER_LOKASI")

    def get_gensets_by_location(self, lokasi_id):
        rows = self.get_all_records("MASTER_GENSET")
        return [
            r for r in rows
            if str(r.get("lokasi_id", "")).strip() == str(lokasi_id).strip()
        ]

    def get_tangki_by_location(self, lokasi_id):
        rows = self.get_all_records("MASTER_TANGKI")
        return [
            r for r in rows
            if str(r.get("lokasi_id", "")).strip() == str(lokasi_id).strip()
        ]

    def has_genset_by_location(self, lokasi_id):
        return len(self.get_gensets_by_location(lokasi_id)) > 0

    def has_tangki_by_location(self, lokasi_id):
        return len(self.get_tangki_by_location(lokasi_id)) > 0

    def get_tangki_by_id(self, tangki_id):
        rows = self.get_all_records("MASTER_TANGKI")
        for r in rows:
            if str(r.get("tangki_id", "")).strip() == str(tangki_id).strip():
                return r
        return None

    def get_genset_by_id(self, genset_id):
        rows = self.get_all_records("MASTER_GENSET")
        for r in rows:
            if str(r.get("genset_id", "")).strip() == str(genset_id).strip():
                return r
        return None

    # =========================
    # USER / PETUGAS
    # =========================
    def get_petugas_by_telegram_id(self, telegram_id):
        rows = self.get_all_records("BOT_USERS")
        for r in rows:
            if str(r.get("telegram_id", "")).strip() == str(telegram_id):
                return r
        return None

    def upsert_petugas(
        self,
        telegram_id,
        username,
        tg_name,
        nama_petugas,
        phone,
        jabatan,
        lokasi_id,
        lokasi_name,
        peran
    ):
        existing = self.get_petugas_by_telegram_id(telegram_id)
        if existing:
            raise RuntimeError("User Telegram ini sudah terdaftar. Update profil belum diaktifkan di v1.1.")

        petugas_rows = self.get_all_records("MASTER_PETUGAS")
        map_rows = self.get_all_records("MAP_PETUGAS_LOKASI")

        petugas_id = f"PTG{len(petugas_rows)+1:03d}"
        self.append_row("MASTER_PETUGAS", [
            petugas_id,
            nama_petugas,
            phone,
            str(telegram_id),
            f"@{username}" if username else "",
            jabatan,
            "Aktif",
            now_str()[:10],
            "-"
        ])

        map_id = f"MAP{len(map_rows)+1:03d}"
        self.append_row("MAP_PETUGAS_LOKASI", [
            map_id,
            lokasi_id,
            lokasi_name,
            petugas_id,
            nama_petugas,
            peran,
            now_str()[:10],
            "",
            "Aktif",
            "-"
        ])

        self.append_row("BOT_USERS", [
            str(telegram_id),
            f"@{username}" if username else "",
            tg_name,
            petugas_id,
            nama_petugas,
            "petugas",
            lokasi_id,
            "aktif",
            now_str(),
            now_str()
        ])
        return petugas_id

    # =========================
    # MASTER GENSET / TANGKI
    # =========================
    def add_genset(self, lokasi_id, lokasi_name, nama_genset, merek, model, kva, no_seri, status):
        rows = self.get_all_records("MASTER_GENSET")
        genset_id = f"GEN{len(rows)+1:03d}"
        kode_genset = f"G{len([r for r in rows if str(r.get('lokasi_id')) == lokasi_id])+1}"
        self.append_row("MASTER_GENSET", [
            genset_id,
            lokasi_id,
            lokasi_name,
            kode_genset,
            nama_genset,
            merek,
            model,
            kva,
            no_seri,
            "",
            status,
            "-"
        ])
        return genset_id

    def add_tangki(
        self,
        lokasi_id,
        lokasi_name,
        genset_id,
        genset_name,
        nama_tangki,
        jenis_tangki,
        kapasitas,
        minimum_stok,
        metode,
        status
    ):
        rows = self.get_all_records("MASTER_TANGKI")
        tangki_id = f"TNK{len(rows)+1:03d}"
        kode_tangki = f"T{len([r for r in rows if str(r.get('lokasi_id')) == lokasi_id])+1}"
        self.append_row("MASTER_TANGKI", [
            tangki_id,
            lokasi_id,
            lokasi_name,
            genset_id,
            genset_name,
            kode_tangki,
            nama_tangki,
            jenis_tangki,
            kapasitas,
            minimum_stok,
            metode,
            status,
            "-"
        ])
        return tangki_id

    # =========================
    # TRANSAKSI
    # =========================
    def add_trx_bbm(
        self,
        lokasi_id,
        lokasi_name,
        tangki_id,
        tangki_name,
        stok_liter,
        petugas_id,
        nama_petugas,
        telegram_id
    ):
        rows = self.get_all_records("TRX_STOK_BBM")
        trx_id = f"BBM{len(rows)+1:05d}"
        self.append_row("TRX_STOK_BBM", [
            trx_id,
            now_str()[:10],
            now_str()[11:19],
            lokasi_id,
            lokasi_name,
            tangki_id,
            tangki_name,
            stok_liter,
            petugas_id,
            nama_petugas,
            str(telegram_id),
            "-"
        ])
        return trx_id

    def add_trx_hour_meter(
        self,
        lokasi_id,
        lokasi_name,
        genset_id,
        genset_name,
        hm_value,
        petugas_id,
        nama_petugas,
        telegram_id
    ):
        rows = self.get_all_records("TRX_HOUR_METER")
        trx_id = f"HM{len(rows)+1:05d}"
        self.append_row("TRX_HOUR_METER", [
            trx_id,
            now_str()[:10],
            now_str()[11:19],
            lokasi_id,
            lokasi_name,
            genset_id,
            genset_name,
            hm_value,
            petugas_id,
            nama_petugas,
            str(telegram_id),
            "-"
        ])
        return trx_id
    
    def add_trx_hm(
        self,
        lokasi_id,
        lokasi_name,
        genset_id,
        genset_name,
        hm_value,
        petugas_id,
        nama_petugas,
        telegram_id
    ):
        rows = self.get_all_records("TRX_HOUR_METER")
        trx_id = f"HM{len(rows)+1:05d}"
        self.append_row("TRX_HOUR_METER", [
            trx_id,
            now_str()[:10],
            now_str()[11:19],
            lokasi_id,
            lokasi_name,
            genset_id,
            genset_name,
            hm_value,
            petugas_id,
            nama_petugas,
            str(telegram_id),
            "-"
        ])
        return trx_id

    def get_last_hour_meter(self, genset_id):
        rows = self.get_all_records("TRX_HOUR_METER")
        filtered = [
            r for r in rows
            if str(r.get("genset_id", "")).strip() == str(genset_id).strip()
        ]
        if not filtered:
            return None

        # Ambil record terakhir berdasarkan urutan append sheet
        last_row = filtered[-1]
        return last_row

    def get_last_bbm_by_tangki(self, tangki_id):
        rows = self.get_all_records("TRX_STOK_BBM")
        filtered = [
            r for r in rows
            if str(r.get("tangki_id", "")).strip() == str(tangki_id).strip()
        ]
        if not filtered:
            return None

        last_row = filtered[-1]
        return last_row
    


    # =========================
    # LOG BOT
    # =========================
    def write_log(self, telegram_id, nama_petugas, menu, aksi, target_sheet, ref_id, catatan):
        self.append_row("BOT_LOG", [
            "",
            now_str(),
            str(telegram_id),
            nama_petugas,
            menu,
            aksi,
            target_sheet,
            ref_id,
            catatan
        ])


    # Tambahkan 2 function baru.

    def find_today_bbm(self, lokasi_id, tangki_id):
        """
        Mengembalikan laporan stok BBM hari ini
        berdasarkan lokasi dan tangki.
        """

        rows = self.get_all_records("TRX_STOK_BBM")

        today = date.today().isoformat()

        for row in reversed(rows):
            if (
                str(row.get("tanggal", "")).strip() == today
                and str(row.get("lokasi_id", "")).strip() == str(lokasi_id)
                and str(row.get("tangki_id", "")).strip() == str(tangki_id)
            ):
                return row

        return None
    
    def find_today_hour_meter(self, lokasi_id, genset_id):

        rows = self.get_all_records("TRX_HOUR_METER")

        today = date.today().isoformat()

        for row in reversed(rows):
            if (
                str(row.get("tanggal", "")).strip() == today
                and str(row.get("lokasi_id", "")).strip() == str(lokasi_id)
                and str(row.get("genset_id", "")).strip() == str(genset_id)
            ):
                return row

        return None
    
    
    def get_active_locations(self):
        """
        Mengembalikan seluruh lokasi yang aktif.
        """

        rows = self.get_all_records("MASTER_LOKASI")

        return [
            row
            for row in rows
            if str(row.get("status_lokasi", "")).strip().lower() == "aktif"
        ]
    

    def get_today_bbm(self):
        """
        Mengembalikan seluruh transaksi BBM hari ini.
        """

        today = date.today().isoformat()

        rows = self.get_all_records("TRX_STOK_BBM")

        return [
            row
            for row in rows
            if str(row.get("tanggal", "")).strip() == today
        ]
    

    def get_today_hour_meter(self):
        """
        Mengembalikan seluruh transaksi Hour Meter hari ini.
        """

        today = date.today().isoformat()

        rows = self.get_all_records("TRX_HOUR_METER")

        return [
            row
            for row in rows
            if str(row.get("tanggal", "")).strip() == today
        ]