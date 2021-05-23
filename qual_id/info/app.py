from qual_id.info.flag import Flag
from qual_id.info.info_message import InfoMessage
from qual_id.info.info_factory import InfoFactory

class App:
    @staticmethod
    def run(arguments):
        flag = arguments.get_flag()
        value = arguments.get_value()
        info = InfoFactory.get(flag, value)
        return InfoMessage(flag, value, info).message()
