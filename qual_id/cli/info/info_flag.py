class InfoFlag:
  def __init__(self, name, is_singular=False):
      self._name = name
      self._is_singular = is_singular

  def name(self):
    return self._name

  def is_singular(self):
    return self._is_singular
