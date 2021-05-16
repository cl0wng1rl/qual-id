from qual_id.flag import Flag

class CliParser:
    def __init__(self, arguments):
        self._arguments = arguments
        self._shift_arguments()
        self._config = {"format": "csv"}

    def parse(self):
        self._check_for_help()
        while len(self._arguments):
            self._extract_parameter(self._get_next_flag())
        return self._config

    def _check_for_help(self):
        if any(map(lambda arg: Flag.HELP.value.equals(arg), self._arguments)):
            self._print_help()
            exit()
    
    def _get_next_flag(self):
        flag = next((flag for flag in Flag if flag.value.equals(self._arguments[0])), None)
        if not flag:
            print("invalid parameter: " + self._arguments[0])
            exit()
        return flag

    def _check_for_remaining_args(self, flag):
        if not len(self._arguments):
            print("no {0} specified".format(flag.value.name()))
            exit()
    
    def _shift_arguments(self):
        self._arguments = self._arguments[1:]

    def _extract_parameter(self, flag):
        self._shift_arguments()
        self._check_for_remaining_args(flag)
        self._config[flag.value.name()] = self._arguments[0]
        self._shift_arguments()

    def _print_help(self):
        print(" ")
        print("Qual ID - get qualitative IDs")
        print(" ")
        print("qual-id [options]")
        print(" ")
        print("options:")
        print("-h, --help                show brief help")
        print("-p, --pattern             specify the pattern of the qual IDs")
        print("-c, --collection          specify which collection to use")
        print("-n, --number              specify how many qual IDs to receive")
        print("-f, --format              specify the format of the qual IDs")
        print(" ")