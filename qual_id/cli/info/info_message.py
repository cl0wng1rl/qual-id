class InfoMessage:
    def __init__(self, parameter, value, info):
        self._type = parameter.value
        self._value = value
        self._info = info
    
    def message(self):
      if self._value == None:
        return "Options for '{0}' parameter: \n{1}".format(self._type, self._info_string())
      return "Values for the {0}, '{1}': \n{2}".format(self._type, self._value, self._info_string())

    def _info_string(self):
        return ", ".join(self._info)