import unittest
from qual_id.categories.planet import Planet
from test.unit.utils.category_helper import CategoryHelper


class TestPlanet(unittest.TestCase):
    def setUp(self):
        self.planet = Planet()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.planet)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
