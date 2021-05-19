from qual_id.cli.info.flag import Flag
from qual_id.cli.info.info_config import InfoConfig
from qual_id.cli.info.info_factory import InfoFactory

class Parser:
    def parse(self, arguments):
        arguments = arguments[2:]
        parameter = Flag.from_string(arguments[0])
        value = arguments[1] if len(arguments) > 1 else None
        info = InfoFactory.get(parameter, value)
        return InfoConfig(parameter, value, info)
