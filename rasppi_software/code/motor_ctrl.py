
#***************************************************************
#	Imports
#***************************************************************
import smbus
import os
import RPi.GPIO as GPIO

#***************************************************************
#	Globals
#***************************************************************

# GPIO-Pins
MOTOR_LEFT			= 40
MOTOR_RIGHT		    = 37


motor_left      = motor_ctrl.MotorCtrl(MOTOR_RIGHT, 'Left')
motor_right     = motor_ctrl.MotorCtrl(MOTOR_RIGHT, 'Right')


#***************************************************************
#	Global-Functions
#***************************************************************
class MotorCtrl:

    """Control of a servo-motor.

    Keyword arguments:
    gpioPin -- The gpio-pin which is connected to the motor-driver
    """

    # Initializes the motor-control
	def __init__(self, gpio_pin, name):
        self.pin = gpio_pin
        self.name = name
        self.on  = True

    # Stops the motor
    def start(self):
        print('Motor:= ; started', self.name)
        GPIO.output(self.pin, 1)
        self.on  = True

    # Starts the motor
    def stop(self)
        print('Motor:= ; stopped', self.name)
        GPIO.output(self.pin, 0)
        self.on  = False
    
    # Indicates if the motor is running
    def is_on(self)
        return self.on
