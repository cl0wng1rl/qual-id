import unittest
from qual_id.categories.animal import Animal
from test.unit.utils.category_helper import CategoryHelper


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal = Animal()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.animal)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
