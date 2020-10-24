from ..category import Category
import strgen


class RandomId(Category):
    def get_values(self):
        return [self.get_id()]

    def get_id(self):
        return strgen.StringGenerator("[a-z0-9]{10}").render()
