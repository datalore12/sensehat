#!/usr/bin/env python
from sense_hat import AstroPi
import time
import datetime
from pygame.locals import *
import requests

ap = AstroPi()

humid = int(ap.get_humidity())

print humid
