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
@app.route('/Motor/<string:direct>/')
@app.route('/Motor/<string:direct>/<float:velocity>/')
@app.route('/Motor/<string:direct>/<float:velocity>/<int:angle>')
def motor(direct, velocity = 1.0, angle = 0):
  velocity = calculate_velocity(velocity)
  if direct == 'right':
    motor_right.forward(velocity)
    return 'RIGHT movement started'
  elif direct == 'left':
    motor_left.forward(velocity)
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
    return 'Invalid direction'

@app.route('/Horn/<string:status>', methods=['GET'])
def horn(status):
  if status == 'Horn1':
    horn_1.backward()
    return 'Short horn sound is played back'
  elif status == 'Horn2':
    horn_1.stop()
    return 'Playback of short horn sound is stopped'
  else:
    return 'Short horn sound is played back'

#@app.route('/Led/<string:position>/<string:status>/', methods=['GET'])
@app.route('/Led/<string:position>/<string:status>/')
@app.route('/Led/<string:position>/<string:status>/<int:frequency>')
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
     return 'Position not found'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)