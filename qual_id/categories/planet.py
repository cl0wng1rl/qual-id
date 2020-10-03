from ..category import Category


class Planet(Category):
    def get_values(self):
        return [
            "earth",
            "jupiter",
            "mars",
            "mercury",
            "neptune",
            "saturn",
            "uranus",
            "venus",
        ]
