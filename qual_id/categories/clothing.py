from ..category import Category

class Clothing(Category):
  def get_values(self):
    return [
        't-shirt',
        'shoes',
        'socks',
        'pants',
        'hat',
        'scarf',
        'mittens',
        'vest',
        'suit',
        'tie',
        'shorts',
        'skirt',
        'coat'
    ]
