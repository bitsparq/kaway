"""
Description: Developed to prototype an emoji led display installed on the back of the car.
Author: Abe Lopez
Credits: F.Stern 2014 for multilineMAX7219.py python library
"""


# Import library
import multilineMAX7219_2x2 as LEDMatrix
import time

# Initialise the library and the MAX7219/8x8LED arrays
LEDMatrix.init()

try:
	# Display a stationary message
	LEDMatrix.static_message("Hi!")
	time.sleep(2)
	LEDMatrix.clear_all()


except KeyboardInterrupt:
	# Display a stationary message
	LEDMatrix.static_message("Bye!")
	time.sleep(2)
	LEDMatrix.clear_all()
