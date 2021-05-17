class Pattern:
    __random_key = "random"

    def __init__(self, category_names, collection):
        self._collection = collection
        self._categories = self._get_categories(category_names)

    def random(self):
        return "-".join([category.random() for category in self._categories])

    def _get_categories(self, category_names):
        categories = self._replace_randoms(category_names)
        return [self._collection.get(category) for category in categories]

    def _replace_randoms(self, categories):
        return [self._replace_random(x) for x in categories]

    def _replace_random(self, category):
        if category == Pattern.__random_key:
            return self._collection.random()
        return category
