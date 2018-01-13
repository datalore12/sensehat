#!/usr/bin/env python

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)

sense.show_message("SenseHat is aweseome", scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,0,255])
