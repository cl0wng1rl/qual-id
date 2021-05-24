import unittest
from qual_id.formatter import Formatter
from unittest.mock import Mock, call, patch


class TestFormatter(unittest.TestCase):
    """Unit Tests for Formatter"""

    CSV = "csv"
    JSON = "json"
    QUAL_IDS = ["qual_id1", "qual_id2", "qual_id3"]
    ERROR_MESSAGE = "error message"

    def test__format_qual_ids__csv_format__correct_string(self):
        """Formatter -> format_qual_ids - csv format"""
        result = Formatter.format_qual_ids(self.CSV, self.QUAL_IDS)
        excepted_result = ",".join(self.QUAL_IDS)
        self.assertEqual(excepted_result, result)

    def test__format_qual_ids__json_format__correct_object(self):
        """Formatter -> format_qual_ids - json format"""
        result = Formatter.format_qual_ids(self.JSON, self.QUAL_IDS)
        excepted_result = {"data": self.QUAL_IDS}
        self.assertEqual(excepted_result, result)

    def test__format_error__csv_format__correct_string(self):
        """Formatter -> format_error - csv format"""
        result = Formatter.format_error(self.CSV, self.ERROR_MESSAGE)
        excepted_result = self.ERROR_MESSAGE
        self.assertEqual(excepted_result, result)

    def test__format_error__json_format__correct_object(self):
        """Formatter -> format_error - json format"""
        result = Formatter.format_error(self.JSON, self.ERROR_MESSAGE)
        excepted_result = {"error": self.ERROR_MESSAGE}
        self.assertEqual(excepted_result, result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
