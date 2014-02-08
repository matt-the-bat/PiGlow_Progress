""" Use a Pimoni PiGlow as a progress indicator. """

from piglow import PiGlow
from time import sleep
import math

class Progress:
    """ min_ & max_value set the spectrum for progress.
	
    """

    def __init__(self, min_value, max_value):
        self.min_value = float(min_value)
        self.max_value = float(max_value)
        self.current_value = float(min_value)

	self.pi = PiGlow()
	self.pi.all(0)

    def current(self, value):
        """ Send current value to progress bar. Defaults as minimum value."""
        self.current_value = float(value)
	self.draw()

    def draw(self):
	scale = self.max_value - self.min_value + 1

	last = int(math.ceil((self.current_value * 6)/ scale))
	# Invert arm
	#last = 7 - last
	print 'Glowing at', last
	for x in range(1,last+1):
		self.pi.led(x, 20)
#		print 'Glowing at', x	

pigress = Progress(1,10)
pigress.current(1)
sleep(1)
pigress.current(2)
sleep(1)
pigress.current(3)
sleep(1)
pigress.current(4)
