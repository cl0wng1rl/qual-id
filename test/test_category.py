import unittest
from qual_id.category import Category
import unittest.mock as mock
import random


def fixed_choice(lst):
  print('in')
  print(lst)
  return TestCategory.__random_choice


class TestCategory(unittest.TestCase):
  __random_choice = 'random_choice'

  def setUp(self):
    self.category = Category()

  def test__get_values__returns_list_with_empty_string(self):
    self.assertEqual(self.category.get_values(), [''])

  def test__get_random_choice__mock_random_choice__returns_empty_string(self):
    random.seed(0)
    self.assertEqual(self.category.get_random_value(), '')


if __name__ == '__main__':
  unittest.main()
