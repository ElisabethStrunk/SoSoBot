
from flask import Flask, request
from flask_restful import Api, Resource
from motor_ctrl import motor_left, motor_right

#***************************************************************
#	Global-Functions
#***************************************************************

class Motor(Resource):
    def get(self, direction, status):
        if direction == 'right':
            if status == 'on':
                motor_right.forward()
                return {"message": "RIGHT movement started"}, 200
            elif status == 'off':
                motor_right.stop()
                return {"message": "RIGHT movement stopped"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        elif direction == 'left':
            if status == 'on':
                motor_left.forward()
                return {"message": "LEFT movement started"}, 200
            elif status == 'off':
                motor_left.stop()
                return {"message": "LEFT movement stopped"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        elif direction == 'forward':
            if status == 'on':
                motor_right.forward()
                motor_left.forward()
                return {"message": "FORWARD movement started"}, 200
            elif status == 'off':
                motor_right.stop()
                motor_left.stop()
                return {"message": "BACKWARD movement started"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        elif direction == 'backward':
            if status == 'on':
                motor_right.backward()
                motor_left.backward()
                return {"message": "BACKWARD movement started"}, 200
            elif status == 'off':
                motor_right.stop()
                motor_left.stop()
                return {"message": "BACKWARD movement stopped"}, 200
            else:
                return {"message": "Parameter ON/OFF is either missing or not valid"}, 400
        else:
            return {"message": "Direction '{}' not found".format(direction)}, 400


app = Flask(__name__)
api = Api(app)
api.add_resource(Motor, '/<string:direction>/<string:status>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
