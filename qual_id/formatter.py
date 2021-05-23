class Formatter:
    @staticmethod
    def format_qual_ids(format_string, qual_ids):
        if format_string == 'csv':
            return ','.join(qual_ids)
        return {"data": qual_ids}

    @staticmethod
    def format_error(format_string, error_message):
        if format_string == 'csv':
            return error_message
        return {"error": error_message}