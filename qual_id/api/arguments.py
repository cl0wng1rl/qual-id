from qual_id.groups import GroupFactory

class Arguments:
    def __init__(self, args):
        self._group = self._get_group_from_name(args["group"] or "all")
        self._categories = self._get_list_of_categories((args["categories"] or "").split("-"))
        self._format = args["format"] or "json"
        self._number = int(args["number"]) or 1

    def get_categories(self):
        return self._categories

    def get_group(self):
        return self._group

    def get_format(self):
        return self._format

    def get_number(self):
        return self._number

    def _get_group_from_name(self, group_name):
        return GroupFactory.get(group_name)

    def _get_list_of_categories(self, category_names):
        return list(self._group.get(name) for name in category_names)
