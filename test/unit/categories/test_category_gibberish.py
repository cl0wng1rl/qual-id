import unittest
from qual_id.categories.gibberish import Gibberish
import random


class TestGibberish(unittest.TestCase):
    """Unit Tests for Gibberish"""

    def setUp(self):
        random.seed(1)

    def test__random__is_random_id(self):
        """Gibberish -> random"""
        gibberish = Gibberish()
        result = gibberish.random()
        expected_string = "sejaty"

        self.assertEqual(expected_string, result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
