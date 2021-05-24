from .argument_parser import ArgumentParser
from .info_arguments import InfoArguments
from .main_arguments import MainArguments
from .command import Command


class Parser:
    @staticmethod
    def parse(arguments):
        parser = ArgumentParser()
        namespace = parser.parse(arguments)
        if namespace.command == Command.MAIN:
            return MainArguments(namespace)
        return InfoArguments(namespace)
