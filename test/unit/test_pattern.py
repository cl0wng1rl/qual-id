import unittest
from qual_id.pattern import Pattern
from unittest.mock import Mock, call, patch


class TestPattern(unittest.TestCase):
    """Unit Tests for Pattern"""

    VALUES = ["first", "second", "third"]

    def setUp(self):
        self.categories = self.mock_categories()

    def test__random__pattern__correct_qual_id(self):
        """Pattern -> random"""
        result = Pattern(self.categories).random()
        self.assertEqual("-".join(self.VALUES), result)

    def mock_categories(self):
        return [
            self.mock_category(self.VALUES[0]),
            self.mock_category(self.VALUES[1]),
            self.mock_category(self.VALUES[2]),
        ]

    def mock_category(self, random):
        mock = Mock()
        mock.random.return_value = random
        return mock


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
