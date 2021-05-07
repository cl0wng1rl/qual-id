from random import choice


class Collection:
    _instance = None

    _name = ""
    _categories = []
    _category_map = {}

    def __init__(self):
        self._initialise_map()

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def get(cls, category_name):
        return cls._category_map.get(category_name)

    @classmethod
    def invalid(cls, category_names):
        return [name for name in category_names if name not in cls._category_map]

    @classmethod
    def random(cls):
        return choice(cls._categories)

    @classmethod
    def name(cls):
        return cls._name

    @classmethod
    def _initialise_map(cls):
        cls._category_map = dict((c.name(), c) for c in cls._categories)
