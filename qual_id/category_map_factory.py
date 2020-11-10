from qual_id.category_map import CategoryMap


class CategoryMapFactory:
    @staticmethod
    def all():
        return CategoryMap()

    @staticmethod
    def minimal():
        categories = [
            "adjective",
            "animal",
            "bird",
            "color",
            "food",
            "fruit",
            "geography",
            "instrument",
            "planet",
            "tea",
            "vehicle",
        ]
        return CategoryMap(categories)

    @staticmethod
    def neutral():
        categories = [
            "adjective",
            "animal",
            "bird",
            "capital",
            "city",
            "clothing",
            "color",
            "constellation",
            "country",
            "currency",
            "drink",
            "element",
            "emotion",
            "food",
            "fruit",
            "geography",
            "instrument",
            "particle",
            "planet",
            "state",
            "tea",
            "tool",
            "utensil",
            "vehicle",
            "wine",
        ]
        return CategoryMap(categories)
