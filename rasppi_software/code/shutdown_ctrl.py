#***************************************************************
#	Imports
#***************************************************************
import os
import RPi.GPIO as GPIO

#***************************************************************
#	Globals
#***************************************************************

SHUTDOWN_SWITCH = 3

#***************************************************************
#	Setup
#***************************************************************
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# SHUTDOWN_SWITCH Pin set up as input. It is pulled up to stop false signals
GPIO.setup(SHUTDOWN_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # wait for the pin to be sorted with GND and, if so, halt the system
        GPIO.wait_for_edge(SHUTDOWN_SWITCH, GPIO.FALLING)
        # shut down the Pi
        os.system("/sbin/shutdown -h now")
except:
    GPIO.cleanup()