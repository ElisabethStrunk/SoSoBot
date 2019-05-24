
#***************************************************************
#	Imports
#***************************************************************
import smbus
import os
import RPi.GPIO as GPIO
import threading
from enum import Enum

#***************************************************************
#	Globals
#***************************************************************

# GPIO-Pins (12,13,18 and 19 are capable of PWM)
MOTOR_RIGHT_FORWARD = 23
MOTOR_RIGHT_BACKWARD = 24
MOTOR_LEFT_FORWARD = 17
MOTOR_LEFT_BACKWARD = 27
PWM_FREQUENCY = 10000

#***************************************************************
#	Setup
#***************************************************************
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_RIGHT_FORWARD,GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_BACKWARD,GPIO.OUT)
GPIO.setup(MOTOR_LEFT_FORWARD,GPIO.OUT)
GPIO.setup(MOTOR_LEFT_BACKWARD,GPIO.OUT)

class direction(Enum):
  FORWARD  = 1
  BACKWARD = 2
  STOP = 3

#***************************************************************
#	Private-Functions
#***************************************************************
# Starts the motor in forward direction


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
    
    self.direct = direction.STOP
    self.t_on = 0
    self.t_off =  0

  #
  def run(self, direct, velocity):
    self.direct = direct
    self.t_off =  0

    # calculates the duty_cycle by velocity
    if velocity is None:
      duty_cycle = 1
    else:
      duty_cycle = velocity / 100

    # calculates t_on and t_off for the PWM
    period = 1 / PWM_FREQUENCY
    self.t_on = duty_cycle * period
    self.t_off = period - self.t_on  
    print(self.name + ': ' + 't_on = ' + str(self.t_on) + 't_off = ' + str(self.t_off))
    self.__run()

   # Stops the motor
  def stop(self):
    GPIO.output(self.pin_forward, 0)
    GPIO.output(self.pin_backward, 0)
    self.on  = False
  
  # Starts the motor in forward direction
  def __forward(self):
    GPIO.output(self.pin_backward, 0)
    GPIO.output(self.pin_forward, 1)
    self.on  = True
        
  # Starts the motor in backward direction
  def __backward(self):
    GPIO.output(self.pin_forward, 0)
    GPIO.output(self.pin_backward, 1)
    self.on  = True

  def __run(self):

    if self.direct == direction.FORWARD:
      if self.on == True:
        self.stop()
      else:
        self.__forward()
    elif self.direct == direction.BACKWARD:
      if self.on == True:
        self.stop()
      else:
        self.__backward()
     
    if self.t_off <= 0.0:
      if self.direct == direction.FORWARD:
        self.__forward()
      else:
        self.__backward()
    elif self.t_on <= 0.0:
       self.stop()
    elif self.on == True:
      threading.Timer(self.t_on, self.__run).start()
    elif self.on == False:
      threading.Timer(self.t_off, self.__run).start()
    
  # Indicates if the motor is running
  def is_on(self):
    return self.on


#***************************************************************
#	Objects
#***************************************************************
motor_right = MotorCtrl(MOTOR_RIGHT_FORWARD, MOTOR_RIGHT_BACKWARD, 'Right')
motor_left  = MotorCtrl(MOTOR_LEFT_FORWARD, MOTOR_LEFT_BACKWARD, 'Left')
