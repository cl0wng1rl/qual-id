from .helper import Helper
from .validator import Validator
from .parser import Parser

class App:
    @staticmethod
    def run(args):
        helper = Helper(args)
        if helper.is_help():
            return helper.help_message()

        validator = Validator(args)
        if validator.is_valid():
            return Parser().parse(args).message()

        return validator.error_message()
