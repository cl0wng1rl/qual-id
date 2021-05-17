import enum
from qual_id.cli.info.info_flag import InfoFlag

class Flag(enum.Enum):
  COLLECTION = InfoFlag("collection")
  CATEGORY = InfoFlag("category")
  FORMAT = InfoFlag("format", True)

  @staticmethod
  def from_string(string):
      return next((flag for flag in Flag if flag.value.name() == string), None)