from random import choice

from .categories.adjective import Adjective
from .categories.animal import Animal
from .categories.author import Author
from .categories.bird import Bird
from .categories.book import Book
from .categories.brand import Brand
from .categories.celebrity import Celebrity
from .categories.city import City
from .categories.clothing import Clothing
from .categories.color import Color
from .categories.company import Company
from .categories.constellation import Constellation
from .categories.country import Country
from .categories.cuisine import Cuisine
from .categories.currency import Currency
from .categories.drink import Drink
from .categories.electronic import Electronic
from .categories.element import Element
from .categories.emotion import Emotion
from .categories.festivals import Festivals
from .categories.film import Film
from .categories.food import Food
from .categories.fruit import Fruit
from .categories.game import Game
from .categories.geography import Geography
from .categories.instrument import Instrument
from .categories.language import Language
from .categories.music import Music
from .categories.operatingsystem import OperatingSystem
from .categories.particle import Particle
from .categories.planet import Planet
from .categories.pokemon import Pokemon
from .categories.profession import Profession
from .categories.programminglanguage import ProgrammingLanguage
from .categories.scientist import Scientist
from .categories.searchengine import SearchEngine
from .categories.shape import Shape
from .categories.sports import Sports
from .categories.state import State
from .categories.tea import Tea
from .categories.tool import Tool
from .categories.utensil import Utensil
from .categories.vehicle import Vehicle


class Pattern:
    __random_key = "random"

    __category_map = {
        "adjective": Adjective(),
        "animal": Animal(),
        "author": Author(),
        "bird": Bird(),
        "book": Book(),
        "brand": Brand(),
        "celebrity": Celebrity(),
        "city": City(),
        "clothing": Clothing(),
        "color": Color(),
        "company": Company(),
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
        "game": Game(),
        "geography": Geography(),
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
        "sports": Sports(),
        "state": State(),
        "tea": Tea(),
        "tool": Tool(),
        "utensil": Utensil(),
        "vehicle": Vehicle(),
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
