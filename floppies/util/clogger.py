import logging
import coloredlogs
from .cloglevel import ClogLevel

logger = logging.getLogger(__name__)


class Clogger():
    # TODO: Make it so ClogLevel.NOTICE shows up as 'NOTICE' instead of
    #       'Level ClogLevel.NOTICE' in logging output

    def __init__(self, loglevel: str):
        self.__format = '[%(asctime)s (%(name)s) %(levelname)s]: %(message)s'
        self.__datefmt = '%H:%M:%S'
        self.__field_styles = {
            'asctime': {'color': 'white'},
            'levelname': {
                # 'bold': True,
                'color': 'white'
            },
            'name': {'color': 'blue'}
        }
        self.__level = ClogLevel[loglevel]

    def install(self):
        coloredlogs.install(
            level=self.__level,
            fmt=self.__format,
            datefmt=self.__datefmt,
            field_styles=self.__field_styles
        )
