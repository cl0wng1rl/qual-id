from ..category import Category
import strgen


class RandomId(Category):
    def get_values(self):
        return [self.get_random_id()]

    def get_random_id(self):
        return strgen.StringGenerator("[a-zA-Z0-9]{10}").render()
