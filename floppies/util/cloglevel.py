from enum import IntEnum


class ClogLevel(IntEnum):
    NOTSET = 0,
    DEBUG = 10,
    INFO = 20,
    NOTICE = 25,
    WARNING = 30,
    ERROR = 40,
    CRITICAL = 50
