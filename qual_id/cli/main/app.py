from qual_id.response import Response


class App:
    @staticmethod
    def run(arguments):
        return Response(arguments).get_response_obj()