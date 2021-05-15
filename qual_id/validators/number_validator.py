class NumberValidator:
    def __init__(self, number):
        self._number = number
        self._is_valid = None
        self._error_message = None

    def validate(self):
        self._is_valid = isinstance(self._number, int)
        if not self._is_valid:
            self._error_message = "'number' argument is not an integer"

    def is_valid(self):
        return self._is_valid

    def error_message(self):
        return self._error_message
