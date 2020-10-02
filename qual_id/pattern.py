from random import choice
from .categories.animal import Animal
from .categories.color import Color
from .categories.country import Country
from .categories.shape import Shape
from .categories.film import Film
from .categories.book import Book
from .categories.drink import Drink
from .categories.electronic import Electronic
from .categories.emotion import Emotion
from .categories.food import Food
from .categories.game import Game
from .categories.geography import Geography
from .categories.instrument import Instrument
from .categories.music import Music
from .categories.tool import Tool
from .categories.searchengine import SearchEngine
from .categories.adjective import Adjective
from .categories.city import City
from .categories.planet import Planet
from .categories.language import Language
from .categories.vehicle import Vehicle

class Pattern:
  __random_key = "random"

  __category_map = {
      "animal": Animal(),
      "color": Color(),
      "country": Country(),
      "shape": Shape(),
      "film": Film(),
      "book": Book(),
      "drink": Drink(),
      "electronic":Electronic(),
      "emotion": Emotion(),
      "food": Food(),
      "game":Game(),
      "geography":Geography(),
      "instrument": Instrument(),
      "music": Music(),
      "tool": Tool(),
      "searchengine": SearchEngine(),
      "adjective": Adjective(),
      "city": City(),
      "planet": Planet(),
      "language": Language(),
      "vehicle": Vehicle()
  }

  @staticmethod
  def get_category_options():
    return list(Pattern.__category_map.keys())

  def __init__(self, pattern_string):
    categories_array = [p for p in pattern_string.split('-') if p != ""]
    self.__categories = self.__replace_randoms(categories_array)

  def has_acceptable_categories_length(self):
    return self.__categories_length_is_acceptable()

  def get_nonexistent_categories(self):
    return [category for category in self.__categories if category not in Pattern.__category_map]

  def get_categories(self):
    return [Pattern.__category_map[category] for category in self.__categories]

  def __categories_length_is_acceptable(self):
    return (0 < len(self.__categories) < 6)

  @staticmethod
  def __random_category():
    return choice(Pattern.get_category_options())

  @staticmethod
  def __replace_randoms(categories):
    return [Pattern.__replace_random(x) for x in categories]

  @staticmethod
  def __replace_random(category):
    return Pattern.__random_category() if category == Pattern.__random_key else category
