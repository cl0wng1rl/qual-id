from .arguments import Arguments
from .validator import Validator
from qual_id.qual_id_factory import QualIDFactory
from qual_id.formatter import Formatter


class API:
    @staticmethod
    def run(args):
        args = API._get_defaults(args)
        error_message = Validator.validate(args)
        if error_message:
            return Formatter.format_error(args["format"], error_message)
        arguments = Arguments(args)
        qual_ids = QualIDFactory.get_qual_ids(arguments)
        return Formatter.format_qual_ids(arguments.get_format(), qual_ids)

    @staticmethod
    def _get_defaults(args):
        new_args = {}
        new_args["group"] = API._get_field(args, "group") or "all"
        new_args["categories"] = (
            (API._get_field(args, "pattern"))
            or (API._get_field(args, "categories"))
            or []
        )
        new_args["number"] = API._get_field(args, "number") or 1
        new_args["format"] = API._get_field(args, "format") or "json"
        return new_args

    @staticmethod
    def _get_field(args, field):
        return field in args and args[field]
