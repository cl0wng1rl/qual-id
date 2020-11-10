from random import choice
from qual_id.category_map import CategoryMap


class Pattern:
    __random_key = "random"

    @staticmethod
    def get_category_options():
        return CategoryMap.all()

    def __init__(self, pattern_string, category_map=CategoryMap()):
        categories_array = [p for p in pattern_string.split("-") if p != ""]
        self.__categories = self.__replace_randoms(categories_array)
        self.__category_map = category_map

    def has_acceptable_categories_length(self):
        return 0 < len(self.__categories) < 6

    def get_nonexistent_categories(self):
        return CategoryMap.invalid(self.__categories)

    def get_categories(self):
        return [self.__category_map.get(category) for category in self.__categories]

    @staticmethod
    def __random_category():
        return choice(Pattern.get_category_options())

    @staticmethod
    def __replace_randoms(categories):
        return [Pattern.__replace_random(x) for x in categories]

    @staticmethod
    def __replace_random(category):
        return (
            Pattern.__random_category()
            if category == Pattern.__random_key
            else category
        )
