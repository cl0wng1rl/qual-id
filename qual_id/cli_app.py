from qual_id.response import Response
from qual_id.cli_parser import CliParser


class CliApp:
    @staticmethod
    def run(args):
        parser = CliParser(args)
        config = parser.parse()
        return Response(config).get_response_obj()
