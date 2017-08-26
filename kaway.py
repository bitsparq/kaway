"""
Description: Developed to prototype an emoji led display installed on the back of the car.
Author: Abe Lopez
Credits: F.Stern 2014 for multilineMAX7219.py python library
"""


# Import library
import time
import multilineMAX7219_2x2 as LEDMatrix

# The following imported variables make it easier to feed parameters to the library functions
from multilineMAX7219_2x2 import DIR_L, DIR_R, DIR_U, DIR_D
from multilineMAX7219_2x2 import DIR_LU, DIR_RU, DIR_LD, DIR_RD
from multilineMAX7219_2x2 import DISSOLVE, GFX_ON, GFX_OFF, GFX_INVERT


# Initialise the library and the MAX7219/8x8LED arrays
LEDMatrix.init()

try:
	# Display a stationary message
	LEDMatrix.static_message("Hi!")
	time.sleep(2)
	LEDMatrix.clear_all()

	# Define & draw a sprite array, and then move it around on the array
	Pi = [[0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 1, 1, 1, 0, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0],
	      [1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 1, 0],
	      [0, 0, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0],
	      [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
	LEDMatrix.gfx_set_all(GFX_OFF)
	LEDMatrix.gfx_sprite_array(Pi, 7, 8)
	LEDMatrix.gfx_render()
	time.sleep(1)
	for repeat in range(2):
		for scroll in (DIR_L, DIR_LU, DIR_U, DIR_RU, DIR_R, DIR_RD, DIR_D, DIR_LD):
			moves = 2 * repeat + 1
			if scroll in [DIR_R, DIR_RD, DIR_D, DIR_LD]:
				moves += 1
			for loop in range(moves):
				LEDMatrix.gfx_scroll(scroll)
				LEDMatrix.gfx_render()
				time.sleep(0.1)
	time.sleep(1)

except KeyboardInterrupt:
	# Display a stationary message
	LEDMatrix.static_message("Bye!")
	time.sleep(2)
	LEDMatrix.clear_all()
