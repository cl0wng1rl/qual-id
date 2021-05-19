class Helper:
    FLAGS = ["--help", "-h"]
    HELP_MESSAGE_LINES = []

    def __init__(self, arguments):
      self._is_help = any(h in arguments for h in Helper.FLAGS)

    def is_help(self):
        return self._is_help

    @classmethod
    def help_messge(cls):
        return "\n".join(cls.HELP_MESSAGE_LINES)
