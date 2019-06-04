#***************************************************************
#	Imports
#***************************************************************
import sys
import time
import RPi.GPIO as GPIO
from led_ctrl import led_left, led_right

#***************************************************************
#	Global-Functions
#***************************************************************

try:
  while True:
    print('Start Test:')
    print('Test: Turn ON both leds')
    led_left.on()
    led_right.on()
    time.sleep(5)
    print('Test: Turn OFF both leds')
    led_left.off()
    led_right.off()
    time.sleep(5)
    print('Test: Let the led blink with a frequency of 2Hz')
    led_left.on(2)
    led_right.on(2)
#    time.sleep(5)
#    print('Test: Turn OFF both leds')
#    led_left.off()
#    led_right.off()
#    time.sleep(5)
#    break
          
except KeyboardInterrupt:
	GPIO.cleanup()
	print('Bye')
	sys.exit()





