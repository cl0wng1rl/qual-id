import unittest
from qual_id.config import Config


class TestConfig(unittest.TestCase):
    """Unit Tests for Config"""

    ARGS = {
        "pattern": "TEST-PATTERN",
        "group": "TEST GROUP",
        "number": 1,
        "format": "TEST FORMAT",
    }

    def test__get_categories__correct_pattern(self):
        """Config -> get_categories"""
        config = Config(self.ARGS)
        expected_pattern = self.ARGS.get("pattern").split("-")
        self.assertEqual(config.get_categories(), expected_pattern)

    def test__get_group__correct_group(self):
        """Config -> get_categories"""
        config = Config(self.ARGS)
        expected_group = self.ARGS.get("group")
        self.assertEqual(config.get_group(), expected_group)

    def test__get_number__correct_number(self):
        """Config -> get_categories"""
        config = Config(self.ARGS)
        expected_number = self.ARGS.get("number")
        self.assertEqual(config.get_number(), expected_number)

    def test__get_format__correct_format(self):
        """Config -> get_categories"""
        config = Config(self.ARGS)
        expected_format = self.ARGS.get("format")
        self.assertEqual(config.get_format(), expected_format)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
