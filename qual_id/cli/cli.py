from qual_id.parser.command import Command
from qual_id.parser.parser import Parser
from .main import App as App
from .info import App as InfoApp

class CLI:
    @staticmethod
    def run(args):
        arguments = Parser.parse(args[1:])
        if arguments.get_command() == Command.INFO:
            return InfoApp.run(arguments)
        return App.run(arguments)
