import unittest
from qual_id.categories.particle import Particle
from test.utils.category_helper import CategoryHelper


class TestParticle(unittest.TestCase):
    def setUp(self):
        self.particle = Particle()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.particle)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
