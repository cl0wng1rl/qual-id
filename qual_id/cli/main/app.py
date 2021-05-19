from qual_id.response import Response
from qual_id.cli.main.helper import Helper
from qual_id.cli.main.validator import Validator
from qual_id.cli.main.parser import Parser


class App:
    @staticmethod
    def run(args):
        helper = Helper(args)
        if helper.is_help():
            return helper.help_messge()

        validator = Validator(args)
        if validator.is_valid():
            return Response(Parser(args).parse()).get_response_obj()

        return validator.error_message()