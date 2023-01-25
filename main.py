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
import logging

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
        self.fonts = Fonts(time_font_size = 25, date_font_size = 25, temperature_font_size = 25)
        self.epd = epd2in9.EPD()
        self.epd.init()
    
    def primary_mode(self, start_mode = DISPLAY_MODE_WEATHER):
        self.mode = start_mode
        while True:
            self.draw_clock()

    def draw_clock(self):
        datetime_now = datetime.now()
        datestring = datetime_now.strftime(DATE_FORMAT).capitalize()
        timestring = datetime_now.strftime(TIME_FORMAT)
        
        logging.info("1.Drawing the clock
        Limage = Image.new('1', (self.epd.height, self.epd.width), 255) 
        draw = ImageDraw.Draw(Limage)
        draw.text((0, 0), timestring, font = self.fonts.time_font_size,align='center', fill = 0)
        draw.text((0, 05), datestring, font = self.fonts.date_font_size, align='center', fill = 0)
        draw.line((0,100,500,100), width=2, fill=0)
        draw.line((0,150,500,150), width=2, fill=0)
        self.epd.display(self.epd.getbuffer(Limage))


if __name__ == '__main__':
    weather = Weather()
    weather.primary_mode(DISPLAY_MODE_WEATHER)
'''
print(data.id)
print(data.temperature)
print(data.humidity)
print(data.pressure)
'''
