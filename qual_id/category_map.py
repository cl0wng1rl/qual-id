from qual_id.category import Category
from qual_id.categories import *


class CategoryMap:
    def __init__(self, keys=[]):
        self.__map = self.__construct_map(keys) if keys else CategoryMap.__all

    def get(self, key):
        return self.__map[key]

    def categories(self):
        return [key for key in self.__map]

    def invalid(self, keys):
        return [key for key in keys if key not in self.__map]

    def __construct_map(self, keys):
        category_map = {}
        for key in keys:
            category_map[key] = CategoryMap.__all[key]
        return category_map

    __all = {
        "adjective": Adjective(),
        "animal": Animal(),
        "author": Author(),
        "bird": Bird(),
        "book": Book(),
        "brand": Brand(),
        "cake": Cake(),
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
        "flower": Flower(),
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