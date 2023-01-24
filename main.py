import bme280
import smbus2
import os
import time

from lib.waveshare_epd import epd4in2
from PIL import Image, ImageDraw,ImageFont





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

