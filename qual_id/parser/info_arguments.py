from .command import Command
from qual_id.cli.info.flag import Flag
from qual_id.groups.all import All
from qual_id.groups import GroupFactory

class InfoArguments:
    def __init__(self, namespace):
        self._flag = self._get_flag(namespace)
        if self._flag == Flag.GROUP:
            self._value = namespace.group
        if self._flag == Flag.CATEGORY:
            self._value = namespace.category
    
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
