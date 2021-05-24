from .parser import Command
from .parser import Parser
from qual_id.qual_id_factory import QualIDFactory
from qual_id.formatter import Formatter
from qual_id.info import App as InfoApp


class CLI:
    @staticmethod
    def run(args):
        arguments = Parser.parse(args[1:])
        if arguments.get_command() == Command.INFO:
            return InfoApp.run(arguments)
        qual_ids = QualIDFactory.get_qual_ids(arguments)
        return Formatter.format_qual_ids(arguments.get_format(), qual_ids)
