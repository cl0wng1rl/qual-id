from random import choice


class Group:
    _name = ""
    _categories = []
    _category_map = {}

    @classmethod
    def get(cls, category_name):
        return cls._get_category_map().get(category_name)

    @classmethod
    def invalid(cls, category_names):
        return [name for name in category_names if name not in cls._get_category_map()]

    @classmethod
    def random(cls):
        return choice(cls._categories)

    @classmethod
    def name(cls):
        return cls._name

    @classmethod
    def info(cls):
        return list(map(lambda c: c.name(), cls._categories))

    @classmethod
    def _get_category_map(cls):
        if not cls._category_map:
            cls._category_map = dict((c.name(), c) for c in cls._categories)
        return cls._category_map
