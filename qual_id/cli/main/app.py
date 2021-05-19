from qual_id.response import Response
from qual_id.cli.main.parser import Parser
from qual_id.cli.main.validator import Validator


class App:
    @staticmethod
    def run(args):
        App._validate_arguments(args)
        return App._get_response(args)
    
    @staticmethod
    def _validate_arguments(args):
        validator = Validator(args)
        if validator.is_help():
            App._print_help()
        if not validator.is_valid():
            App._print_error(validator)

    @staticmethod
    def _get_response(args):
        parser = Parser(args)
        config = parser.parse()
        return Response(config).get_response_obj()

    @staticmethod
    def _print_help():
        print(" ")
        print("Qual ID - get qualitative IDs")
        print(" ")
        print("qual-id [options]")
        print(" ")
        print("options:")
        print("-h, --help                show brief help")
        print("-p, --pattern             specify the pattern of the qual IDs")
        print("-c, --collection          specify which collection to use")
        print("-n, --number              specify how many qual IDs to receive")
        print("-f, --format              specify the format of the qual IDs")
        print(" ")
        exit()
    
    @staticmethod
    def _print_error(validator):
        print(validator.error_message())
        exit()