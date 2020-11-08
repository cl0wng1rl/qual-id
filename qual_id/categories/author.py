from ..category import Category


class Author(Category):
    def get_values(self):
        return [
            "aesop",
            "asimov",
            "caroll",
            "eliot",
            "frost",
            "hemingway",
            "homer",
            "kipling",
            "orwell",
            "shakespeare",
            "stevenson",
            "tolstoy",
            "twain",
            "wilde",
            "wordsworth",
        ]
