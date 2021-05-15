from qual_id.pattern import Pattern
from qual_id.collection_factory import CollectionFactory


class Validator:
    def __init__(self, pattern_string, collection_string):
        self.__pattern_string = pattern_string
        self.__collection_string = collection_string
        self.__pattern = None

    def error(self):
        if not CollectionFactory.has(self.__collection_string):
            return "invalid collection: %s" % (self.__collection_string)
        collection = CollectionFactory.get(self.__collection_string)
        return Pattern(self.__pattern_string, collection).error()
