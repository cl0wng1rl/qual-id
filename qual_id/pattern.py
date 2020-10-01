from random import choice
from .categories.animal import Animal
from .categories.color import Color
from .categories.drink import Drink
from .categories.food import Food
from .categories.game import Game
from .categories.geography import Geography
from .categories.instrument import Instrument
from .categories.tool import Tool


class Pattern:
  __random_key = "random"

  __category_map = {
      "animal": Animal(),
      "color": Color(),
      "drink": Drink(),
      "food": Food(),
      "game":Game(),
      "geography":Geography(),
      "instrument": Instrument(),
      "tool": Tool()

  }

  @staticmethod
  def get_category_options():
    return list(Pattern.__category_map.keys())

  def __init__(self, pattern_string):
    self.__categories = self.__replace_randoms(pattern_string.split('-'))

  def is_valid(self):
    return self.__categories_length_is_acceptable() and self.__categories_all_exist()

  def get_categories(self):
    return [Pattern.__category_map[category] for category in self.__categories]

  def __categories_length_is_acceptable(self):
    return (0 < len(self.__categories) < 6)

  def __categories_all_exist(self):
    return all([(category in Pattern.__category_map) for category in self.__categories])

  @staticmethod
  def __random_category():
    return choice(Pattern.get_category_options())

  @staticmethod
  def __replace_randoms(categories):
    return [Pattern.__replace_random(x) for x in categories]

  @staticmethod
  def __replace_random(category):
    return Pattern.__random_category() if category == Pattern.__random_key else category
