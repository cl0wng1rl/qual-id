import unittest
from qual_id.cli.parser import Parser


class TestParser(unittest.TestCase):
    COMMAND_NAME = "qid"
    PATTERN_FLAG = "--pattern"
    PATTERN = "category1-category2"
    FORMAT_FLAG = "--format"
    FORMAT = "format"
    NUMBER_FLAG = "--number"
    NUMBER = "3"
    COLLECTION_FLAG = "--collection"
    COLLECTION = "collection"

    EXPECTED_CONFIG = {
        "pattern": PATTERN,
        "collection": COLLECTION,
        "format": FORMAT,
        "number": NUMBER,
    }

    def test__parse__args__correct_config(self):
        parser = Parser(self.get_valid_args())
        self.assertDictEqual(self.EXPECTED_CONFIG, parser.parse())

    def get_valid_args(self):
        return [
            self.COMMAND_NAME,
            self.PATTERN_FLAG,
            self.PATTERN,
            self.FORMAT_FLAG,
            self.FORMAT,
            self.NUMBER_FLAG,
            self.NUMBER,
            self.COLLECTION_FLAG,
            self.COLLECTION,
        ]


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
