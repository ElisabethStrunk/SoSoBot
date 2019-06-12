# ***************************************************************
# Imports
# ***************************************************************
import sys
import time
import RPi.GPIO as GPIO
from motor_ctrl import motor_left, motor_right


# ***************************************************************
# Global-Functions
# ***************************************************************
print('Start Test:')
print('Test: Turn on both motors forward')
motor_right.forward(1)
motor_left.forward(1)
time.sleep(1)
print('Test: Stops both motors')
motor_right.stop()
motor_left.stop()
time.sleep(0.5)
print('Test: Turn on both motors backward')
motor_right.backward(1)
motor_left.backward(1)
time.sleep(1)
print('Test: Stops both motors')
motor_right.stop()
motor_left.stop()
time.sleep(0.5)

GPIO.cleanup()
print('Bye')
sys.exit()
