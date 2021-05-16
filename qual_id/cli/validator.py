from qual_id.cli.flag import Flag

class Validator:
    def __init__(self, arguments):
        self._is_help = False
        self._is_valid = True
        self._error_message = None
        self._arguments = arguments
        self._validate()

    def is_help(self):
        return self._is_help

    def is_valid(self):
        return self._is_valid

    def error_message(self):
        return self._error_message

    def _validate(self):
        self._shift_arguments()
        self._check_for_help() and self._extract_parameters()

    def _check_for_help(self):
        if any(map(lambda arg: Flag.HELP.value.equals(arg), self._arguments)):
            self._is_help = True
            self._is_valid = True
        return not self._is_help

    def _extract_parameters(self):
        while (len(self._arguments) and self._is_valid):
            self._extract_parameter(self._get_next_flag())

    def _extract_parameter(self, flag):
        self._shift_arguments()
        self._check_for_remaining_args(flag)
        self._shift_arguments()

    def _get_next_flag(self):
        flag = next((flag for flag in Flag if flag.value.equals(self._arguments[0])), None)
        if not flag:
            self._is_valid = False
            self._error_message = "invalid parameter: {0}".format(self._arguments[0])
        return flag

    def _check_for_remaining_args(self, flag):
        if (self._is_valid and not len(self._arguments)):
            self._is_valid = False
            self._error_message = "no {0} specified".format(flag.value.name())

    def _shift_arguments(self):
        self._arguments = self._arguments[1:]
