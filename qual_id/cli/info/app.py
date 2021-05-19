from .validator import Validator
from .parser import Parser

class App:
    @staticmethod
    def run(args):
        validator = Validator(args)
        if validator.is_valid():
            return Parser().parse(args).message()
        return validator.error_message()
