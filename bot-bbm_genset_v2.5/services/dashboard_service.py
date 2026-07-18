from services.sheets_service import SheetsService


class DashboardService:

    def __init__(self):
        self.sheet = SheetsService()

    def summary_today(self):

        aktif = self.sheet.get_active_locations()

        bbm = self.sheet.get_today_bbm()
        hm = self.sheet.get_today_hour_meter()

        bbm_lokasi = {
            str(row["lokasi_id"]).strip()
            for row in bbm
            if row.get("lokasi_id")
        }

        hm_lokasi = {
            str(row["lokasi_id"]).strip()
            for row in hm
            if row.get("lokasi_id")
        }

        bbm_belum_list = []
        hm_belum_list = []

        for lokasi in aktif:

            lokasi_id = str(lokasi["lokasi_id"]).strip()
            nama = lokasi["nama_lokasi"]

            if lokasi_id not in bbm_lokasi:
                bbm_belum_list.append(nama)

            if lokasi_id not in hm_lokasi:
                hm_belum_list.append(nama)

        total = len(aktif)

        return {

            "total_lokasi": total,

            "bbm_masuk": len(bbm_lokasi),
            "bbm_belum": len(bbm_belum_list),

            "hm_masuk": len(hm_lokasi),
            "hm_belum": len(hm_belum_list),

            "bbm_belum_list": bbm_belum_list,

            "hm_belum_list": hm_belum_list,
        }