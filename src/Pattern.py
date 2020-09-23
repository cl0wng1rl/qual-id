from random import choice
from .Animal import Animal
from .Food import Food

class Pattern:
  __random_key = "random"

  __category_map = {
    "animal": Animal(),
    "food": Food(),
  }

  def __init__(self, pattern_string):
    self.__categories = pattern_string.split('-')

  def is_valid(self):
    return self.__categories_length_is_acceptable() and self.__categories_all_exist()
  
  def get_categories(self):
    return [Pattern.__category_map[category] for category in self.__categories]

  def __categories_length_is_acceptable(self):
    return (0 < len(self.__categories) < 6)
  
  def __get_path_from_category(self, category):
    if category == Pattern.__random_key:
      category = Pattern.__random_category()
    return Pattern.__category_map[category]
  
  def __categories_all_exist(self):
    for category in self.__categories:
      path = self.__get_path_from_category(category)
      if not path:
        return False
    return True

  @staticmethod
  def get_category_options(self):
    return Pattern.__category_map.keys()
  
  @staticmethod
  def __random_category(self):
    return choice(Pattern.get_category_options())