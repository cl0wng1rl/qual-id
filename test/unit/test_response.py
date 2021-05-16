import unittest
from qual_id.pattern import Pattern
from qual_id.collection import Collection
from qual_id.collection_factory import CollectionFactory
from qual_id.validator import Validator
from qual_id.response import Response
from unittest.mock import Mock, call, patch


class TestResponse(unittest.TestCase):
    CSV = "csv"
    QUAL_ID = "qual_id"
    ERROR_MESSAGE = "error message"

    def setUp(self):
        self.args = {
            "pattern": "pattern",
            "collection": "all",
            "number": 2,
            "format": "json",
        }

    @patch.object(CollectionFactory, "get")
    @patch.object(Validator, "is_valid")
    @patch.object(Validator, "error_message")
    @patch.object(Pattern, "random")
    def test__get_response_obj__valid_args__returns_correct_object(
        self, mock_pattern_random, mock_validator_error_message, mock_validator_is_valid, mock_get
    ):
        mock_get.return_value = self.get_mock_collection()
        mock_validator_is_valid.return_value = True
        mock_validator_error_message.return_value = None
        mock_pattern_random.return_value = "-".join([TestResponse.QUAL_ID] * 2)
        response = Response(self.args)

        expected = {"data": self.dual_double_qual_id_array()}
        self.assertEqual(expected, response.get_response_obj())

    @patch.object(CollectionFactory, "get")
    @patch.object(Validator, "is_valid")
    @patch.object(Validator, "error_message")
    @patch.object(Pattern, "random")
    def test__get_response_obj__valid_args_with_csv_format__returns_correct_object(
        self, mock_pattern_random, mock_validator_error_message, mock_validator_is_valid, mock_get
    ):
        mock_get.return_value = self.get_mock_collection()
        mock_validator_is_valid.return_value = True
        mock_validator_error_message.return_value = None
        mock_pattern_random.return_value = "-".join([TestResponse.QUAL_ID] * 2)

        self.args["format"] = TestResponse.CSV
        response = Response(self.args)

        expected = self.dual_double_qual_id_string()
        self.assertEqual(expected, response.get_response_obj())

    @patch.object(CollectionFactory, "get")
    @patch.object(Validator, "is_valid")
    @patch.object(Validator, "error_message")
    @patch.object(Pattern, "random")
    def test__get_response_obj__invalid_args__returns_correct_object(
        self, mock_pattern_random, mock_validator_error_message, mock_validator_is_valid, mock_get
    ):
        mock_get.return_value = self.get_mock_collection()
        mock_validator_is_valid.return_value = False
        mock_validator_error_message.return_value = TestResponse.ERROR_MESSAGE
        mock_pattern_random.return_value = "-".join([TestResponse.QUAL_ID] * 2)

        response = Response(self.args)

        expected = {"error": TestResponse.ERROR_MESSAGE}
        self.assertEqual(expected, response.get_response_obj())

    @patch.object(CollectionFactory, "get")
    @patch.object(Validator, "is_valid")
    @patch.object(Validator, "error_message")
    @patch.object(Pattern, "random")
    def test__get_response_obj__invalid_args_with_csv_format__returns_correct_object(
        self, mock_pattern_random, mock_validator_error_message, mock_validator_is_valid, mock_get
    ):
        mock_get.return_value = self.get_mock_collection()
        mock_validator_is_valid.return_value = False
        mock_validator_error_message.return_value = TestResponse.ERROR_MESSAGE
        mock_pattern_random.return_value = "-".join([TestResponse.QUAL_ID] * 2)

        self.args["format"] = TestResponse.CSV
        response = Response(self.args)

        self.assertEqual(TestResponse.ERROR_MESSAGE, response.get_response_obj())

    @patch.object(CollectionFactory, "get")
    @patch.object(Validator, "is_valid")
    @patch.object(Pattern, "random")
    def test__get_qual_ids__valid_args__returns_correct_object(
        self, mock_pattern_random, mock_validator_is_valid, mock_get
    ):
        mock_get.return_value = self.get_mock_collection()
        mock_validator_is_valid.return_value = True
        mock_pattern_random.return_value = "-".join([TestResponse.QUAL_ID] * 2)

        response = Response(self.args)

        self.assertEqual(self.dual_double_qual_id_array(), response.get_qual_ids())

    def get_mock_collection(self):
        mock = Mock()
        mock.get.return_value = self.mock_category()
        mock.invalid.return_value = []
        return mock

    def mock_category(self):
        mock = Mock()
        mock.random.return_value = TestResponse.QUAL_ID
        return mock

    def dual_double_qual_id_string(self):
        return "{0},{0}".format(self.double_qual_id())

    def dual_double_qual_id_array(self):
        return [self.double_qual_id()] * 2

    def double_qual_id(self):
        return "{0}-{0}".format(TestResponse.QUAL_ID)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
