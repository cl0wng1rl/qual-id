from ..category import Category


class Shape(Category):
    def get_values(self):
        return [
            "circle",
            "cube",
            "diamond",
            "hexagon",
            "oval",
            "pentagon",
            "pyramid",
            "rectangle",
            "square",
            "star",
            "triangle",
        ]
