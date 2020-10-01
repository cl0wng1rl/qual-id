class CategoryHelper:
  __disallowed_characters = [' ', '-', '_']

  @staticmethod
  def get_values_is_valid(category):
    returns_a_list = CategoryHelper.get_values_returns_a_list(category)
    does_not_contain_invalid_string = CategoryHelper.get_values_does_not_contain_invalid_string(category)
    does_not_contain_repeats = CategoryHelper.get_values_does_not_contain_repeats(category)
    return returns_a_list and does_not_contain_invalid_string and does_not_contain_repeats

  @staticmethod
  def get_values_returns_a_list(category):
    is_list = isinstance(category.get_values(), list)
    is_empty = len(category.get_values()) == 0
    return is_list and not is_empty

  @staticmethod
  def get_values_does_not_contain_invalid_string(category):
    return not any([CategoryHelper.string_contains_disallowed_character(value) for value in category.get_values()])

  @staticmethod
  def get_values_does_not_contain_repeats(category):
    return len(set(category.get_values())) == len(category.get_values())

  @staticmethod
  def string_contains_disallowed_character(str):
    return any([c in str for c in CategoryHelper.__disallowed_characters])
