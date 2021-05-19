from qual_id.cli.info.flag import Flag
from qual_id.cli.info.info_factory import InfoFactory

class Validator:
    def __init__(self, arguments):
        self._is_valid = True
        self._error_message = None
        self._validate(arguments)

    def is_valid(self):
        return self._is_valid

    def error_message(self):
        return self._error_message

    def _validate(self, arguments):
        arguments = arguments[2:]
        parameter = Flag.from_string(arguments[0])
        if not parameter:
            self._is_valid = False
            self._error_message = "invalid info value: {0}".format(arguments[0])
            return
        if len(arguments) > 1:
            self._check_value(parameter, arguments[1])
    
    def _check_value(self, parameter, value):
        if parameter.value.is_singular():
            self._is_valid = False
            self._error_message = "invalid value: {0}".format(value)
        elif not InfoFactory.has(parameter, value):
            self._is_valid = False
            self._error_message = "invalid {0} value: {1}".format(parameter.value.name(), value)