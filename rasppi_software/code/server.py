
from flask import Flask, request
from flask_restful import Api, Resource
from motor_ctrl import motor_left, motor_right
from motor_ctrl import direction

import os

#***************************************************************
#	Global-Functions
#***************************************************************

class Motor(Resource):
    def get(self, direction, status, velocity):
        if direction == 'right':
            if status == 'on':
                motor_left.run(direction.FORWARD, velocity)
                return {"message": "RIGHT movement started"}, 200
            elif status == 'off':
                motor_left.stop()
                return {"message": "RIGHT movement stopped"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        elif direction == 'left':
            if status == 'on':
                motor_right.run(direction.FORWARD, velocity)
                return {"message": "LEFT movement started"}, 200
            elif status == 'off':
                motor_right.stop()
                return {"message": "LEFT movement stopped"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        elif direction == 'forward':
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
        elif direction == 'backward':
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

app = Flask(__name__)
api = Api(app)
api.add_resource(Motor, '/<string:direction>/<string:status>/<float:velocity>')
api.add_resource(Horn, '/<string:status>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
