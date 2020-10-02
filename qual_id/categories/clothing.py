from ..category import Category

class Clothing(Category):
  def get_values(self):
    return [
        'tshirt',
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
