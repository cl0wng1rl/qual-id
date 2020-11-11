import unittest
from qual_id.categories.profession import Profession
from test.unit.utils.category_helper import CategoryHelper


class TestProfession(unittest.TestCase):
    def setUp(self):
        self.profession = Profession()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.profession)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
