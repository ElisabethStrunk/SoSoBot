#***************************************************************
#	Imports
#***************************************************************
import sys
import time
import RPi.GPIO as GPIO
from motor_ctrl import motor_left, motor_right

#***************************************************************
#	Global-Functions
#***************************************************************

try:
  while True:
    print('Start Test:')
    print('Test: Turn on both motors forward with 100%')
    motor_right.forward()
    motor_left.forward()
    time.sleep(5)
    print('Test: Stopps both motors')
    motor_right.stop()
    motor_left.stop()
    time.sleep(5)
    print('Test: Turn on both motors backward with 100%')
    motor_right.backward()
    motor_left.backward()
    time.sleep(5)
    print('Test: Stopps both motors')
    motor_right.stop()
    motor_left.stop()
    time.sleep(5)
    print('Test: Starts the motors forward with 50%')
    motor_right.forward(0.5)
    motor_left.forward(0.5)
    break
          
except KeyboardInterrupt:
	GPIO.cleanup()
	print('Bye')
	sys.exit()



