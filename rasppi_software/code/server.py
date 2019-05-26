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
    calc_velocity = 0.0
  return calc_velocity

#***************************************************************
#	Classes
#***************************************************************
class Motor(Resource):
  def get(self, direct, velocity):
    velocity = calculate_velocity(velocity)
    if direct == 'right':
      motor_left.forward(velocity)
      return {"message": "RIGHT movement started"}, 200
    elif direct == 'left':
      motor_left.forward(velocity)
      return {"message": "LEFT movement started"}, 200
    elif direct == 'forward':
      motor_left.forward(velocity)
      motor_left.forward(velocity)
      return {"message": "FORWARD movement started"}, 200
    elif direct == 'backward':
      motor_left.backward(velocity)
      motor_left.backward(velocity)
      return {"message": "BACKWARD movement started"}, 200
    elif direct == 'stop':
      motor_left.stop()
      motor_left.stop()
      return {"message": "Motors stopped"}, 200
    else:
      return {"message": "Direction '{}' not found".format(direction)}, 400

class Horn(Resource):
  def get(self, status):
    if status == 'Horn1':
      horn_1.backward()
      return {"message": "Short horn sound is played back."}, 200
    elif status == 'Horn2':
      horn_1.stop()
      return {"message": "Playback of short horn sound is stopped."}, 200
    else:
      return {"message": "Parameter ON/OFF is either missing or not valid"}, 400

class Led(Resource):
  def get(self, position, status):
    if position == 'right_led':
      if status == 'on':
        led_right.on()
        return {"message": "RIGHT LED is turned on"}, 200
      elif status == 'off':
         led_right.off()
        return {"message": "RIGHT LED is turned off"}, 200
      else:
        return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
    if position == 'left_led':
      if status == 'on':
        led_left.on()
        return {"message": "LEFT LED is turned on"}, 200
      elif status == 'off':
        led_left.off()
        return {"message": "LEFT LED is turned off"}, 200
      else:
        return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
    else:
      return {"message": "Position '{}' not found".format(direction)}, 400

app = Flask(__name__)
api = Api(app)
api.add_resource(Motor, '/<string:direct>/<string:status>/<float:velocity>')
api.add_resource(Horn, '/<string:status>')
api.add_resource(Led, '/<string:position>/<string:status>')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
