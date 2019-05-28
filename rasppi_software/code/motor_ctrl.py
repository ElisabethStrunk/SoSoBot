
#***************************************************************
#	Imports
#***************************************************************
import os
import RPi.GPIO as GPIO
import threading
from enum import Enum

#***************************************************************
#	Globals / Constants / Enums
#***************************************************************

# Constants for GPIO-Pins
MOTOR_RIGHT_FORWARD = 23
MOTOR_RIGHT_BACKWARD = 24
MOTOR_LEFT_FORWARD = 17
MOTOR_LEFT_BACKWARD = 27

# Constant for PWM Frequency
PWM_FREQUENCY = 10000

# Enum of direction
class direction(Enum):
  FORWARD  = 1
  BACKWARD = 2
  STOP = 3

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
    self.direct = direction.STOP
    self.t_on = 0
    self.t_off =  0
    self.timer = None

  def forward(self, velocity = 1.0):
    self._stop_timer()
    self.direct = direction.FORWARD
    _run(velocity)

  def backward(self, velocity = 1.0):
    self._stop_timer()
    self.direct = direction.BACKWARD
    _run(velocity)

  def stop(self):
    self._stop_timer()
    self.direct = direction.STOP
    self._stop()

  # Indicates if the motor is running
  def is_on(self):
    return self.on

  def _run(velocity):
    if velocity >= 1.0:
      if self.direct == direction.FORWARD:
        self._forward()
      elif self.direct == direction.BACKWARD:
        self._backward()
    elif velocity <= 0.0:
      self._stop()
    else:
      duty_cycle = velocity
      period = 1 / PWM_FREQUENCY
      self.t_on = duty_cycle * period
      self.t_off = period - self.t_on
      _run_pwm()
    
  def _run_pwm(self):
    if self.on:
       self._stop()
       self.timer = threading.Timer(self.t_off, self._run_pwm)
       self.timer.start()
    else:
      if self.direct == direction.FORWARD:
        self._forward()
      elif self.direct == direction.BACKWARD:
        self._backward()
      self.timer = threading.Timer(self.t_off, self._run_pwm)
      self.timer.start()
        
  def _forward(self):
    GPIO.output(self.pin_backward, 0)
    GPIO.output(self.pin_forward, 1)
    self.on  = True

  def _backward(self):
    GPIO.output(self.pin_forward, 0)
    GPIO.output(self.pin_backward, 1)
    self.on  = True

  def _stop(self):
    GPIO.output(self.pin_forward, 0)
    GPIO.output(self.pin_backward, 0)
    self.on  = False 

  def _stop_timer(self):
    if self.timer != None:
      self.timer.cancel()
      self.timer = None
    
#***************************************************************
#	Objects
#***************************************************************
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_RIGHT_FORWARD,GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_BACKWARD,GPIO.OUT)
GPIO.setup(MOTOR_LEFT_FORWARD,GPIO.OUT)
GPIO.setup(MOTOR_LEFT_BACKWARD,GPIO.OUT)

motor_right = MotorCtrl(MOTOR_RIGHT_FORWARD, MOTOR_RIGHT_BACKWARD, 'Right')
motor_left  = MotorCtrl(MOTOR_LEFT_FORWARD, MOTOR_LEFT_BACKWARD, 'Left')
