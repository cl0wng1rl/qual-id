from ..category import Category


class Clothing(Category):
    def get_values(self):
        return [
            "coat",
            "hat",
            "mitten",
            "pants",
            "scarf",
            "shoe",
            "shorts",
            "skirt",
            "sock",
            "suit",
            "tie",
            "tshirt",
            "vest",
        ]
