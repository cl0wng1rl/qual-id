from ..category import Category


class Electronic(Category):
  def get_values(self):
    return [
        'laptop',
        'Desktop',
        'refrigerator',
        'mobile',
        'television',
        'radio',
        'trimmer',
		'headPhones',
		'fan',
		'elevator'
    ]