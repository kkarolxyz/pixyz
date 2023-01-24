import RPi.GPIO as GPIO

def __init__(self,pin):
    self.__pin = pin
    GPIO.setmode(GPIO.BCM)