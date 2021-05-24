from .all import All
from .minimal import Minimal
from .neutral import Neutral


class GroupFactory:
    _groups = [All, Minimal, Neutral]
    _group_map = dict((c.name(), c) for c in _groups)

    @staticmethod
    def get(name):
        return GroupFactory._group_map.get(name)

    @staticmethod
    def has(name):
        return name in GroupFactory._group_map

    @staticmethod
    def info():
        return map(lambda c: c.name(), GroupFactory._groups)
