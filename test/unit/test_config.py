import unittest
from qual_id.config import Config


class TestConfig(unittest.TestCase):
    ARGS = {
        "pattern": "TEST-PATTERN",
        "collection": "TEST COLLECTION",
        "number": 1,
        "format": "TEST FORMAT",
    }

    def test__get_categories__returns_correct_pattern(self):
        config = Config(self.ARGS)
        expected_pattern = self.ARGS.get("pattern").split("-")
        self.assertEqual(config.get_categories(), expected_pattern)

    def test__get_collection__returns_correct_collection(self):
        config = Config(self.ARGS)
        expected_collection = self.ARGS.get("collection")
        self.assertEqual(config.get_collection(), expected_collection)

    def test__get_number__returns_correct_number(self):
        config = Config(self.ARGS)
        expected_number = self.ARGS.get("number")
        self.assertEqual(config.get_number(), expected_number)

    def test__get_format__returns_correct_format(self):
        config = Config(self.ARGS)
        expected_format = self.ARGS.get("format")
        self.assertEqual(config.get_format(), expected_format)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
