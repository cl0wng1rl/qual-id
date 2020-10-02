from ..category import Category


class Shape(Category):
    def get_values(self):
        return [
            "oval",
            "circle",
            "triangle",
            "square",
            "rectangle",
            "hexagon",
            "pyramid",
            "pentagon",
            "cube",
            "star",
            "diamond",
        ]
