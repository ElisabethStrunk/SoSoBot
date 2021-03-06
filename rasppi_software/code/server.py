#***************************************************************
#	Imports
#***************************************************************
from flask import Flask, request
from flask_restful import Api, Resource

from motor_ctrl import motor_left, motor_right
from led_ctrl import led_left, led_right
from horn_ctrl import horn_1

#***************************************************************
#	Global-Functions
#***************************************************************
def calculate_velocity(velocity):
  calc_velocity = velocity
  if velocity <= 0.0:
    calc_velocity = 0.0
  elif velocity >= 1.0:
    calc_velocity = 1.0
  return calc_velocity

#***************************************************************
#	Classes
#***************************************************************
app = Flask(__name__)
@app.route('/move/<string:direct>/')
@app.route('/move/<string:direct>/<float:velocity>/')
@app.route('/move/<string:direct>/<float:velocity>/<int:angle>')
def motor(direct, velocity = 1.0, angle = 0):
  velocity = calculate_velocity(velocity)
  if direct == 'right':
    motor_left.forward(velocity)
    return 'RIGHT movement started'
  elif direct == 'left':
    motor_right.forward(velocity)
    return 'LEFT movement started'
  elif direct == 'forward':
    motor_left.forward(velocity)
    motor_right.forward(velocity)
    return 'FORWARD movement started'
  elif direct == 'backward':
    motor_left.backward(velocity)
    motor_right.backward(velocity)
    return 'BACKWARD movement started'
  elif direct == 'stop':
    motor_left.stop()
    motor_right.stop()
    return 'Motors stopped'
  else:
    return 'ERROR: Invalid direction'

@app.route('/horn/<string:status>', methods=['GET'])
def horn(status):
  if status == '1':
    horn_1.backward()
    return 'Sound 1 is playing'
  elif status == '2':
    horn_1.stop()
    return 'Sound 2 is playing'
  else:
    return 'ERROR: Invalid sound-option. Please choose another one'

#@app.route('/Led/<string:position>/<string:status>/', methods=['GET'])
@app.route('/led/<string:position>/<string:status>/')
@app.route('/led/<string:position>/<string:status>/<int:frequency>')
def led(position, status, frequency = 0):
  if position == 'right':
    if status == 'on':
      led_right.on(frequency)
      return 'Right LED on'
    elif status == 'off':
      led_right.off()
      return 'Right LED off'
    else:
      return 'Parameter ON/OFF is either missing or not valid'
  if position == 'left':
    if status == 'on':
      led_left.on(frequency)
      return 'Left LED on'
    elif status == 'off':
      led_left.off()
      return 'Left LED on'
    else:
       return 'Parameter ON/OFF is either missing or not valid'
  else:
     return 'ERROR: Invalid LED'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)