from argparse import Action, ArgumentTypeError


class RangeActionFactory:
    """A class that gets RequiredLength argparse.Action closures"""

    @staticmethod
    def get_action(minimum, maximum):
        """
        Return RequiredLength argparse.Action closure for given range
        
        PARAMETERS
        minimum: (int) the minimum length of the given list of values
        maximum: (int) the maximum length of the given list of values
        """
        class RequiredLength(Action):
            def __call__(self, parser, args, values, option_string=None):
                if not self._is_in_range(len(values)):
                    parser.error(self._get_error_message())
                setattr(args, self.dest, values)


            def _is_in_range(self, length):
                return minimum <= length <= maximum

            def _get_error_message(self):
                template = 'argument "{arg}" requires between {min} and {max} arguments'
                return template.format(arg=self.dest, min=minimum, max=maximum)

        return RequiredLength