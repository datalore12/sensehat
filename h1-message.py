#!/usr/bin/env python

from sense_hat import SenseHat
sense=SenseHat()

t = sense.get_temperature_from_pressure()
p = sense.get_pressure()
h = sense.get_humidity()

t = round(t,1)
p = round(p,1)
h = round(h,1)

msg="Temperature = %s, Pressure=%s, Humidity=%s" %(t,p,h)

sense.set_rotation(180)

try:
	while True:
	        if t > 18.3 and t < 26.7:
	                bg = [0, 100, 0] # green
	        else:
	                bg = [100, 0, 0] # red

	        sense.show_message(msg,scroll_speed=0.10, back_colour=bg)
except KeyboardInterrupt:
	sense.clear()
