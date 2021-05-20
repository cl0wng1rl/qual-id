import enum
from qual_id.cli.main.command_flag import CommandFlag

class Flag(enum.Enum):
  GROUP = CommandFlag("group", "g")
  PATTERN = CommandFlag("pattern", "p")
  FORMAT = CommandFlag("format", "f")
  NUMBER = CommandFlag("number", "n")
