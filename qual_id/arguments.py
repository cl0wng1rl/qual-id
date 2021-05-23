from qual_id.groups import GroupFactory

class Arguments:
    def __init__(self, args_object):
        self._group = self._get_group_from_name(args_object["group"])
        self._categories = self._get_list_of_categories(args_object["categories"])
        self._format = args_object["format"]
        self._number = args_object["number"]

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
