from ..category import Category


class Planet(Category):
    def get_values(self):
        return [
            'mercury',
            'venus',
            'earth',
            'mars',
            'jupyter',
            'saturn',
            'uranus',
            'neptune'
        ]
