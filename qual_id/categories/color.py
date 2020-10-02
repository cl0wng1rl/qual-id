from ..category import Category


class Color(Category):
    def get_values(self):
        return [
            "black",
            "red",
            "blue",
            "green",
            "white",
            "grey",
            "yellow",
            "brown",
            "orange",
            "purple",
        ]
