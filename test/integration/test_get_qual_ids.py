import unittest
from qual_id.response import Response
import random


class TestGetQualIDsIntegration(unittest.TestCase):
    def setUp(self):
        random.seed(1)
        self.args = {
            "pattern": "fruit-geography",
            "collection": "all",
            "number": 3,
            "format": "json",
        }

    def test__get_qual_ids__returns_qual_id(self):
        response = Response(self.args)
        response_obj = response.get_response_obj()
        qual_ids = response_obj["data"]
        expected_qual_ids = ["coconut-sky", "blackberry-hill", "clementine-plateau"]
        self.assertEqual(expected_qual_ids, qual_ids)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
