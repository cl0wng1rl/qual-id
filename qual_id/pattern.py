from random import choice
from qual_id.collection import Collection


class Pattern:
    __random_key = "random"

    def __init__(self, pattern_string, collection):
        self.__categories = [p for p in pattern_string.split("-") if p != ""]
        self._collection = collection
        self.__replace_randoms()

    def get_categories(self):
        return [self._collection.get(category) for category in self.__categories]

    def __valid_number_of_categories(self):
        return 0 < len(self.__categories) < 6

    def __replace_randoms(self):
        self.__categories = [self.__replace_random(x) for x in self.__categories]

    def __replace_random(self, category):
        if category == Pattern.__random_key:
            return self._collection.random()
        return category
