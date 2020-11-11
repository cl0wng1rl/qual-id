from qual_id.pattern import Pattern
from qual_id.category_map_factory import CategoryMapFactory


class Validator:
    def __init__(self, pattern_string, collection_string):
        self.__pattern_string = pattern_string
        self.__collection_string = collection_string
        self.__pattern = None

    def error(self):
        if not CategoryMapFactory.has(self.__collection_string):
            return "invalid collection: %s" % (self.__collection_string)
        category_map = CategoryMapFactory.get(self.__collection_string)
        self.__pattern = Pattern(self.__pattern_string, category_map)
        return self.__pattern.error()

    def valid_pattern(self):
        return self.__pattern
