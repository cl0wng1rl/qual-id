from qual_id.cli.flag import Flag

class Parser:
    def __init__(self, arguments):
        self._arguments = arguments
        self._config = {"format": "csv"}
        self._shift_arguments()

    def parse(self):
        while len(self._arguments):
            self._extract_parameter(self._get_next_flag())
        return self._config

    def _get_next_flag(self):
        return next((flag for flag in Flag if flag.value.equals(self._arguments[0])), None)

    def _extract_parameter(self, flag):
        self._shift_arguments()
        self._config[flag.value.name()] = self._arguments[0]
        self._shift_arguments()

    def _shift_arguments(self):
        self._arguments = self._arguments[1:]
