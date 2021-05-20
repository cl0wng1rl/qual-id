class Config:
    PATTERN_KEY = "pattern"
    GROUP_KEY = "group"
    NUMBER_KEY = "number"
    FORMAT_KEY = "format"

    PATTERN_DEFAULT = ""
    GROUP_DEFAULT = "all"
    NUMBER_DEFAULT = 1
    FORMAT_DEFAULT = "json"

    def __init__(self, args):
        self._categories = args.get(self.PATTERN_KEY, self.PATTERN_DEFAULT).split("-")
        self._group = args.get(self.GROUP_KEY, self.GROUP_DEFAULT)
        self._number = int(args.get(self.NUMBER_KEY, self.NUMBER_DEFAULT))
        self._format = args.get(self.FORMAT_KEY, self.FORMAT_DEFAULT)

    def get_categories(self):
        return self._categories

    def get_group(self):
        return self._group

    def get_number(self):
        return self._number

    def get_format(self):
        return self._format
