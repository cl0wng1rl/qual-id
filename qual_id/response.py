from qual_id.config import Config
from qual_id.validator import Validator
from qual_id.collection_factory import CollectionFactory
from qual_id.pattern import Pattern


class Response:
    def __init__(self, args):
        self.__pattern = args.get("pattern", "")
        self.__collection = args.get("collection", "all")
        self.__number = int(args.get("number", 1))
        self.__format = args.get("format", "json")
        self._config = Config(args)

    def get_response_obj(self):
        response_obj = {}
        validator = Validator(self._config)
        validator.validate()

        if validator.is_valid():
            response_obj["data"] = self.get_qual_ids()
        else:
            response_obj["error"] = validator.error_message()
        return self.__format_response(response_obj)

    def get_qual_ids(self):
        collection = CollectionFactory.get(self.__collection)
        pattern = Pattern(self.__pattern, collection)
        return [self.__get_qual_id(pattern) for _ in range(self.__number)]

    def __format_response(self, response_obj):
        if self.__format == "csv":
            return self.__data_or_error(response_obj)
        return response_obj

    def __data_or_error(self, response_obj):
        if "data" in response_obj:
            return ",".join(response_obj["data"])
        return response_obj["error"]

    def __get_qual_id(self, pattern):
        return "-".join([category.random() for category in pattern.get_categories()])