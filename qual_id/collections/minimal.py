from ..categories import *
from .collection import Collection

class Minimal(Collection):
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
