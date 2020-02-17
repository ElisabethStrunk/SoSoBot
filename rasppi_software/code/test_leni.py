import sys
import time
import RPi.GPIO as GPIO
from motor_ctrl import motor_left, motor_right

try:
 while True:
  print('left forward')
  motor_left.forward(1.0)
  time.sleep(5.0)
  print('left backward')
  motor_left.backward(1.0)
  time.sleep(5.0)
  motor_left._stop()
  time.sleep(1.0)
  print('right forward')
  motor_right.forward(1.0)
  time.sleep(5.0)
  print('right backward')
  motor_right.backward(1.0)
  time.sleep(5.0)
  motor_left._stop()
  time.sleep(1.0)
  break 
  

except KeyboardInterrupt:
  print('program close')
  GPIO.cleanup()
  sys.exit()
