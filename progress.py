""" Use a Pimoni PiGlow as a progress indicator. """

from piglow import PiGlow


class Progress:
    """ min_ & max_value set the spectrum for progress """

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = min_value

    def set_current(self, value):
        """ Send current value to progress bar. Defaults as minimum value."""
        self.current_value = value