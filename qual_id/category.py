from random import choice


class Category:
    _name = "category"
    _values = [""]

    @classmethod
    def random(cls):
        return choice(cls._values)

    @classmethod
    def get_name(cls):
        return cls._name
