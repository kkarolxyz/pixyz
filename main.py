#!/usr/bin/env python3

from lib import epd4in2
from PIL import Image, ImageDraw,ImageFont
from datetime import datetime

import RPi._GPIO as GPIO
import bme280
import smbus2
import os
import json
import time

RES_FONT = os.path.join(os.path.dirname(os.path.relpath(__file__)),'font/')
RES_PIC = os.path.join(os.path.dirname(os.path.relpath(__file__)),'pic/')

DATE_FORMAT = "%b %d %Y"
TIME_FORMAT = "%H:%M"
FONT = os.path.join(RES_FONT,'Roboto-Black.ttf')


#x = datetime(2022, 9, 15, 12, 45, 35)
#print(x.strftime(DATE_FORMAT))

class Fonts:
    def __init__(self,temperature_font_size, time_font_size,date_font_size):
        pass


'''
port = 1 
address = 0x77
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

data = bme280.sample(bus,address,calibration_params)

print(data.id)
print(data.temperature)
print(data.humidity)
print(data.pressure)
'''

