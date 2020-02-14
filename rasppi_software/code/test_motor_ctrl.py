#***************************************************************
#	Imports
#***************************************************************
import sys
import time
import RPi.GPIO as GPIO
from motor_ctrl import motor_left

#***************************************************************
#	Global-Functions
#***************************************************************

try:
  while True:
    print('Start Test:')
    print('Test: Turn on left motor forward with 100%')
    motor_left.forward(1.0)
    time.sleep(5)
    print('Test: Stopps left motor')
    motor_left.stop()
    time.sleep(5)
    print('Test: Turn on left motor backward with 100%')
    motor_left.backward(1.0)
    time.sleep(5)
    print('Test: Stopps left motor')
    motor_left.stop()
    time.sleep(5)
    break
          
except KeyboardInterrupt:
	GPIO.cleanup()
	print('Bye')
	sys.exit()



