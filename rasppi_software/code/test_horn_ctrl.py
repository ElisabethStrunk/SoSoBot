import sys
import time
import RPi.GPIO as GPIO
from horn_ctrl import horn_1

#***************************************************************
#	Global-Functions
#***************************************************************

try:
  while True:
    print('Start Test:')
    print('Test: Turn ON the horn sound for backward')
    horn_1.backward()
    time.sleep(5)
    print('Test: Turn ON the horn sound for stop')
    horn_1.stop(0.5)
    time.sleep(5)
    break
          
except KeyboardInterrupt:
	GPIO.cleanup()
	print('Bye')
	sys.exit()




