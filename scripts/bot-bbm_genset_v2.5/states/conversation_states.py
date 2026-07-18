from enum import IntEnum


class RegisterStates(IntEnum):
    NAME = 100
    PHONE = 101
    POSITION = 102
    LOCATION = 103
    ROLE = 104
    CONFIRM = 105


class GensetStates(IntEnum):
    LOCATION = 200
    NAME = 201
    BRAND = 202
    MODEL = 203
    KVA = 204
    SERIAL = 205
    STATUS = 206
    CONFIRM = 207


class TangkiStates(IntEnum):
    LOCATION = 300
    GENSET_LINK = 301
    GENSET = 302
    NAME = 303
    JENIS = 304
    KAPASITAS = 305
    MIN_STOK = 306
    METODE = 307
    STATUS = 308
    CONFIRM = 309


class DailyReportStates(IntEnum):
    MENU = 400

    BBM_TANGKI = 401
    BBM_STOK = 402
    BBM_CONFIRM = 403
    BBM_FORCE_CONFIRM = 404

    HM_GENSET = 410
    HM_VALUE = 411
    HM_CONFIRM = 412
    HM_FORCE_CONFIRM = 413