class Pattern:
    def __init__(self, category_names, group):
        self._group = group
        self._categories = self._get_categories(category_names)

    def random(self):
        return "-".join([category.random() for category in self._categories])

    def _get_categories(self, category_names):
        return [self._group.get(name) for name in category_names]
