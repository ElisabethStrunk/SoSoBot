
#***************************************************************
#	Imports
#***************************************************************
#import smbus
import os
import RPi.GPIO as GPIO
import time


#***************************************************************
#	Globals
#***************************************************************

# GPIO-Pins (12,13,18 and 19 are capable of PWM)
LED_LEFT = 12
LED_RIGHT = 16

#***************************************************************
#	Setup
#***************************************************************
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_LEFT,GPIO.OUT)
GPIO.setup(LED_RIGHT,GPIO.OUT)

#GPIO.output(LED_LEFT, 1)
#GPIO.output(LED_RIGHT, 1)

#time.sleep(2)

#GPIO.output(LED_LEFT, 0)
#GPIO.output(LED_RIGHT, 0)
