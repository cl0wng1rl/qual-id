import unittest
from qual_id.category import Category
import random


class TestCategory(unittest.TestCase):
  def setUp(self):
    self.category = Category()

  def test__get_values__returns_list_with_empty_string(self):
    self.assertEqual(self.category.get_values(), [''])

  def test__get_random_choice__mock_random_choice__returns_empty_string(self):
    random.seed(0)
    fixed_choice = self.__get_random_choice_from_values()
    self.assertEqual(self.category.get_random_value(), fixed_choice)

  def __get_random_choice_from_values(self):
    return random.choice(self.category.get_values())


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
