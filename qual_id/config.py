class Config:
    PATTERN_KEY = "pattern"
    COLLECTION_KEY = "collection"
    NUMBER_KEY = "number"
    FORMAT_KEY = "format"

    PATTERN_DEFAULT = ""
    COLLECTION_DEFAULT = "all"
    NUMBER_DEFAULT = 1
    FORMAT_DEFAULT = "json"

    def __init__(self, args):
        self._categories = args.get(self.PATTERN_KEY, self.PATTERN_DEFAULT).split("-")
        self._collection = args.get(self.COLLECTION_KEY, self.COLLECTION_DEFAULT)
        self._number = int(args.get(self.NUMBER_KEY, self.NUMBER_DEFAULT))
        self._format = args.get(self.FORMAT_KEY, self.FORMAT_DEFAULT)

    def get_categories(self):
        return self._categories

    def get_collection(self):
        return self._collection

    def get_number(self):
        return self._number

    def get_format(self):
        return self._format
