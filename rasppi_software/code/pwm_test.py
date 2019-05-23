#***************************************************************
#	Imports
#***************************************************************
import os
import time
import RPi.GPIO as GPIO

#***************************************************************
#	Globals
#***************************************************************

# GPIO-Pins, the following are are availe for PWM
# 12 (Pin 32)
# 13 (Pin 33)
# 18 (Pin 12)
# 19 (Pin 35)
PWM_PIN_1 = 32
PWM_PIN_2 = 33
PWM_FREQUENCY = 1000
PWM_DC = 50

#***************************************************************
#	Setup
#***************************************************************
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN_1,GPIO.OUT)
GPIO.setup(PWM_PIN_2,GPIO.OUT)

#***************************************************************
#	Global-Functions
#***************************************************************

try:
    while 1:

        # Set PWM on Pin 32
        p = GPIO.PWM(PWM_PIN_1, PWM_FREQUENCY)  
        p.start(PWM_DC)
        time.sleep(100)
        p.stop()

         # Set PWM on Pin 33
        p = GPIO.PWM(PWM_PIN_2, PWM_FREQUENCY)  
        p.start(PWM_DC)
        time.sleep(100)
        p.stop()
            
except KeyboardInterrupt:
    pass
    p.stop()
    GPIO.cleanup()
	  print('Bye')
	  sys.exit()
