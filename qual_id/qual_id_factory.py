from qual_id.pattern import Pattern


class QualIDFactory:
    @staticmethod
    def get_qual_ids(arguments):
        pattern = Pattern(arguments.get_categories())
        return [pattern.random() for _ in range(arguments.get_number())]
