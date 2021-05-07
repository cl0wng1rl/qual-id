import unittest
from qual_id.category import Category
import random


class TestCategory(unittest.TestCase):

    def test__get_name__returns_category(self):
        self.assertEqual(Category.get_name(), "category")

    def test__get_random_choice__mock_random_choice__returns_empty_string(self):
        random.seed(0)
        fixed_choice = random.choice(Category._values)
        self.assertEqual(Category.random(), fixed_choice)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
