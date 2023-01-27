#!/usr/bin/env python3

from lib import epd2in9_v2
from PIL import Image, ImageDraw,ImageFont
from datetime import datetime
import RPi.GPIO as GPIO

import bme280
import smbus2
import os
import time

RES_FONT = os.path.join('font/','Roboto-Black.ttf')
DATE_FORMAT = "%b %d %Y"
TIME_FORMAT = "%H:%M:%S"

port = 1 
address = 0x77
bus = smbus2.SMBus(port)


#Display mode, in future it will be posible to set few differen window
DISPLAY_MODE_WEATHER = 1

class Fonts:
    def __init__(self,temperature_font_size, time_font_size,date_font_size, hum_pre_font_size ):
        self.temperature_font_size = ImageFont.truetype(RES_FONT,temperature_font_size)
        self.time_font_size = ImageFont.truetype(RES_FONT, time_font_size)
        self.date_font_size = ImageFont.truetype(RES_FONT, date_font_size)
        self.hum_pre_font_size = ImageFont.truetype(RES_FONT, hum_pre_font_size)

        
class Weather:
    
    epd = None
    fonts = None
    mode = DISPLAY_MODE_WEATHER
    nobeldata = None
    
    def __init__(self):

        self.fonts = Fonts(time_font_size = 25, date_font_size = 25, temperature_font_size = 45, hum_pre_font_size = 22)
        self.epd = epd2in9_v2.EPD()
        self.epd.init()
    
    def primary_mode(self, start_mode = DISPLAY_MODE_WEATHER):
        self.mode = start_mode
        while True:
            self.draw()
        

    def draw(self):
        while (True):
            datetime_now = datetime.now()
            datestring = datetime_now.strftime(DATE_FORMAT).capitalize()
            timestring = datetime_now.strftime(TIME_FORMAT)


            calibration_params = bme280.load_calibration_params(bus, address)
            data = bme280.sample(bus,address,calibration_params)
            #print(data.id)
            TEMPERATURE = "{0:0.1f}".format(data.temperature)
            HUMIDITY = "{0:0.1f}".format(data.humidity)
            PRESURE = "{0:0.1f}".format(data.pressure)


            Limage = Image.new('1', (self.epd.height, self.epd.width), 255) 
            draw = ImageDraw.Draw(Limage)
            draw.text((20, 1),timestring, font = self.fonts.time_font_size, fill = 0)
            draw.text((130, 1), datestring, font = self.fonts.date_font_size, fill = 0)
            draw.line((0,30,epd2in9_v2.EPD_HEIGHT,30), width=2, fill=0)
            draw.text((80,35),TEMPERATURE+u"\u00b0C", font = self.fonts.temperature_font_size, fill = 0)
            draw.text((10,90),HUMIDITY+u"%", font = self.fonts.hum_pre_font_size, fill = 0)
            draw.text((80,90),PRESURE+u"hPa", font = self.fonts.hum_pre_font_size, fill = 0)
            draw.line((0,85,epd2in9_v2.EPD_HEIGHT,85), width=2, fill=0)
            self.epd.display_Partial(self.epd.getbuffer(Limage))

            '''
            draw.rectangle((0, 0, epd2in9_v2.EPD_HEIGHT, epd2in9_v2.EPD_WIDTH), fill = 255)
            draw.text((20, 1), time.strftime('%H:%M:%S'), font = self.fonts.time_font_size, fill = 0)
            draw.line((0,30,epd2in9_v2.EPD_WIDTH,30), width=2, fill=0)
            draw.text((130, 1), datestring, font = self.fonts.date_font_size, fill = 0)
            draw.text((80, 50),tmp+" C", font = self.fonts.temperature_font_size, fill = 0)
            newimage = Limage.crop([0, 0, epd2in9_v2.EPD_HEIGHT, epd2in9_v2.EPD_WIDTH])
            Limage.paste(newimage, (0, 0, epd2in9_v2.EPD_HEIGHT, epd2in9_v2.EPD_WIDTH)) 
            self.epd.display_Partial(self.epd.getbuffer(Limage))
            '''
if __name__ == '__main__':
    weather = Weather()
    weather.primary_mode(DISPLAY_MODE_WEATHER)
