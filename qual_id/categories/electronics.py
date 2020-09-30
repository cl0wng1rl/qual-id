from ..category import Category


class Electronics(Category):
  def get_values(self):
    return [
        'laptop',
        'Desktop',
        'microwave-oven',
        'refrigerator',
        'mobile',
        'television',
        'radio',
        'electric-guitar',
        'washing-machine',
        'trimmer',
        'air-conditioner',
    ]