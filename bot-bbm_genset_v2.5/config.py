import os
from dotenv import load_dotenv
DEBUG=True

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "").strip()
GOOGLE_CREDENTIALS_FILE = os.getenv("GOOGLE_CREDENTIALS_FILE", "service_account.json").strip()
ADMIN_TELEGRAM_IDS = [x.strip() for x in os.getenv("ADMIN_TELEGRAM_IDS", "").split(",") if x.strip()]

REQUIRED_SHEETS = [
    "MASTER_LOKASI",
    "MASTER_PETUGAS",
    "MAP_PETUGAS_LOKASI",
    "MASTER_GENSET",
    "MASTER_TANGKI",
    "BOT_USERS",
    "STATUS_SETUP_LOKASI",
    "BOT_LOG",
]

def validate_config():
    missing = []
    if not BOT_TOKEN:
        missing.append("BOT_TOKEN")
    if not GOOGLE_SHEET_ID:
        missing.append("GOOGLE_SHEET_ID")
    if not GOOGLE_CREDENTIALS_FILE:
        missing.append("GOOGLE_CREDENTIALS_FILE")
    if missing:
        raise RuntimeError("Config belum lengkap. Isi environment variable: " + ", ".join(missing))
