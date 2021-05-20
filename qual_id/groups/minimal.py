from ..categories import *
from .group import Group

class Minimal(Group):
    _name = "minimal"
    _categories = [
        Adjective,
        Animal,
        Bird,
        Cake,
        Color,
        Food,
        Fruit,
        Geography,
        Instrument,
        Planet,
        Tea,
        Vehicle,
    ]
