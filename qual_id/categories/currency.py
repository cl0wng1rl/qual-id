from ..category import Category


class Currency(Category):
  def get_values(self):
    return [
        'aud',
        'cad',
        'clp',
        'cny',
        'cop',
        'czk',
        'dkk',
        'eur',
        'gbp',
        'hkd',
        'idr',
        'inr',
        'jpy',
        'nzd',
        'rub',
        'sar',
        'sgd',
        'usd',
        'zar',
    ]
