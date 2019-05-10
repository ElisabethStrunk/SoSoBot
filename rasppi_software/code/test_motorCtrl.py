from motor_ctrl import motor_left, motor_right

#***************************************************************
#	Global-Functions
#***************************************************************

try:
    while True:
        print('Start Test:')
        time.sleep(5)
        print('Test: Turn on right motor')
        motor_right.forward()
        time.sleep(5)
        print('Test: Turn off right motor')
        motor_right.stop()
        time.sleep(5)
        print('Test: Turn on left motor')
        motor_left.forward()
        time.sleep(5)
        print('Test: Turn off left motor')
        motor_left.stop()
          
except KeyboardInterrupt:
	GPIO.cleanup()
	print('Bye')
	sys.exit()




