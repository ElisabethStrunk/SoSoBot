
#***************************************************************
#	Imports
#***************************************************************
import smbus
import os
import RPi.GPIO as GPIO

#***************************************************************
#	Globals
#***************************************************************

# GPIO-Pins (12,13,18 and 19 are capable of PWM)
MOTOR_RIGHT_FORWARD = 14
MOTOR_RIGHT_BACKWARD = 15
MOTOR_LEFT_FORWARD = 17
MOTOR_LEFT_BACKWARD	= 27


#***************************************************************
#	Setup
#***************************************************************
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_RIGHT_FORWARD,GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_BACKWARD,GPIO.OUT)
GPIO.setup(MOTOR_LEFT_FORWARD,GPIO.OUT)
GPIO.setup(MOTOR_LEFT_BACKWARD,GPIO.OUT)


#***************************************************************
#	Global-Functions
#***************************************************************
class MotorCtrl:

  """Control of a servo-motor.

  Keyword arguments:
  gpioPin -- The gpio-pin which is connected to the motor-driver
  """

  # Initializes the motor-control
  def __init__(self, gpio_pin_forward, gpio_pin_backward, name):
    self.pin_forward = gpio_pin_forward
    self.pin_backward = gpio_pin_backward
    self.name = name
    self.on  = False

  # Starts the motor in forward direction
  def forward(self):
    print('Motor:= ; started forward', self.name)
    GPIO.output(self.pin_backward, 0)
    GPIO.output(self.pin_forward, 1)
    self.on  = True

        
  # Starts the motor in backward direction
  def forward(self):
    print('Motor:= ; started backward', self.name)
    GPIO.output(self.pin_forward, 0)
    GPIO.output(self.pin_backward, 1)
    self.on  = True

  # Stops the motor
  def stop(self):
    print('Motor:= ; stopped', self.name)
    GPIO.output(self.pin_forward, 0)
    GPIO.output(self.pin_backward, 0)
    self.on  = False
    
  # Indicates if the motor is running
  def is_on(self):
    return self.on


#***************************************************************
#	Objects
#***************************************************************
motor_right = MotorCtrl(MOTOR_RIGHT_FORWARD, MOTOR_RIGHT_BACKWARD, 'Right')
motor_left  = MotorCtrl(MOTOR_LEFT_FORWARD, MOTOR_LEFT_BACKWARD, 'Left')