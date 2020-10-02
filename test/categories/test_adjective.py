import unittest
from qual_id.categories.adjective import Adjective
from test.utils.category_helper import CategoryHelper


class TestAdjective(unittest.TestCase):
  def setUp(self):
    self.adjective = Adjective()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.adjective))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
