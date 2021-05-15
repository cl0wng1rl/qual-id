class FormatValidator:
    _VALID_FORMATS = ["json", "csv"]

    def __init__(self, result_format):
        self._format = result_format
        self._is_valid = None
        self._error_message = None

    def validate(self):
        self._is_valid = self._format in self._VALID_FORMATS
        if not self._is_valid:
            self._error_message = "'format' argument must be " + self._join_formats()

    def is_valid(self):
        return self._is_valid

    def error_message(self):
        return self._error_message

    @staticmethod
    def _join_formats():
        first_formats = ", ".join(FormatValidator._VALID_FORMATS[:-1])
        return " or ".join([first_formats, FormatValidator._VALID_FORMATS[-1]])
