from random import choice


class Category:
    _name = ""
    _values = [""]

    @classmethod
    def random(cls):
        return choice(cls._values)

    @classmethod
    def name(cls):
        return cls._name

    @classmethod
    def info(cls):
        return cls._values
