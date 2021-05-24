from .command import Command
from qual_id.info.flag import Flag


class InfoArguments:
    def __init__(self, namespace):
        self._flag = self._get_flag(namespace)
        self._value = self._get_value(namespace)

    def get_flag(self):
        return self._flag

    def get_value(self):
        return self._value

    def get_command(self):
        return Command.INFO

    def _get_flag(self, namespace):
        if namespace.group != False:
            return Flag.GROUP
        if namespace.category != False:
            return Flag.CATEGORY
        return Flag.FORMAT

    def _get_value(self, namespace):
        if self._flag == Flag.GROUP:
            return namespace.group
        if self._flag == Flag.CATEGORY:
            return namespace.category
