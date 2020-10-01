import unittest
from qual_id.categories.planet import Planet
from test.utils.category_helper import CategoryHelper


class TestPlanet(unittest.TestCase):
  def setUp(self):
    self.planet = Planet()

  def test__get_values__is_valid(self):
    self.assertTrue(CategoryHelper.get_values_is_valid(self.planet))


if __name__ == '__main__':  # pragma: no cover
  unittest.main()
