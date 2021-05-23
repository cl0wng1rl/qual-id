from qual_id.parser.command import Command
from qual_id.parser.parser import Parser
from qual_id.response import Response
from qual_id.info import App as InfoApp

class CLI:
    @staticmethod
    def run(args):
        arguments = Parser.parse(args[1:])
        if arguments.get_command() == Command.INFO:
            return InfoApp.run(arguments)
        return Response(arguments).get_response_obj()
