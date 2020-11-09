from random import choice
from .categories import *


class Pattern:
    __random_key = "random"

    __category_map = {
        "adjective": Adjective(),
        "animal": Animal(),
        "author": Author(),
        "bird": Bird(),
        "book": Book(),
        "brand": Brand(),
        "capital": Capital(),
        "city": City(),
        "clothing": Clothing(),
        "color": Color(),
        "constellation": Constellation(),
        "country": Country(),
        "cuisine": Cuisine(),
        "currency": Currency(),
        "drink": Drink(),
        "electronic": Electronic(),
        "element": Element(),
        "emotion": Emotion(),
        "festivals": Festivals(),
        "film": Film(),
        "food": Food(),
        "fruit": Fruit(),
        "geography": Geography(),
        "id": RandomId(),
        "instrument": Instrument(),
        "language": Language(),
        "music": Music(),
        "operatingsystem": OperatingSystem(),
        "particle": Particle(),
        "planet": Planet(),
        "pokemon": Pokemon(),
        "profession": Profession(),
        "programminglanguage": ProgrammingLanguage(),
        "scientist": Scientist(),
        "searchengine": SearchEngine(),
        "shape": Shape(),
        "sport": Sport(),
        "state": State(),
        "tea": Tea(),
        "tool": Tool(),
        "utensil": Utensil(),
        "vehicle": Vehicle(),
        "wine": Wine(),
    }

    @staticmethod
    def get_category_options():
        return list(Pattern.__category_map.keys())

    def __init__(self, pattern_string):
        categories_array = [p for p in pattern_string.split("-") if p != ""]
        self.__categories = self.__replace_randoms(categories_array)

    def has_acceptable_categories_length(self):
        return self.__categories_length_is_acceptable()

    def get_nonexistent_categories(self):
        return [
            category
            for category in self.__categories
            if category not in Pattern.__category_map
        ]

    def get_categories(self):
        return [Pattern.__category_map[category] for category in self.__categories]

    def __categories_length_is_acceptable(self):
        return 0 < len(self.__categories) < 6

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
