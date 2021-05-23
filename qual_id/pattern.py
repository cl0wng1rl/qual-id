class Pattern:
    def __init__(self, categories):
        self._categories = categories

    def random(self):
        return "-".join([category.random() for category in self._categories])
