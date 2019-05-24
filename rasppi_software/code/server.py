
from flask import Flask, request
from flask_restful import Api, Resource
from motor_ctrl import motor_left, motor_right
from motor_ctrl import direction

from led import LED_RIGHT, LED_LEFT
import RPi.GPIO as GPIO

import os


def calculate_velocity(velocity):
    calc_velocity = 0
    if velocity <= 5.0:
        calc_velocity = 0
    elif velocity <= 15.0:
        calc_velocity = 10
    elif velocity <= 25.0:
        calc_velocity = 20
    elif velocity <= 35.0:
        calc_velocity = 30
    elif velocity <= 45.0:
        calc_velocity = 40
    elif velocity <= 55.0:
        calc_velocity = 50
    elif velocity <= 65.0:
        calc_velocity = 60
    elif velocity <= 75.0:
        calc_velocity = 70
    elif velocity <= 85.0:
        calc_velocity = 80
    elif velocity <= 95.0:
        calc_velocity = 90
    else:
        calc_velocity = 100
    return calc_velocity

#***************************************************************
#	Global-Functions
#***************************************************************

class Motor(Resource):
    def get(self, direct, status, velocity):
        velocity = calculate_velocity(velocity)
        if direct == 'right':
            if status == 'on':
                motor_left.run(direction.FORWARD, velocity=None)
                return {"message": "RIGHT movement started"}, 200
            elif status == 'off':
                motor_left.stop()
                return {"message": "RIGHT movement stopped"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        elif direct == 'left':
            if status == 'on':
                motor_right.run(direction.FORWARD, velocity)
                return {"message": "LEFT movement started"}, 200
            elif status == 'off':
                motor_right.stop()
                return {"message": "LEFT movement stopped"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        elif direct == 'forward':
            if status == 'on':
                motor_right.run(direction.FORWARD, velocity)
                motor_left.run(direction.FORWARD, velocity)
                return {"message": "FORWARD movement started"}, 200
            elif status == 'off':
                motor_right.stop()
                motor_left.stop()
                return {"message": "BACKWARD movement started"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        elif direct == 'backward':
            if status == 'on':
                motor_right.run(direction.BACKWARD, velocity)
                motor_left.run(direction.BACKWARD, velocity)
                return {"message": "BACKWARD movement started"}, 200
            elif status == 'off':
                motor_right.stop()
                motor_left.stop()
                return {"message": "BACKWARD movement stopped"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        else:
            return {"message": "Direction '{}' not found".format(direction)}, 400

class Horn(Resource):
    def get(self, status):
        if status == 'Horn1':
             os.system('mpg321 /home/pi/SoSoBot/rasppi_software/code/horn1.mp3 &')
             return {"message": "Short horn sound is played back."}, 200
        elif status == 'Horn2':
              os.system('mpg321 /home/pi/SoSoBot/rasppi_software/code/horn2.mp3 &')
              return {"message": "Playback of short horn sound is stopped."}, 200
        else:
            return {"message": "Parameter ON/OFF is either missing or not valid"}, 400

class Led(Resource):
    def get(self, position, status):
        if position == 'right_led':
            if status == 'on':
                GPIO.output(LED_RIGHT, 1)
                return {"message": "RIGHT LED is turned on"}, 200
            elif status == 'off':
                GPIO.output(LED_RIGHT, 0)
                return {"message": "RIGHT LED is turned off"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        if position == 'left_led':
            if status == 'on':
                GPIO.output(LED_LEFT, 1)
                return {"message": "LEFT LED is turned on"}, 200
            elif status == 'off':
                GPIO.output(LED_LEFT, 0)
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
