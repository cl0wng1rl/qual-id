from qual_id.pattern import Pattern


class Response:
    def __init__(self, arguments):
        self._arguments = arguments

    def get_response_obj(self):
        response_obj = {}
        response_obj["data"] = self.get_qual_ids()
        return self.__format_response(response_obj)

    def get_qual_ids(self):
        pattern = Pattern(self._arguments.get_categories())
        return [pattern.random() for _ in range(self._arguments.get_number())]

    def __format_response(self, response_obj):
        if self._arguments.get_format() == "csv":
            return self.__data_or_error(response_obj)
        return response_obj

    def __data_or_error(self, response_obj):
        if "data" in response_obj:
            return ",".join(response_obj["data"])
        return response_obj["error"]
