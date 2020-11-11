import unittest
from qual_id.categories.city import City
from test.unit.utils.category_helper import CategoryHelper


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.city)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
