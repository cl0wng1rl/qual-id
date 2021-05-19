from .main import App as App
from .info import App as InfoApp

class CLI:
    INFO_LONG = "--info"
    INFO_SHORT = "-i"
    
    @staticmethod
    def run(arguments):
        if CLI.INFO_LONG in arguments or CLI.INFO_SHORT in arguments:
            return InfoApp.run(arguments)
        return App.run(arguments)
