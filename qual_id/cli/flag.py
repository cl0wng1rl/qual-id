import enum
from qual_id.cli.command_flag import CommandFlag

class Flag(enum.Enum):
  COLLECTION = CommandFlag("collection", "c")
  PATTERN = CommandFlag("pattern", "p")
  FORMAT = CommandFlag("format", "f")
  NUMBER = CommandFlag("number", "n")
  HELP = CommandFlag("help", "h")