
#***************************************************************
#	Imports
#***************************************************************
#import smbus
import os
import RPi.GPIO as GPIO
import time
import threading


#***************************************************************
#	Globals
#***************************************************************

# GPIO-Pins (12,13,18 and 19 are capable of PWM)
LED_LEFT = 12
LED_RIGHT = 16

#***************************************************************
#	Class definition
#***************************************************************
class LedCtrl:

  """Control of a LED.

  Keyword arguments:
  gpioPin -- The gpio-pin which is connected to the motor-driver
  """

  # Initializes a handle for a control-motor
  def __init__(self, gpio_pin, name):
    self.gpio_pin = gpio_pin
    self.name = 'LED_' + name
    self.isOn  = False
    self.timer = None
    
  def on(self):
    self._stop_timer()
    return self._on()

  def off(self):
    self._stop_timer()
    return self._off()
  
  def blink(self, freq):
    self._stop_timer()
    interval = 1 / freq
    self.timer = threading.Timer(interval, self._blink)
    return True

  def _blink(self):
    if self.isOn:
      self._off()
    else:
      self._on()
    self.timer.start()

  def _on(self):
    print('turn on')
    GPIO.output(self.gpio_pin, 1)
    self.isOn = True
    return True

  def _off(self):
    print('turn off')
    GPIO.output(self.gpio_pin, 0)
    self.isOn = False
    return True

  def _stop_timer(self):
     if self.timer != None:
      self.timer.cancel()
      self.timer = None

#***************************************************************
#	Setup
#***************************************************************
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_LEFT,GPIO.OUT)
GPIO.setup(LED_RIGHT,GPIO.OUT)

led_left = LedCtrl(LED_LEFT, 'Left')
led_right = LedCtrl(LED_RIGHT, 'Right')

