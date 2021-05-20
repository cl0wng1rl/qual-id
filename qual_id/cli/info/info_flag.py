class InfoFlag:
  def __init__(self, long, short, is_singular=False):
      self._long = long
      self._short = short
      self._values = { self._format_long(), self._format_short() }
      self._is_singular = is_singular

  def name(self):
    return self._long

  def is_singular(self):
    return self._is_singular

  def equals(self, flag):
    return flag in self._values

  def _format(self, long, short):
    return { self._format_long(), self._format_short() }

  def _format_long(self):
      return "--{0}".format(self._long)

  def _format_short(self):
      return "-{0}".format(self._short)