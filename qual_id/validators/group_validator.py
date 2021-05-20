from qual_id.groups import GroupFactory


class GroupValidator:
    def __init__(self, group):
        self._group = group
        self._is_valid = None
        self._error_message = None

    def validate(self):
        self._is_valid = GroupFactory.has(self._group)
        if not self._is_valid:
            self._error_message = "invalid group: %s" % (self._group)

    def is_valid(self):
        return self._is_valid

    def error_message(self):
        return self._error_message
