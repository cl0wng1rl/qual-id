from .group_validator import GroupValidator
from .format_validator import FormatValidator
from .number_validator import NumberValidator
from .pattern_validator import PatternValidator


class Validator:
    def __init__(self, config):
        self._validators = Validator._get_validators(config)
        self._is_valid = None
        self._error_message = None

    def validate(self):
        index = 0
        while (index < len(self._validators)) and (self._is_valid != False):
            self._validate(self._validators[index])
            index += 1

    def is_valid(self):
        return self._is_valid

    def error_message(self):
        return self._error_message

    def _validate(self, validator):
        validator.validate()
        self._error_message = validator.error_message()
        self._is_valid = validator.is_valid()

    @staticmethod
    def _get_validators(config):
        return [
            GroupValidator(config.get_group()),
            PatternValidator(config.get_group(), config.get_categories()),
            FormatValidator(config.get_format()),
            NumberValidator(config.get_number()),
        ]
