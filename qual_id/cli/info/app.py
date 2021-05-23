from .flag import Flag
from .info_message import InfoMessage
from .info_factory import InfoFactory

class App:
    @staticmethod
    def run(arguments):
        flag = arguments.get_flag()
        value = arguments.get_value()
        info = InfoFactory.get(flag, value)
        return InfoMessage(flag, value, info).message()
