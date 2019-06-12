# ***************************************************************
# Imports
# ***************************************************************
import RPi.GPIO as GPIO


# ***************************************************************
# Globals / Constants / Enums
# ***************************************************************
# Constants for GPIO-Pins
MOTOR_RIGHT_FORWARD = 23
MOTOR_RIGHT_BACKWARD = 24

# your found GPIO pin numbers for the left motor:
# MOTOR_LEFT_FORWARD = ??
# MOTOR_LEFT_BACKWARD = ??


# ***************************************************************
# Class definition
# ***************************************************************


class MotorCtrl:

    """ Control of a servo-motor.

    Keyword arguments:
    gpioPin -- The gpio-pin which is connected to the motor-driver
    """

    # Initializes a handle for a control-motor
    def __init__(self, gpio_pin_forward, gpio_pin_backward, name):
        self.pin_forward = gpio_pin_forward
        self.pin_backward = gpio_pin_backward
        self.name = 'Motor_' + name
        self.on = False

    def forward(self, velocity):
        ret = self.name + ': '
        if velocity > 0.0:
            GPIO.output(self.pin_backward, 0)
            GPIO.output(self.pin_forward, 1)
            self.on = True
            ret = ret + 'Started forward'
        else:
            ret = ret + self.stop()
        return ret

    def backward(self, velocity):

        # your code here

        return "Your return message here"

    def stop(self):

        # your code here

        return "Your return message here"

    def is_on(self):
        # Indicates if the motor is running
        return self.on
        
    
# ***************************************************************
# Objects
# ***************************************************************
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_RIGHT_FORWARD, GPIO.OUT)
GPIO.setup(MOTOR_RIGHT_BACKWARD, GPIO.OUT)

# your code here for setting up the GPIOs of the left motor


motor_right = MotorCtrl(MOTOR_RIGHT_FORWARD, MOTOR_RIGHT_BACKWARD, 'Right')

# your code for initializing the left motor here
