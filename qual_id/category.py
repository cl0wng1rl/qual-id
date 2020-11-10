from random import choice


class Category:
    def random(self):
        return choice(self.get_values())

    def get_values(self):
        return [""]
