
#***************************************************************
#	Imports
#***************************************************************
import os
import RPi.GPIO as GPIO
import threading

#***************************************************************
#	Globals / Constants / Enums
#***************************************************************

# Constants for GPIO-Pins
MOTOR_LEFT_FORWARD  = 17
MOTOR_LEFT_BACKWARD = 27
MOTOR_RIGHT_FORWARD = 23
MOTOR_RIGHT_BACKWARD = 24
# Your code for right motor-pins


#***************************************************************
#	Class definition
#***************************************************************
class MotorCtrl:

  """Control of a servo-motor.

  Keyword arguments:
  gpioPin -- The gpio-pin which is connected to the motor-driver
  """

  # Initializes a handle for a control-motor
  def __init__(self, gpio_pin_forward, gpio_pin_backward, name):
    self.pin_forward = gpio_pin_forward
    self.pin_backward = gpio_pin_backward
    self.name = 'Motor_' + name
    self.on  = False

  def forward(self, velocity):
    ret = self.name + ': '
    if velocity > 0.0:
      GPIO.output(self.pin_backward, 0)
      GPIO.output(self.pin_forward, 1)
      self.on  = True
      ret = ret + 'Started forward'
    else:
      ret = ret + self._stop()
    return ret

  # Your code for backwards-function

  def _stop(self):
    GPIO.output(self.pin_forward, 0)
    GPIO.output(self.pin_backward, 0)
    self.on  = False 
    return 'Stopped'

  # Indicates if the motor is running
  def is_on(self):
    return self.on
        
    
#***************************************************************
#	Objects
#***************************************************************
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_LEFT_FORWARD,GPIO.OUT)
GPIO.setup(MOTOR_LEFT_BACKWARD,GPIO.OUT)
# Your code for pin setup of the gpios for the right motor

motor_left  = MotorCtrl(MOTOR_LEFT_FORWARD, MOTOR_LEFT_BACKWARD, 'Left')
