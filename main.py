#!/usr/bin/env python3

from lib import epd2in9
from PIL import Image, ImageDraw,ImageFont
from datetime import datetime
import RPi.GPIO as GPIO

import bme280
import smbus2
import os
import json
import time

RES_FONT = os.path.join('font/','Roboto-Black.ttf')
DATE_FORMAT = "%b %d %Y"
TIME_FORMAT = "%H:%M"

#port = 1 
#address = 0x77
#bus = smbus2.SMBus(port)
#calibration_params = bme280.load_calibration_params(bus, address)
#data = bme280.sample(bus,address,calibration_params)

#Display mode, in future it will be posible to set few differen window
DISPLAY_MODE_WEATHER = 1

class Fonts:
    def __init__(self,temperature_font_size, time_font_size,date_font_size):
        self.temperature_font_size = ImageFont.truetype(RES_FONT,temperature_font_size)
        self.time_font_size = ImageFont.truetype(RES_FONT, time_font_size)
        self.date_font_size = ImageFont.truetype(RES_FONT, date_font_size)

        
class Weather:
    
    epd = None
    fonts = None
    mode = DISPLAY_MODE_WEATHER
    nobeldata = None
    
    def __init__(self):

        self.fonts = Fonts(time_font_size = 75, date_font_size = 35, temperature_font_size = 50)
        self.epd = epd2in9.EPD()
        self.epd.init()
    
    def primary_mode(self, start_mode = DISPLAY_MODE_WEATHER):
        self.mode = start_mode
        while True:
            self.draw_clock()
            self.clock_update()

    def clock_update(self):
        now = datetime.now()
        seconds_until_next_minute = 60 - now.time().second
        time.sleep(seconds_until_next_minute)
    

    def draw_clock(self):
        datetime_now = datetime.now()
        datestring = datetime_now.strftime(DATE_FORMAT).capitalize()
        timestring = datetime_now.strftime(TIME_FORMAT)

        Limage = Image.new('1', (self.epd.height, self.epd.width), 255) 
        draw = ImageDraw.Draw(Limage)
        draw.text((50, 10), timestring, font = self.fonts.time_font_size,align='center', fill = 0)
        draw.text((50, 100), datestring, font = self.fonts.date_font_size, align='center', fill = 0)
        self.epd.display(self.epd.getbuffer(Limage))


if __name__ == '__main__':
    weather = Weather()
    weather.primary_mode(DISPLAY_MODE_WEATHER)
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

