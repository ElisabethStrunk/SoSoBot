from motor_ctrl import motor_left, motor_right
import time
import sys
import RPi.GPIO as GPIO

#***************************************************************
#	Global-Functions
#***************************************************************

try:
  while True:
    print('Start Test:')
    time.sleep(5)
    print('Test: Turn on right motor forward')
    motor_right.forward()
    time.sleep(5)
    print('Test: Turn on right motor backward')
    motor_right.backward()
    time.sleep(5)
    print('Test: Turn off right motor')
    motor_right.stop()
    time.sleep(5)
    print('Test: Turn on left motor forward')
    motor_left.forward()
    time.sleep(5)
    print('Test: Turn on right motor backward')
    motor_left.backward()
    time.sleep(5)
    print('Test: Turn off left motor')
    motor_left.stop()
          
except KeyboardInterrupt:
	GPIO.cleanup()
	print('Bye')
	sys.exit()




