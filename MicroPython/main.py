"""
Created by: Mr. Coxall
Created on: Nov 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *

# variables
location_x = 0
location_y = 0

display.show(Image.HAPPY)

# on button A press
while True:
    if button_a.is_pressed():
        display.clear()
        location_x = 0
        location_y = 0
        # loop down
        while location_y <= 3:
            # #loop to the right
            while location_x <= 3:
                sleep(500)
                display.clear()
                display.set_pixel(location_x, location_y, 9)
                location_x = location_x + 1
            sleep(500)
            display.clear()
            display.set_pixel(location_x, location_y, 9)
            location_y = location_y + 1

        # move pixel up
        while location_y >= 0:
            # move pixel left
            while location_x >= 1:
                sleep(500)
                display.clear()
                display.set_pixel(location_x, location_y, 9)
                location_x = location_x - 1
            sleep(500)
            display.clear()
            display.set_pixel(location_x, location_y, 9)
            location_y = location_y - 1

        # end
        sleep(100)
        display.clear()
        location_y = 0
        location_y = 0
        display.show(Image.HAPPY)
