import unittest
from qual_id.categories.electronic import Electronic
from test.utils.category_helper import CategoryHelper


class TestAnimal(unittest.TestCase):
  def setUp(self):
    self.electronic = Electronic()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.electronic))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()