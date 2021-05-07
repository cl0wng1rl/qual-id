import unittest
from qual_id.categories.randomid import RandomId
import random


class TestRandomId(unittest.TestCase):
    def setUp(self):
        random.seed(1)

    def test__random__is_random_id(self):
        randomId = RandomId()
        result = randomId.random()
        expected_id = "ieqh524yng"

        self.assertEqual(expected_id, result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
