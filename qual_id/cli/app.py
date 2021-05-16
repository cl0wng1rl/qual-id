from qual_id.response import Response
from qual_id.cli.parser import Parser


class App:
    @staticmethod
    def run(args):
        parser = Parser(args)
        config = parser.parse()
        return Response(config).get_response_obj()
